from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from FgBlog.batchOutput.batchOutput import getFileList
from FgBlog.batchOutput.batchOutput import newDownloadExcel, readJson
import time
from pyquery import PyQuery as pq
from hr_manage_db import models
import pandas as pd
import openpyxl
import xlrd
import json
import datetime
from FgBlog.commonMethods import projectStatusMonthly
from FgBlog.commonMethods import selectDepartment
from FgBlog.commonMethods import get_final_pic_value
from FgBlog.commonMethods import getPicData2
from django import forms


def realHome(request):
    return render(request, 'index.html')


def project_status_monthly(request):
    if request.method == 'POST':
        projectStatusMonthly()
        return JsonResponse({'msg': 'startTask'}, safe=False)


def get_applicant_info(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            print(type(req))
            print(req)
            filterData = req.get('filterData')
            filterRegion = req.get('filterRegion')
            filterNickname = req.get('filterNickname')
            # 角色判断
            role = models.UserInfo.objects.filter(nickname__icontains=filterNickname).first()
            if not role:
                return JsonResponse({"status": False, 'error': "登录异常。"})

            # 筛选器
            if filterData:
                print(filterData)
                for i in list(filterData.keys()):
                    if filterData[i] == '':
                        filterData.pop(i)
                target = models.ApplicantInfo.objects.filter(**filterData).order_by('-key')
            else:
                target = models.ApplicantInfo.objects.all().order_by('-key')
            # 角色筛选
            # 如果当前角色为招聘,只筛选推荐人为当前登录人的候选人信息
            if role.level == "4":
                target = target.filter(recommender__icontains=filterNickname)
            # 地域筛选
            elif filterRegion and filterRegion != 'null' and filterRegion != 'all':
                print(f'region:{filterRegion}')
                regionList = filterRegion.split('|')
                targetList = []
                for i in regionList:
                    targetList.append(target.filter(region__icontains=i))
                target = ''
                for i in targetList:
                    if target == '':
                        target = i
                    else:
                        target = target | i

            # 整理返回数据
            applicantList = []
            for index in range(len(target)):
                i = target[index]
                applicant = model_to_dict(i)
                for k in applicant.keys():
                    if applicant[k] is None:
                        applicant[k] = ''
                applicantList.append(applicant)
            data = {'applicantList': applicantList}
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"status": False, 'error': str(e)})


def applicant_according_to_recruitment(request):
    data = json.loads(request.body.decode('utf-8'))
    recruitmentId = data.get('recruitmentId')
    info = {}
    totalTarget = models.ApplicantInfo.objects.all().filter(related=recruitmentId)
    total = len(totalTarget)
    fail = len(totalTarget.filter(process_status__icontains='不通过')) if totalTarget.filter(
        process_status__icontains='不通过') else 0
    done = len(totalTarget.filter(process_status__icontains='已入职')) if totalTarget.filter(
        process_status__icontains='已入职') else 0
    giveUp = len(totalTarget.filter(process_status__icontains='放弃offer')) if totalTarget.filter(
        process_status__icontains='放弃offer') else 0
    discuss = len(totalTarget.filter(process_status__icontains='谈offer中')) if totalTarget.filter(
        process_status__icontains='谈offer中') else 0
    standBy = len(totalTarget.filter(process_status__icontains='待入职')) if totalTarget.filter(
        process_status__icontains='待入职') else 0
    created = len(totalTarget.filter(process_status__icontains='创建')) if totalTarget.filter(
        process_status__icontains='创建') else 0
    filtering = len(totalTarget.filter(process_status__icontains='通过')) if totalTarget.filter(
        process_status__icontains='通过') else 0
    info['total'] = total
    info['done'] = done
    info['discuss'] = discuss
    info['standBy'] = standBy
    info['filtering'] = filtering + created + standBy + discuss
    info['fail'] = fail
    info['giveUp'] = giveUp
    print(info)
    return JsonResponse(info, safe=False)


