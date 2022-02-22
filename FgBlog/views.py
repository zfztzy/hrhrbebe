from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from FgBlog.paragraph.About import About
from FgBlog.paragraph.studyInfo import StudyInfo
from FgBlog.componentsApi.componentsApi import CompontentsApi
import time
from pyquery import PyQuery as pq
from hr_manage_db import models
import json



def realHome(request):
    return render(request, 'index.html')


def getParagraphDetail(request):
    if request.method == 'POST':
        a = About()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        pid = eval(request.body.decode()).get('pid')
        print(type(pid))
        print(pid)
        # pid = pid['pid']
        pp = a.getParagraph(pid)
        ii = a.getInfo(pid)
        rsp = {
            'code': 0,
            'msg': 'success',
            'paragraph': pp,
            'Info': ii,
            **ii
        }
        return JsonResponse(rsp)


def studyInfo2(request):
    if request.method == 'POST':
        index = request.GET.get('data')
        print(type(index))
        print(index)
        # rsp = a.getStudyInfo(index)
        return JsonResponse(index, safe=False)


def get_applicant_info(request):
    if request.method == 'POST':
        target = models.ApplicantInfo.objects.all()
        applicantList = []
        for i in range(len(target)):
            ii = i
            i = target[i]
            applicant = {
                'key': ii,
                'id': i.id,
                'name': i.name,
                'phone_num': i.phone_num,
                'graduated_from': i.graduated_from,
                'education': i.education,
                'major': i.major,
                'working_seniority': i.working_seniority,
                'job': i.job,
                'region': i.region,
                'related': i.related,
                'arrival_time': i.arrival_time,
                'recommender': i.recommender,
                'recommend_time': i.recommend_time,
                'own_interviewer': i.own_interviewer,
                'own_interview_results': i.own_interview_results,
                'reason1': i.reason1,
                'own_interview_time': i.own_interview_time,
                'machine_test_type': i.machine_test_type,
                'machine_test_score': i.machine_test_score,
                'machine_test_time': i.machine_test_time,
                'hw_interviewer1': i.hw_interviewer1,
                'hw_interview_results1': i.hw_interview_results1,
                'reason2': i.reason2,
                'hw_interview_time1': i.hw_interview_time1,
                'hw_interviewer2': i.hw_interviewer2,
                'hw_interview_results2': i.hw_interview_results2,
                'reason3': i.reason3,
                'hw_interview_time2': i.hw_interview_time2,
                'final_result': i.final_result,
                'final_time': i.final_time,
                'reason4': i.reason4,
            }
            print(i.id)
            applicantList.append(applicant)
        data = {'applicantList': applicantList}
        return JsonResponse(data, safe=False)


def get_recruitment_info(request):
    if request.method == 'POST':
        target = models.RecruitmentInfo.objects.all()
        infoList = []
        for i in range(len(target)):
            ii = i
            i = target[i]
            info = {
                'key': ii,
                'id': i.id,
                'internal_id': i.internal_id,
                'department': i.department,
                'pdu': i.pdu,
                'project': i.project,
                'position_attribute': i.position_attribute,
                'skill_keyword': i.skill_keyword,
                'requirements': i.requirements,
                'working_seniority': i.working_seniority,
                'proposed_time': i.proposed_time,
                'proposer': i.proposer,
                'arrival_time': i.arrival_time,
                'num': i.num,
                'recruiter': i.recruiter,
                'project_leader': i.project_leader,
                'region': i.region,
                'location': i.location,
                'urgency': i.urgency,
                'type': i.type,
                'interviewer': i.interviewer,
                'synthetical_interviewer': i.synthetical_interviewer,
                'arrival_num': i.arrival_num,
                'status': i.status,
                'close_time': i.close_time,
                'remarks': i.remarks
            }
            print(i.id)
            infoList.append(info)
        data = {'infoList': infoList}
        return JsonResponse(data, safe=False)


