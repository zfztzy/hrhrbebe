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


def selectPicData1(region, pdu, recommender):
    # target = models.ApplicantInfo.objects.all()
    filterData = {}
    if region:
        filterData['region'] = region
    if pdu:
        filterData['pdu'] = pdu
    if recommender:
        filterData['recommender'] = recommender
    target = models.ApplicantInfo.objects.all().filter(**filterData)
    List1 = []
    List2 = []
    List3 = []
    List4 = []
    for i in target:
        if i.process_status and i.resume_status:
            # print(i.name)
            if i.resume_status == 'open':
                if i.process_status == 'created':
                    msg = '创建'
                    List1.append(i.name)
                else:
                    msg = '流程中'
                    List2.append(i.name)
            else:
                msg = ''
                if i.process_status == 'fellow':
                    msg = '已入职'
                    List3.append(i.name)
                else:
                    msg = '淘汰'
                    List4.append(i.name)
            # print(f'状态-{msg}')
        else:
            print('数据错误')
    a = {
        '创建': List1,
        '流程中': List2,
        '已入职': List3,
        '淘汰': List4,
    }
    # print('创建', List1)
    # print('流程中', List2)
    # print('已入职', List3)
    # print('淘汰', List4)
    return a


def selectDepartment(department):
    target = models.PduInfo.objects.filter(department=department)
    pduList = []
    for i in target:
        pduList.append(i.pdu)
    print(department)
    return pduList


def getPicData2(department):
    pduList = selectDepartment(department)
    print(pduList)
    picDataList = []
    for i in pduList:
        region = None
        recommender = None
        pdu = i
        print(i)
        a = {'y': selectPicData1(region, pdu, recommender), 'x': i}
        picDataList.append(a)
        print(a)

    print(datetime.datetime.now())
    print(picDataList)


def get_status_object(date):
    target = models.ProjectStatusInfo.objects.filter(date=date)
    pduList = models.ProjectStatusInfo.objects.values('pdu').distinct()
    pduTotal = {}
    pduReach = {}
    pduTarget = {}
    for pdu in pduList:
        pdu = pdu['pdu']
        for i in target:
            if i.pdu == pdu:
                try:
                    pduTotal[pdu] += int(i.new_project_num)
                except:
                    pduTotal[pdu] = int(i.new_project_num)
                try:
                    pduTotal[pdu] += int(i.offset_num)
                except:
                    pduTotal[pdu] = int(i.offset_num)
                try:
                    pduReach[pdu] += int(i.monthly_reach)
                except:
                    pduReach[pdu] = int(i.monthly_reach)
                try:
                    pduTarget[pdu] += int(i.monthly_target)
                except:
                    pduTarget[pdu] = int(i.monthly_target)
    return pduTotal, pduReach, pduTarget


def get_status_object2(date):
    target = models.ProjectStatusInfo.objects.filter(date=date)
    regionList = models.ProjectStatusInfo.objects.values('region').distinct()
    departmentList1Total = {}
    departmentList1Reach = {}
    departmentList1Target = {}
    departmentList2Total = {}
    departmentList2Reach = {}
    departmentList2Target = {}
    for region in regionList:
        region = region['region']
        for i in target:
            if i.region == region and i.department == '海思半导体':
                try:
                    departmentList1Total[region] += int(i.new_project_num)
                except:
                    departmentList1Total[region] = int(i.new_project_num)
                try:
                    departmentList1Total[region] += int(i.offset_num)
                except:
                    departmentList1Total[region] = int(i.offset_num)
                try:
                    departmentList1Reach[region] += int(i.monthly_reach)
                except:
                    departmentList1Reach[region] = int(i.monthly_reach)
                try:
                    departmentList1Target[region] += int(i.monthly_target)
                except:
                    departmentList1Target[region] = int(i.monthly_target)
            elif i.region == region and i.department == '上海海思':
                try:
                    departmentList2Total[region] += int(i.new_project_num)
                except:
                    departmentList2Total[region] = int(i.new_project_num)
                try:
                    departmentList2Total[region] += int(i.offset_num)
                except:
                    departmentList2Total[region] = int(i.offset_num)
                try:
                    departmentList2Reach[region] += int(i.monthly_reach)
                except:
                    departmentList2Reach[region] = int(i.monthly_reach)
                try:
                    departmentList2Target[region] += int(i.monthly_target)
                except:
                    departmentList2Target[region] = int(i.monthly_target)
    return departmentList1Total, departmentList1Reach, departmentList1Target, departmentList2Total, departmentList2Reach, departmentList2Target


