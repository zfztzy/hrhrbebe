from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from FgBlog.batchOutput.batchOutput import getFileList
from FgBlog.batchOutput.batchOutput import newDownloadExcel
import time
from pyquery import PyQuery as pq
from hr_manage_db import models
import pandas as pd
import openpyxl
import xlrd
import json
import datetime



def realHome(request):
    return render(request, 'index.html')



def studyInfo2(request):
    if request.method == 'POST':
        index = request.GET.get('data')
        print(type(index))
        print(index)
        # rsp = a.getStudyInfo(index)
        return JsonResponse(index, safe=False)


def get_applicant_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('filterData')
        if data:
            print(data)
            for i in list(data.keys()):
                if data[i] == '':
                    data.pop(i)
            print(data)
            target = models.ApplicantInfo.objects.filter(**data).order_by('-id')
        else:
            print(1)
            target = models.ApplicantInfo.objects.all().order_by('-id')
        applicantList = []
        for index in range(len(target)):
            i = target[index]
            applicant = model_to_dict(i)
            applicant['key'] = index
            for k in applicant.keys():
                if applicant[k] is None:
                    applicant[k] = ''
            applicantList.append(applicant)
        data = {'applicantList': applicantList}
        return JsonResponse(data, safe=False)


def get_recruitment_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            data = data.get('filterData')
            if data:
                print(data)
                for i in list(data.keys()):
                    if data[i] == '':
                        data.pop(i)
                print(data)
                target = models.RecruitmentInfo.objects.filter(**data).order_by('-id')
            else:
                print(1)
                target = models.RecruitmentInfo.objects.all().order_by('-id')
        except:
            print(1)
            target = models.RecruitmentInfo.objects.all().order_by('-id')
        infoList = []
        for index in range(len(target)):
            i = target[index]
            info = model_to_dict(i)
            info['key'] = index
            for k in info.keys():
                if info[k] is None:
                    info[k] = ''
            infoList.append(info)
        data = {'infoList': infoList}
        return JsonResponse(data, safe=False)


def get_file_list(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        fileType = data.get('batchType')
        print(fileType)
        fileList = getFileList(fileType)
        data = {'fileList': fileList}
        return JsonResponse(data, safe=False)


def new_download_excel(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        fileType = data.get('batchType')
        print(fileType)
        fileInfo = newDownloadExcel(fileType)
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
        target = models.ProjectStatusInfo.objects.all().order_by('-id')
        infoList = []
        for i in range(len(target)):
            ii = i
            i = target[i]
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
                'key': ii,
                'id': i.id,
                'date': i.date,
                'department': i.department,
                'pdu': i.pdu,
                'project': i.project,
                'region': i.region,
                'sow_num': i.sow_num,
                'project_num': i.project_num,
                'new_project_num': i.new_project_num,
                'offset_num': i.offset_num,
                'monthly_target': i.monthly_target,
                'urgency': i.urgency,
                'mouthly_reach': i.mouthly_reach,
                'mouthly_target_reach': int(i.mouthly_reach)/int(i.monthly_target),
                'remarks': i.remarks,
                'project_num_all': offset_num + new_project_num,
                'project_satisfaction': project_num/int(i.sow_num),
            }
            infoList.append(info)
        data = {'infoList': infoList}
        return JsonResponse(data, safe=False)


def get_project_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('filterData')
        if data:
            print(data)
            for i in list(data.keys()):
                if data[i] == '':
                    data.pop(i)
            print(data)
            target = models.ProjectInfo.objects.filter(**data)
        else:
            print(1)
            target = models.ProjectInfo.objects.all()
        infoList = []
        for index in range(len(target)):
            i = target[index]
            info = model_to_dict(i)
            info['key'] = index
            for k in info.keys():
                if info[k] is None:
                    info[k] = ''
            infoList.append(info)
        data = {'infoList': infoList}
        return JsonResponse(data, safe=False)


def update_applicant_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        for k in list(data.keys()):
            if not data[k]:
                del data[k]
        print(type(data))
        print(data)
        try:
            data.pop('key')
        except:
            print("don't have key")
        target = models.ApplicantInfo.objects.filter(id=data['id'])
        target.update(**data)
        res = {'infoList': '11111'}
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
                return JsonResponse(res)
        except:
            res = {'msg': '内部错误'}
            return JsonResponse(res)


def batchInputExcel(path, excelType):
    data = pd.read_excel(path)
    print(type(data))
    print("len(data):", len(data))
    n = []
    for i in data.columns:
        n.append(i)
    for i in range(len(data)):
        a = data.loc[i]
        target = {}
        for r in range(2, len(n)):
            print(n[r])
            print(a[r])
            if a[r] is not None and a[r] != 'None' and a[r] != 'nan':
                target[n[r]] = a[r]
            print(target)
        print("#########")
        print(excelType)
        if excelType == 'ApplicantInfo':
            res = models.ApplicantInfo.objects.create(**target)
            print(res)
        if excelType == 'ProjectInfo':
            models.ProjectInfo.objects.create(**target)
        if excelType == 'ProjectStatusInfo':
            models.ProjectStatusInfo.objects.create(**target)
        if excelType == 'RecruitmentInfo':
            models.RecruitmentInfo.objects.create(**target)



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
        data.pop('key')
        target = models.RecruitmentInfo.objects.filter(id=data['id'])
        target.update(**data)
        res = {'infoList': '11111'}
        return JsonResponse(res, safe=False)


def update_project_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        data.pop('key')
        target = models.ProjectInfo.objects.filter(id=data['id'])
        target.update(**data)
        res = {'infoList': '11111'}
        return JsonResponse(res, safe=False)


def update_project_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        data.pop('key')
        data.pop('project_satisfaction')
        data.pop('project_num_all')
        data.pop('mouthly_target_reach')
        target = models.ProjectStatusInfo.objects.filter(id=data['id'])
        target.update(**data)
        res = {'infoList': '11111'}
        return JsonResponse(res, safe=False)

# Anaconda
# export PATH=$PATH:/home/fg/anaconda3/bin


# uwsgi –http :8000 chdir /home/fg/fgBlog/fgBlog –module django_wsgi