def get_project_status_info(request):
    if request.method == 'POST':
        target = models.ProjectStatusInfo.objects.all()
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
            print(i.id)
            infoList.append(info)
        data = {'infoList': infoList}
        return JsonResponse(data, safe=False)


def get_project_info(request):
    if request.method == 'POST':
        target = models.ProjectInfo.objects.all()
        infoList = []
        for i in range(len(target)):
            ii = i
            i = target[i]
            info = {
                'key': ii,
                'id': i.id,
                'project_id': i.project_id,
                'department': i.department,
                'pdu': i.pdu,
                'business': i.business,
                'name': i.name,
                'region': i.region,
                'delivery_leader': i.delivery_leader,
                'pm': i.pm,
                'qa': i.qa,
                'hr': i.hr,
                'hwpm': i.hwpm
            }
            print(i.id)
            infoList.append(info)
        data = {'infoList': infoList}
        return JsonResponse(data, safe=False)


def update_applicant_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data = data.get('data')
        print(type(data))
        print(data)
        data.pop('key')
        target = models.ApplicantInfo.objects.filter(id=data['id'])
        target.update(**data)
        res = {'infoList': '11111'}
        return JsonResponse(res, safe=False)


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


def studyInfo(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        index = int(eval(request.body.decode()).get('sid'))
        print(type(index))
        print(index)
        rsp = a.getStudyInfo(index)
        return JsonResponse(rsp)


def studyType(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        sType = eval(request.body.decode()).get('sType')
        print(type(sType))
        print(sType)
        msg = a.getStudyType(sType)
        rsp = {
            'code': '0',
            'msg': msg
        }
        return JsonResponse(rsp)


def studyList(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        sType = eval(request.body.decode()).get('sType')
        print(type(sType))
        print(sType)
        slist = a.getStudyList(sType)
        rsp = {
            'code': '0',
            'slist': slist
        }
        return JsonResponse(rsp)



def getStudyTopInfo(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        sType = eval(request.body.decode()).get('type')
        print(type(sType))
        print(sType)
        sTopInfo = a.getStudyTopInfo(sType)
        rsp = {
            'code': '0',
            'topInfo': sTopInfo
        }
        return JsonResponse(rsp)


def getStudyMidInfo(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        sType = eval(request.body.decode()).get('type')
        print(type(sType))
        print(sType)
        sTopInfo = a.getStudyMidInfo(sType)
        rsp = {
            'code': '0',
            'midInfo': sTopInfo
        }
        return JsonResponse(rsp)


def getStudyBotInfo(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        sType = eval(request.body.decode()).get('type')
        print(type(sType))
        print(sType)
        sTopInfo = a.getStudyBotInfo(sType)
        rsp = {
            'code': '0',
            'botInfo': sTopInfo
        }
        return JsonResponse(rsp)


def getStudySwiper(request):
    if request.method == 'POST':
        a = StudyInfo()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        sType = eval(request.body.decode()).get('type')
        print(type(sType))
        print(sType)
        sTopInfo = a.getStudySwiper(sType)
        rsp = {
            'code': '0',
            'swipeInfo': sTopInfo
        }
        return JsonResponse(rsp)


def getNavbarList(request):
    if request.method == 'POST':
        a = CompontentsApi()
        print(request.headers)
        print(request.body)
        print(type(request.body))
        nType = eval(request.body.decode()).get('type')
        print(type(nType))
        print(nType)
        nList = a.getNavbarList(nType)
        rsp = {
            'code': '0',
            'navbarList': nList
        }
        return JsonResponse(rsp)


def getHtml(request):
    if request.method == 'POST':
        print(request.headers)
        print(request.body)
        print(type(request.body))
        url = eval(request.body.decode()).get('url')
        print(type(url))
        print(url)
        html = pq(url=url, encoding='utf-8')('body').html()
        print(html)
        rsp = {
            'code': '0',
            'html': html
        }
        return JsonResponse(rsp)


# Anaconda
# export PATH=$PATH:/home/fg/anaconda3/bin


# uwsgi –http :8000 chdir /home/fg/fgBlog/fgBlog –module django_wsgi