def get_final_pic_value(date):
    pduList = selectDepartment('海思半导体')
    pduValueList = get_status_object(date)
    xData1 = []
    series1 = []
    series2 = []
    series3 = []
    for i in pduList:
        try:
            xData1.append(i)
            series1.append(pduValueList[0][i])
            series2.append(pduValueList[1][i])
            # series3.append(pduValueList[1][i]/pduValueList[2][i] if pduValueList[2][i] != 0 else 0)
            try:
                series3.append(pduValueList[1][i]/pduValueList[2][i])
            except Exception as e:
                series3.append(0)
                print(str(e))
        except:
            print(f'当前日期没有pdu:{i}')
    pduList = selectDepartment('上海海思')
    # pduValueList = get_status_object(date)
    xData2 = []
    series4 = []
    series5 = []
    series6 = []
    for i in pduList:
        try:
            xData2.append(i)
            series4.append(pduValueList[0][i])
            series5.append(pduValueList[1][i])
            # series3.append(pduValueList[1][i]/pduValueList[2][i] if pduValueList[2][i] != 0 else 0)
            try:
                series6.append(pduValueList[1][i]/pduValueList[2][i])
            except Exception as e:
                series6.append(0)
                print(str(e))
        except:
            print(f'当前日期没有pdu:{i}')
    regionValueList = get_status_object2(date)
    xData3 = []
    series7 = []
    series8 = []
    series9 = []
    xData4 = []
    series10 = []
    series11 = []
    series12 = []
    for key in regionValueList[0]:
        try:
            xData3.append(key + ' / 海思半导体')
            series7.append(regionValueList[0][key])
            series8.append(regionValueList[1][key])
            # series9.append(regionValueList[1][key]/regionValueList[2][key] if pduValueList[2][key] != 0 else 0)
            try:
                series9.append(regionValueList[1][key]/regionValueList[2][key])
            except Exception as e:
                series9.append(0)
                print(str(e))
        except Exception as e:
            print(str(e))
    for key in regionValueList[3]:
        try:
            xData4.append(key + ' / 上海海思')
            series10.append(regionValueList[3][key])
            series11.append(regionValueList[4][key])
            # series12.append(regionValueList[4][key]/regionValueList[5][key] if pduValueList[2][key] != 0 else 0)
            try:
                series12.append(regionValueList[1][key]/regionValueList[2][key])
            except Exception as e:
                series12.append(0)
                print(str(e))
        except Exception as e:
            print(str(e))
    # print('###############\n###############')
    # print(xData1)
    # print(series1)
    # print(series2)
    # print(series3)
    # print(xData2)
    # print(series4)
    # print(series5)
    # print(series6)
    # print(xData3)
    # print(series7)
    # print(series8)
    # print(series9)
    # print(xData4)
    # print(series10)
    # print(series11)
    # print(series12)
    res = {
        '海思半导体pduXData': xData1,
        '海思半导体pdu剩余需求数': series1,
        '海思半导体pdu月度满足数': series2,
        '海思半导体pdu月度满足度': series3,
        '上海海思pduXData': xData2,
        '上海海思pdu剩余需求数': series4,
        '上海海思pdu月度满足数': series5,
        '上海海思pdu月度满足度': series6,
        '海思半导体地域xData': xData3,
        '海思半导体地域剩余需求数': series7,
        '海思半导体地域月度满足数': series8,
        '海思半导体地域月度满足度': series9,
        '上海海思地域xData': xData4,
        '上海海思地域剩余需求数': series10,
        '上海海思地域月度满足数': series11,
        '上海海思地域月度满足度': series12,
    }
    return res


if __name__ == '__main__':
    regionList = models.ProjectStatusInfo.objects.values('region').distinct()



