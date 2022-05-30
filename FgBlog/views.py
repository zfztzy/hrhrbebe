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


def realHome(request):
    return render(request, 'index.html')


def project_status_monthly(request):
    if request.method == 'POST':
        projectStatusMonthly()
        return JsonResponse({'msg': 'startTask'}, safe=False)


def get_applicant_info(request):
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
            target = models.ApplicantInfo.objects.filter(**filterData).order_by('-key')
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
            target = models.ApplicantInfo.objects.all().order_by('-key')
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
                target = models.RecruitmentInfo.objects.filter(**filterData).order_by('-key')
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
                target = models.RecruitmentInfo.objects.all().order_by('-key')
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
            if i.date == yearMonth or int(i.date) > int(yearMonth):
                canEdit = True
            else:
                canEdit = False
            project_num = i.project_num
            if project_num == '':
                project_num = 0
            else:
                project_num = int(project_num)
            new_project_num = i.new_project_num
            if new_project_num == '':
                new_project_num = 0
            else:
                new_project_num = int(new_project_num)
            offset_num = i.offset_num
            if offset_num == '':
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
                'monthly_target_reach': str((int(i.monthly_reach) / int(i.monthly_target)) * 100)[:5] + '%' if i.monthly_target != '' and int(
                    i.monthly_target) != 0 else 0,
                'remarks': i.remarks,
                'project_num_all': offset_num + new_project_num,
                'project_satisfaction': str((project_num / int(i.sow_num)) * 100)[:5] + '%' if int(i.sow_num) != 0 else 0,
                'canEdit': canEdit
            }
            infoList.append(info)
        data = {'infoList': infoList}
        if selectDate == str(datetime.date.today()).replace('-', '')[:6] and int(str(datetime.date.today()).replace('-', '')[6:8]) > 4:
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
    for i in range(len(data)): # 行
        a = data.loc[i]
        target = {}
        for r in range(1, len(n)): # 列
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
            res = {'infoList': '11111'}
            return JsonResponse(res, safe=False)
        else:
            target = models.ProjectInfo.objects
            target.update_or_create(**data)
            res = {'infoList': '11111'}
            return JsonResponse(res, safe=False)


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
        if target['date'] == yearMonth or int(target['date']) > int(yearMonth):
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
            target['monthly_target_reach'] = str((int(target['monthly_reach']) / int(target['monthly_target'])) * 100)[:5] + '%'
        except:
            target['monthly_target_reach'] = '0%'
        target['project_num_all'] = offset_num + new_project_num,
        target['project_satisfaction'] = str((project_num / int(target['sow_num'])) * 100)[:5] + '%' if int(target['sow_num']) != 0 else 0,
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
        print(type(tableType))
        print(tableType)
        if tableType == 'project_info':
            res = get_project_info(request)
        if tableType == 'pdu_info':
            res = get_pdu_info(request)
        if tableType == 'po_info' or tableType == 'po_list':
            res = get_po_info(request)
        return res
# Anaconda
# export PATH=$PATH:/home/fg/anaconda3/bin


# uwsgi –http :8000 chdir /home/fg/fgBlog/fgBlog –module django_wsgi
