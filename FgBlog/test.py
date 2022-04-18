import os

if __name__ == '__main__':
# 加载Django项目的配置信息
# 看起来有点长, 不过此命令可以在项目的 manage.py 的第 7 行直接拿来用
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FgBlog.settings')
    # 导入Django，并启动Django项目
    import django

    django.setup()

# 然后就可以直接通过此py文件进行调试了
from hr_manage_db import models
import pymysql
import xlsxwriter
import xlwt
import datetime
import time
import datetime
from django.forms.models import model_to_dict



def newDownloadExcel(excelType):
    if excelType == 'ApplicantInfo':
        dbTarget = models.ApplicantInfo
        target = models.ApplicantInfo
        excelTypeName = '候选人管理'
    if excelType == 'ProjectInfo':
        dbTarget = models.ProjectInfo
        target = models.ProjectInfo
        excelTypeName = '招聘需求'
    if excelType == 'ProjectStatusInfo':
        dbTarget = models.ProjectStatusInfo
        target = models.ProjectStatusInfo
        excelTypeName = '项目满足度'
    if excelType == 'RecruitmentInfo':
        dbTarget = models.RecruitmentInfo
        target = models.RecruitmentInfo
        excelTypeName = '招聘看板'
    try:
        dbTarget = dbTarget._meta.get_fields()
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        keyList = []
        for i in range(len(dbTarget)):
            query = dbTarget[i]
            name = query.name
            keyList.append(name)
            sheet.write(0, i, name)
        target = target.objects.all()
        for i in range(len(target)):
            targetI = model_to_dict(target[i])
            for j in range(len(keyList)):
                value = keyList[j]
                value = targetI[value]
                sheet.write(i + 1, j, str(value))
        now = str(datetime.datetime.now()).split(".")[0]
        wbk.save(f'./dist/static/downloadFile/{now}-{excelTypeName}.xlsx')
    except Exception as e:
        print(str(e))
        print('error', excelType)


def applicant_according_to_recruitment(recruitmentId):
    info = {}
    totalTarget = models.ApplicantInfo.objects.all().filter(related=recruitmentId)
    print(totalTarget)
    total =len(totalTarget)
    fail = len(totalTarget.filter(process_status__icontains='fail')) if totalTarget.filter(process_status__icontains='fail') else 0
    print(fail)
    done = len(totalTarget.filter(process_status__icontains='fellow')) if totalTarget.filter(process_status__icontains='fellow') else 0
    print(done)
    giveUp = len(totalTarget.filter(process_status__icontains='giveUp')) if totalTarget.filter(process_status__icontains='giveUp') else 0
    print(giveUp)
    discuss = len(totalTarget.filter(process_status__icontains='discuss')) if totalTarget.filter(process_status__icontains='discuss') else 0
    print(discuss)
    standBy = len(totalTarget.filter(process_status__icontains='standBy')) if totalTarget.filter(process_status__icontains='standBy') else 0
    print(standBy)
    created = len(totalTarget.filter(process_status__icontains='created')) if totalTarget.filter(process_status__icontains='created') else 0
    print(created)
    filtering = len(totalTarget.filter(process_status__icontains='pass')) if totalTarget.filter(process_status__icontains='pass') else 0
    print(filtering)
    info['total'] = total
    info['done'] = done
    info['filtering'] = filtering + created + standBy + discuss
    info['fail'] = fail
    info['giveUp'] = giveUp
    return info


def projectStatusMonthly():
    date = str(datetime.date.today())
    print(date)
    # date = '2022-04-04'
    if date[-2:] != '04':
        print(date[-2:])
        return
    date = date.replace('-', '')
    yearMonth = date[:6]
    oldYearMonth = date[:4] + str(int(date[4:6]) - 1) if int(date[4:6]) != 1 else str(int(date[:4])-1) + '12'
    oldYearMonth = oldYearMonth[:4] + '0' + oldYearMonth[-1] if len(oldYearMonth) == 5 else oldYearMonth
    print(str(date).replace('-', '')[:6])
    print(yearMonth)
    print(oldYearMonth)
    target = models.ProjectStatusInfo.objects.filter(date=oldYearMonth)
    for i in target:
        i = model_to_dict(i)
        print(i)
        newDict = i.copy()
        newDict.pop('key')
        newDict['date'] = yearMonth
        newDict['sow_num'] = '0'
        newDict['project_num'] = '0'
        newDict['new_project_num'] = '0'
        newDict['offset_num'] = '0'
        newDict['monthly_target'] = '0'
        newDict['monthly_reach'] = '0'
        print(newDict)
        models.ProjectStatusInfo.objects.create(**newDict)


if __name__ == '__main__':
    projectStatusMonthly()