def get_recruitment_info(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            print(type(req))
            print(req)
            filterData = req.get('filterData')
            filterRegion = req.get('filterRegion')
            if filterData:
                print(filterData)
                for i in list(filterData.keys()):
                    if filterData[i] == '':
                        filterData.pop(i)
                print(filterData)
                target = models.RecruitmentInfo.objects.exclude(status='关闭').filter(**filterData).order_by('-key')
                if filterRegion and filterRegion != 'null' and filterRegion != 'all':
                    print(f'region:{filterRegion}')
                    regionList = filterRegion.split('|')
                    targetList = []
                    for i in regionList:
                        targetList.append(target.filter(region__icontains=i))
                    print(regionList)
                    print(targetList)
                    target = ''
                    for i in targetList:
                        if target == '':
                            target = i
                        else:
                            target = target | i
            else:
                print(1)
                target = models.RecruitmentInfo.objects.all().exclude(status='关闭').order_by('-key')
                if filterRegion and filterRegion != 'null' and filterRegion != 'all':
                    print(f'region:{filterRegion}')
                    regionList = filterRegion.split('|')
                    targetList = []
                    for i in regionList:
                        targetList.append(target.filter(region__icontains=i))
                    print(regionList)
                    print(targetList)
                    target = ''
                    for i in targetList:
                        if target == '':
                            target = i
                        else:
                            target = target | i
            infoList = []
            for index in range(len(target)):
                i = target[index]
                info = model_to_dict(i)
                for k in info.keys():
                    if info[k] is None:
                        info[k] = ''
                infoList.append(info)
            data = {'infoList': infoList}
            return JsonResponse(data, safe=False)
        except Exception as e:
            print(str(e))


def get_file_list(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        fileType = data.get('batchType')
        userName = data.get('userName')
        print(fileType)
        fileList = getFileList(fileType, userName)
        data = {'fileList': fileList}
        return JsonResponse(data, safe=False)


def new_download_excel(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        fileType = data.get('batchType')
        selectDate = data.get('selectDate')
        filterRegion = data.get('filterRegion')
        userName = data.get('userName')
        print(fileType)
        fileInfo = newDownloadExcel(fileType, userName=userName, region=filterRegion, selectDate=selectDate)
        data = {'fileInfo': fileInfo}
        return JsonResponse(data, safe=False)


def get_department_list(request):
    if request.method == 'POST':
        target = models.RecruitmentInfo.objects.values('department').all().distinct()
        departmentList = []
        for i in target:
            department = i['department']
            departmentList.append(department)
        print(departmentList)
        res = {'departmentList': departmentList}
        return JsonResponse(res, safe=False)


def get_project_status_info(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        print(type(req))
        print(req)
        selectDate = req.get('selectDate')
        filterRegion = req.get('filterRegion')
        if selectDate:
            target = models.ProjectStatusInfo.objects.all().filter(date=selectDate).order_by('-key')
        else:
            selectDate = str(datetime.date.today()).replace('-', '')[:6]
            target = models.ProjectStatusInfo.objects.all().filter(date=selectDate).order_by('-key')
        if filterRegion and filterRegion != 'null' and filterRegion != 'all':
            print(f'region:{filterRegion}')
            regionList = filterRegion.split('|')
            targetList = []
            for i in regionList:
                targetList.append(target.filter(region__icontains=i))
            print(regionList)
            print(targetList)
            target = ''
            for i in targetList:
                if target == '':
                    target = i
                else:
                    target = target | i
        infoList = []
        date = str(datetime.date.today())
        print(date)
        # date = '2022-04-04'
        date = date.replace('-', '')
        yearMonth = date[:6]
        for i in range(len(target)):
            ii = i
            i = target[i]
            if int(i.date) * 100 + 104 > int(date):
                canEdit = True
            else:
                canEdit = False
            project_num = i.project_num
            if project_num == '' or not project_num:
                project_num = 0
            else:
                project_num = int(project_num)
            new_project_num = i.new_project_num
            if new_project_num == '' or not new_project_num:
                new_project_num = 0
            else:
                new_project_num = int(new_project_num)
            offset_num = i.offset_num
            if offset_num == '' or not offset_num:
                offset_num = 0
            else:
                offset_num = int(offset_num)
            info = {
                'key': i.key,
                'date': i.date,
                'department': i.department,
                'pdu': i.pdu,
                'po_num': i.po_num,
                'project': i.project,
                'region': i.region,
                'sow_num': i.sow_num,
                'project_num': i.project_num,
                'new_project_num': i.new_project_num,
                'offset_num': i.offset_num,
                'monthly_target': i.monthly_target,
                'urgency': i.urgency,
                'monthly_reach': i.monthly_reach,
                'monthly_target_reach': str((int(i.monthly_reach) / int(i.monthly_target)) * 100)[
                                        :5] + '%' if i.monthly_target and i.monthly_target != '' and int(
                    i.monthly_target) != 0 else 0,
                'remarks': i.remarks,
                'project_num_all': offset_num + new_project_num,
                'project_satisfaction': str((project_num / int(i.sow_num)) * 100)[:5] + '%' if i.sow_num and int(
                    i.sow_num) != 0 else 0,
                'canEdit': canEdit
            }
            infoList.append(info)
        data = {'infoList': infoList}
        if selectDate == str(datetime.date.today()).replace('-', '')[:6] and int(
                str(datetime.date.today()).replace('-', '')[6:8]) > 4:
            data['remove'] = True
        return JsonResponse(data, safe=False)


def delete_project_status_info(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        deleteKey = req.get('deleteKey')
        msg = models.ProjectStatusInfo.objects.filter(key=deleteKey).delete()
        data = {'msg': msg}
        return JsonResponse(data, safe=False)


def get_project_info(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        print(type(req))
        print(req)
        filterData = req.get('filterData')
        filterRegion = req.get('filterRegion')
        if filterData:
            print(filterData)
            for i in list(filterData.keys()):
                if filterData[i] == '':
                    filterData.pop(i)
            print(filterData)
            target = models.ProjectInfo.objects.filter(**filterData)
            if filterRegion and filterRegion != 'null' and filterRegion != 'all':
                print(f'region:{filterRegion}')
                regionList = filterRegion.split('|')
                targetList = []
                for i in regionList:
                    targetList.append(target.filter(region__icontains=i))
                print(regionList)
                print(targetList)
                target = ''
                for i in targetList:
                    if target == '':
                        target = i
                    else:
                        target = target | i
        else:
            print(1)
            target = models.ProjectInfo.objects.all()
            if filterRegion and filterRegion != 'null' and filterRegion != 'all':
                print(f'region:{filterRegion}')
                regionList = filterRegion.split('|')
                targetList = []
                for i in regionList:
                    targetList.append(target.filter(region__icontains=i))
                print(regionList)
                print(targetList)
                target = ''
                for i in targetList:
                    if target == '':
                        target = i
                    else:
                        target = target | i
        infoList = []
        for index in range(len(target)):
            i = target[index]
            info = model_to_dict(i)
            for k in info.keys():
                if info[k] is None:
                    info[k] = ''
            infoList.append(info)
        data = {'tableData': infoList}
        return JsonResponse(data, safe=False)


def get_pdu_info(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        print(type(req))
        print(req)
        filterRegion = req.get('filterRegion')
        target = models.PduInfo.objects.all()
        pduList = []
        for i in target:
            pduList.append(model_to_dict(i))
        res = {'tableData': pduList}
        return JsonResponse(res, safe=False)


def get_po_info(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        print(type(req))
        print(req)
        filterRegion = req.get('filterRegion')
        target = models.PoInfo.objects.all()
        poList = []
        for i in target:
            poList.append(model_to_dict(i))
        res = {'tableData': poList}
        return JsonResponse(res, safe=False)


def update_applicant_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        for k in list(data.keys()):
            if not data[k] and data[k] != 0:
                del data[k]
        print(type(data))
        print(data)
        key = data['key']
        print(key)
        data.pop('key')
        print(data)
        target = models.ApplicantInfo.objects.filter(key=key)
        target.update(**data)
        res = {'infoList': '11111'}
        return JsonResponse(res, safe=False)


def get_columns(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        tableType = data.get('tableType')
        print(type(tableType))
        print(tableType)
        target = models.TableCol.objects.filter(table_type=tableType)
        dataIndexList = target[0].col.split(',')
        print(dataIndexList)
        nameList = target[0].name.split(',')
        print(nameList)
        widthList = target[0].width.split(',')
        print(widthList)
        columns = []
        try:
            columns = [
            ]
            for index in range(len(dataIndexList)):
                i = {
                    'title': nameList[index],
                    'dataIndex': dataIndexList[index],
                    'width': int(widthList[index]),
                    'scopedSlots': {'customRender': dataIndexList[index]},
                }
                columns.append(i)
            a = {
                'title': 'operation',
                'dataIndex': 'operation',
                'fixed': 'right',
                'scopedSlots': {'customRender': 'operation'},
                'width': 130,
            }
            columns.append(a)
            print(columns)
        except:
            print("internal_error")
        res = {'columns': columns}
        return JsonResponse(res, safe=False)


def create_applicant_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        target = models.ApplicantInfo.objects
        target.create(**data)
        res = {'msg': '新增成功'}
        return JsonResponse(res)


def create_contact_info(request):
    print("这是新增")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)

        # 检验员工工号 employee_num employee_num
        employee = models.EmployeeInfo.objects.get(rt_num=int(data["employee_num"]))
        if not employee:
            result = {
                "status": False,
                "msg": "工号不存在，请核实。"
            }
            return JsonResponse(result)
        # 对工号与员工姓名的验证
        if employee.name != data["employeename"]:
            result = {
                "status": False,
                "msg": "工号与姓名不匹配，请核实。"
            }
            return JsonResponse(result)
        # 时间format
        contact_date = data["contact_date"]
        try:
            contact_date = datetime.datetime.strptime(contact_date, '%Y%m%d')
            # contact_date = datetime.datetime.strptime(contact_date, '%Y-%m-%d')
            print(contact_date)
        except:
            result = {
                "status": False,
                "msg": "沟通日期填写错误，请按照2022-05-02格式填写。"
            }
            return JsonResponse(result, safe=False)
        # 新增
        obj = models.ContactInfo(employee_num=employee.rt_num, employeename=employee.name,
                                 charger_name=data["charger_name"],
                                 contact_date=contact_date, type=data["type"], remarks=data["remarks"],
                                 contact_type=data["contact_type"], region=employee.region, leader=employee.pdumanager,
                                 pm=employee.pm)
        obj.save()
        result = {
            "status": True,
            "msg": "添加成功。"
        }
        return JsonResponse(result, safe=False)


def update_common_infoDB(data, modelsobject):
    try:
        for k in list(data.keys()):
            if not data[k] and data[k] != 0:
                del data[k]
        key = data['key']
        print(key)

        target = modelsobject.filter(key=key)
        target.update(**data)
        result = {
            "status": True,
            "msg": "更新成功"
        }

    except Exception as e:
        result = {
            "status": False,
            "msg": e
        }
    return JsonResponse(result)


def update_contact_info(request):
    print("这是修改")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')

        return update_common_infoDB(data, models.ContactInfo.objects)


def get_pdu_list(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        department = data.get('department')
        print(type(department))
        print(department)
        pduList = selectDepartment(department, None)
        res = {'pduList': pduList}
        return JsonResponse(res)


def create_recruitment_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        data['proposed_time'] = datetime.datetime.now()
        print(data)
        data.pop('key')
        target = models.RecruitmentInfo.objects
        target.create(**data)
        res = {'msg': '新增成功'}
        return JsonResponse(res)


def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            userInfo = data.get('userInfo')
            print(userInfo)
            if userInfo['user_name'] is None or userInfo['password'] is None:
                res = {'msg': '未登录或登录过期'}
                return JsonResponse(res)
            user_name = userInfo['user_name'][:-5]
            password = userInfo['password'][:-5]
            target = models.UserInfo.objects.filter(user_name=user_name)
            if len(target) == 0:
                res = {'msg': '账号或密码错误'}
                return JsonResponse(res)
            if password != target[0].password:
                res = {'msg': '密码错误'}
                return JsonResponse(res)
            if password == target[0].password:
                res = {
                    'msg': 'pass',
                    'nickname': target[0].nickname,
                    'region': target[0].region,
                    'level': target[0].level
                }
                target = models.UserLevel.objects.filter(level=res['level'])[0]
                limits = model_to_dict(target)
                res['limits'] = limits
                return JsonResponse(res)
        except:
            res = {'msg': '内部错误'}
            return JsonResponse(res)


def batchInputExcel(path, excelType):
    if excelType == 'ApplicantInfo':
        fileName = 'applicant_info'
    if excelType == 'ProjectInfo':
        fileName = 'project_info'
    if excelType == 'ProjectStatusInfo':
        fileName = 'project_status_info'
    if excelType == 'RecruitmentInfo':
        fileName = 'recruitment_info'
    # data = pd.read_excel(path)
    # print(type(data))
    # print("len(data):", len(data))
    # n = []
    # m = readJson(fileName)
    data = pd.read_excel(path)
    print(type(data))
    print("len(data):", len(data))
    n = []
    # nn = []
    m = readJson(fileName)
    # for i in range(len(m)):
    #     print(data.columns[i])
    #     print(type(data.columns[i]))
    #     nn.append(data.columns[i])
    for i in m:
        n.append(i)
    for i in range(len(data)):  # 行
        a = data.loc[i]
        target = {}
        for r in range(1, len(n)):  # 列
            # print(n[r])
            # print(a[r])
            if a[r] is not None and a[r] != 'None' and a[r] != 'nan':
                target[n[r]] = a[r]
        for r in target:
            print(r)
            print(target[r])
            print(type(target[r]))
        print(target)
        try:
            if excelType == 'ApplicantInfo':
                models.ApplicantInfo.objects.create(**target)
            if excelType == 'ProjectInfo':
                models.ProjectInfo.objects.create(**target)
            if excelType == 'ProjectStatusInfo':
                if not target['arrival_num']:
                    target['arrival_num'] = 0
                models.ProjectStatusInfo.objects.create(**target)
            if excelType == 'RecruitmentInfo':
                models.RecruitmentInfo.objects.create(**target)
        except:
            print(f'第{i}条数据没进')


def save_excel(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        excelType = request.POST.get('type')
        fileName = file.name
        print(file, type(file))
        savePath = 'FgBlog/uploadFile/{}'.format(fileName)
        with open(savePath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        batchInputExcel(savePath, excelType)
        res = {'msg': '导入成功', 'type': excelType}
        return JsonResponse(res)


def update_recruitment_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        try:
            data.pop('total')
            data.pop('fail')
            data.pop('discuss')
            data.pop('filtering')
            data.pop('giveUp')
            data.pop('done')
            data.pop('standBy')
        except:
            print('还没加载项目人数')
        for k in list(data.keys()):
            if not data[k] and data[k] != 0:
                del data[k]
        print(type(data))
        print(data)
        key = data['key']
        print(key)
        data.pop('key')
        print(data)
        target = models.RecruitmentInfo.objects.filter(key=key)
        target.update(**data)
        res = {'infoList': '11111'}
        return JsonResponse(res, safe=False)


def update_project_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        for k in list(data.keys()):
            if not data[k] and data[k] != 0:
                del data[k]
        print(type(data))
        print(data)
        key = data['key']
        print(key)
        data.pop('key')
        print(data)
        if key != 0:
            target = models.ProjectInfo.objects.filter(key=key)
            target.update(**data)
            result = {
                "status": True,
                "msg": "更新成功。"
            }
            return JsonResponse(result, safe=False)
            # return JsonResponse(res, safe=False)
        else:
            target = models.ProjectInfo.objects
            target.update_or_create(**data)
            result = {
                "status": True,
                "msg": "添加成功。"
            }
            return JsonResponse(result, safe=False)
            # return JsonResponse(res, safe=False)


def get_status_pic_value(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('selectDate')
        print(type(data))
        print(data)
        if not data:
            data = str(datetime.date.today()).split('-')
            data = data[0] + data[1]
            print('########')
            print(data)
        value = get_final_pic_value(data)
        res = {'picData': value}
        return JsonResponse(res, safe=False)


def create_project_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        try:
            models.ProjectStatusInfo.objects.create(**data)
            res = '新增成功'
        except Exception as e:
            res = e
        res = {'data': res}
        return JsonResponse(res, safe=False)


def update_project_status(request):
    if request.method == 'POST':
        # data = json.loads(request.body.decode('utf-8'))
        # data = data.get('data')
        # print(type(data))
        # print(data)
        # data.pop('key')
        # data.pop('project_satisfaction')
        # data.pop('project_num_all')
        # data.pop('mouthly_target_reach')
        # target = models.ProjectStatusInfo.objects.filter(id=data['id'])
        # target.update(**data)
        # res = {'infoList': '11111'}
        # return JsonResponse(res, safe=False)
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        for k in list(data.keys()):
            if not data[k] and data[k] != 0:
                del data[k]
        data.pop('project_satisfaction')
        data.pop('project_num_all')
        data.pop('monthly_target_reach')
        data.pop('canEdit')
        print(type(data))
        print(data)
        key = data['key']
        print(key)
        data.pop('key')
        print(data)
        target = models.ProjectStatusInfo.objects.filter(key=key)
        target.update(**data)
        target = model_to_dict(models.ProjectStatusInfo.objects.filter(key=key)[0])
        date = str(datetime.date.today())
        print(date)
        # date = '2022-04-04'
        date = date.replace('-', '')
        yearMonth = date[:6]
        if target['date'] + '04' == date or int(target['date']) * 100 + 4 > int(date):
            canEdit = True
        else:
            canEdit = False
        project_num = target['project_num']
        if project_num == '':
            project_num = 0
        else:
            project_num = int(project_num)
        new_project_num = target['new_project_num']
        if new_project_num == '':
            new_project_num = 0
        else:
            new_project_num = int(new_project_num)
        offset_num = target['offset_num']
        if offset_num == '':
            offset_num = 0
        else:
            offset_num = int(offset_num)
        try:
            target['monthly_target_reach'] = str((int(target['monthly_reach']) / int(target['monthly_target'])) * 100)[
                                             :5] + '%'
        except:
            target['monthly_target_reach'] = '0%'
        target['project_num_all'] = offset_num + new_project_num,
        target['project_satisfaction'] = str((project_num / int(target['sow_num'])) * 100)[:5] + '%' if int(
            target['sow_num']) != 0 else 0,
        target['canEdit'] = canEdit
        res = {'data': target}
        return JsonResponse(res, safe=False)


def get_applicant_pic(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        print(req)
        print(type(req))
        picValue = getPicData2(req)
        res = {'picValue': picValue}
        return JsonResponse(res, safe=False)


def get_applicant_region(request):
    if request.method == 'POST':
        regionList = models.ApplicantInfo.objects.values('region').distinct()
        regionList2 = []
        for i in regionList:
            regionList2.append(i['region'])
        res = {'regionList': regionList2}
        return JsonResponse(res, safe=False)


def get_common_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        tableType = data.get('tableType')
        res = JsonResponse({'msg': 'error'}, safe=False)
        poList = []
        print(type(tableType))
        print(tableType)
        if tableType == 'project_info':
            res = get_project_info(request)
        if tableType == 'pdu_info':
            res = get_pdu_info(request)
        if tableType == 'po_info' or tableType == 'po_list':
            res = get_po_info(request)
        if tableType == 'contact':
            # res = get_common_fromDB(request, models.ContactInfo)
            res = get_contact_info(request)
            # target = models.ContactInfo.objects.all()
            # tar = models.EmployeeInfo.objects.get(rt_num=18403)
            # obj = models.ContactInfo(employee_num=tar, charger_name="halou")
            # obj.save()
        # contact.employee_num = 18403
        #
        #
        #
        #  target = models.ContactInfo.objects.all().first()
        #  targets = target.objects.select_related("employee_num__employee_info")
        #  poList = []
        #  for i in targets:
        #      poList.append(model_to_dict(i))
        #  res = {'tableData': poList}
        #  return JsonResponse("res", safe=False)
        # res = get_common_fromDB(request,models.ContactInfo)
        if tableType == 'employee' or tableType == 'employeenum':
            res = get_common_fromDB(request, models.EmployeeInfo)
        return res


def create_common_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        tableType = data.get('tableType')
        # res = JsonResponse({'msg': 'error'}, safe=False)
        data = data.get('data')
        print(type(data))
        print(data)
        if tableType == 'contact':
            res = create_contact_info(request)
            # target = models.ContactInfo.objects
            # target.create(**data)
            # res = JsonResponse(res)
        return res


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = models.ContactInfo
        fields = "__all__"
        # fields = [""]


# def update_contact_info(request):
#     if request.method == 'POST':
#        data = json.loads(request.body.decode('utf-8'))
#        data = data.get('data')
#     for k in list(data.keys()):
#         if not data[k] and data[k] != 0:
#             del data[k]
#     key = data['key']
#     print(key)
#     data.pop('key')
#     print(data)
#     if key != 0:
#         row_object = models.ContactInfo.objects.filter(key=key)
#         if not row_object.first:
#             result = {
#                 "status": False,
#                 "msg": "数据不存在，请刷新重试。"
#             }
#             return JsonResponse(result)
#         # 对工号的验证
#         employeenum = models.ContactInfo.objects.filter(key=key).first().employee_num
#         employee = models.EmployeeInfo.objects.filter(rt_num=employeenum).first()
#         if not employee:
#             result = {
#                 "status": False,
#                 "msg": "工号错误，请重新填写。"
#             }
#             return JsonResponse(result)
#             # return JsonResponse({'msg': "工号错误，请重新填写。"})
#         # datetime没有强制转化。
#         row_object.update(**data)
#         result = {
#             "status": True,
#             "msg": "更新成功。"
#         }
#         # res = {'msg': 'update success'}
#         # return JsonResponse(result, safe=False)
#     else:
#         target = models.ContactInfo.objects
#         target.update_or_create(**data)
#         result = {
#             "status": True,
#             "msg": "更新成功。"
#         }
#         # res = {'msg': 'update success'}
#     return JsonResponse(result, safe=False)


def update_common_info(request):
    print("这是修改")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        tableType = data.get('tableType')
        res = JsonResponse({'msg': 'error'}, safe=False)
        data = data.get('data')
        print(type(data))
        print(data)
        if tableType == 'contact':
            res = update_contact_info(request)
        if tableType == 'project_info':
            res = update_project_info(request)
        return res


def get_contact_info(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            filterData = req.get('filterData')
            filterRegion = req.get('filterRegion')
            filterNickname = req.get('filterNickname')

            # 判断登录人员
            role = models.UserInfo.objects.get(nickname=filterNickname)
            if not role:
                return JsonResponse({"status": False, 'error': "登录异常。"})

            # 筛选器
            if filterData:
                print(filterData)
                for i in list(filterData.keys()):
                    if filterData[i] == '':
                        filterData.pop(i)
                target = models.ContactInfo.objects.filter(**filterData).order_by('-key')
            else:
                target = models.ContactInfo.objects.all().order_by('-key')

            # 角色筛选。 如果当前角色为交付主管,只筛选其下员工的沟通信息
            if role.level == "3":
                target = target.filter(leader__icontains=filterNickname)
            # 地域筛选
            elif filterRegion and filterRegion != 'null' and filterRegion != 'all':
                print(f'region:{filterRegion}')
                regionList = filterRegion.split('|')
                targetList = []
                for i in regionList:
                    targetList.append(target.filter(region__icontains=i))
                target = ''
                for i in targetList:
                    if target == '':
                        target = i
                    else:
                        target = target | i

            # 整理返回数据
            applicantList = []
            for index in range(len(target)):
                i = target[index]
                applicant = model_to_dict(i)
                for k in applicant.keys():
                    if applicant[k] is None:
                        applicant[k] = ''
                applicantList.append(applicant)
            data = {'tableData': applicantList}
            return JsonResponse(data, safe=False)
        except Exception as e:
            result = {
                "status": False,
                "msg": str(e)
            }
            return JsonResponse(result)


def get_common_fromDB(request, modelsobject):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            print(type(req))
            print(req)
            filterData = req.get('filterData')
            filterRegion = req.get('filterRegion')
            if filterData:
                print(filterData)
                for i in list(filterData.keys()):
                    if filterData[i] == '':
                        filterData.pop(i)
                print(filterData)
                target = modelsobject.objects.filter(**filterData).order_by('-key')
            else:
                print(1)
                target = modelsobject.objects.all().order_by('-key')
            if filterRegion and filterRegion != 'null' and filterRegion != 'all':
                print(f'region:{filterRegion}')
                regionList = filterRegion.split('|')
                targetList = []
                for i in regionList:
                    targetList.append(target.filter(region__icontains=i))
                print(regionList)
                print(targetList)
                target = ''
                for i in targetList:
                    if target == '':
                        target = i
                    else:
                        target = target | i
            infoList = []
            for index in range(len(target)):
                i = target[index]
                info = model_to_dict(i)
                for k in info.keys():
                    if info[k] is None:
                        info[k] = ''
                infoList.append(info)
            data = {'tableData': infoList}
            print("========================================")
            print(infoList)
            return JsonResponse(data, safe=False)
        except Exception as e:
            print(str(e))
            return JsonResponse(str(e), safe=False)


def getRegionListTarget(region, regionTarget):
    if region == 'all':
        return regionTarget
    regionList = region.split('|')
    targetList = []
    for i in regionList:
        targetList.append(regionTarget.filter(region__icontains=i))
    target = ''
    for i in targetList:
        if target == '':
            target = i
        else:
            target = target | i
    return target


def getPduRecruitmentPic(region, picType):
    typeKeyList = []
    if picType == 'pdu':
        target = models.RecruitmentInfo.objects.values('pdu').distinct()
        target = getRegionListTarget(region, target)
        for i in target:
            typeKeyList.append(i['pdu'])
    if picType == 'job':
        target = models.RecruitmentInfo.objects.values('position_attribute').distinct()
        target = getRegionListTarget(region, target)
        for i in target:
            typeKeyList.append(i['position_attribute'])
    # if picType == 'region':
    #     target = models.RecruitmentInfo.objects.values('region').distinct()
    #     target = getRegionListTarget(region, target)
    #     for i in target:
    #         typeKeyList.append(i['region'])
    SumList = []
    slaList = []
    xData = []
    Sub1Sum = 0
    Sub2Sum = 0
    Sub1Sla = 0
    Sub2Sla = 0
    hsbdt = getPduRecruitmentPduSum(region, '海思半导体')
    Sub1Sum = hsbdt['SumList']
    Sub1Sla = hsbdt['slaList']
    shhs = getPduRecruitmentPduSum(region, '上海海思')
    Sub2Sum = shhs['SumList']
    Sub2Sla = shhs['slaList']
    for key in typeKeyList:
        if picType == 'pdu':
            target = models.RecruitmentInfo.objects.filter(pdu=key, status__icontains='进行中')
            target = getRegionListTarget(region, target)
        if picType == 'job':
            target = models.RecruitmentInfo.objects.filter(position_attribute=key, status__icontains='进行中')
            target = getRegionListTarget(region, target)
        # if picType == 'region':
        #     target = models.RecruitmentInfo.objects.filter(region=key, status__icontains='进行中')
        #     target = getRegionListTarget(region, target)
        pduSum = 0
        sla = 0
        for i in target:
            if i.type2 == 'SLA':
                sla += (int(i.num) - int(i.arrival_num))
            pduSum += (int(i.num) - int(i.arrival_num))
        if pduSum == 0:
            continue
        # print(key)
        # print(pduSum)
        # print(sla)
        xData.append(key)
        slaList.append(sla)
        SumList.append(pduSum)
    return {
        'xData': xData,
        'slaList': slaList,
        'SumList': SumList,
        'Sub1Sum': Sub1Sum,
        'Sub2Sum': Sub2Sum,
        'Sub1Sla': Sub1Sla,
        'Sub2Sla': Sub2Sla
    }


def getPduRecruitmentPduSum(region, department):
    typeKeyList = []
    target = models.RecruitmentInfo.objects.values('pdu').distinct()
    target = getRegionListTarget(region, target)
    for i in target:
        typeKeyList.append(i['pdu'])
    SumList = []
    slaList = []
    xData = []
    for key in typeKeyList:
        target = models.RecruitmentInfo.objects.filter(pdu=key, status__icontains='进行中', department=department)
        target = getRegionListTarget(region, target)
        # if picType == 'region':
        #     target = models.RecruitmentInfo.objects.filter(region=key, status__icontains='进行中')
        #     target = getRegionListTarget(region, target)
        pduSum = 0
        sla = 0
        for i in target:
            if i.type2 == 'SLA':
                sla += (int(i.num) - int(i.arrival_num))
            pduSum += (int(i.num) - int(i.arrival_num))
        if pduSum == 0:
            continue
        xData.append(key)
        slaList.append(sla)
        SumList.append(pduSum)
        # print(key)
        # print(pduSum)
        # print(sla)
    return {
        'slaList': sum(slaList),
        'SumList': sum(SumList)
    }


def get_recruitmentInfo_pic(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        region = data.get('filterRegion')
        picType = data.get('picType')
        picData = getPduRecruitmentPic(region, picType)
        res = {'picData': picData}
        return JsonResponse(res, safe=False)


def get_recruitmentInfo_pdu_sum(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        region = data.get('filterRegion')
        department = data.get('department')
        sumData = getPduRecruitmentPduSum(region, department)
        res = {'sumData': sumData}
        return JsonResponse(res, safe=False)







# Anaconda
# export PATH=$PATH:/home/fg/anaconda3/bi

# uwsgi –http :8000 chdir /home/fg/fgBlog/fgBlog –module django_wsgi
