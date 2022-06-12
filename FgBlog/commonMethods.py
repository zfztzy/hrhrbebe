import datetime
from hr_manage_db import models
from django.forms.models import model_to_dict
from dateutil.relativedelta import relativedelta


def projectStatusMonthly():
    date = str(datetime.date.today() + relativedelta(months=1))
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
        print(newDict)
        models.ProjectStatusInfo.objects.create(**newDict)


def selectDepartment(department, date):
    if date:
        target = models.ProjectStatusInfo.objects.values('pdu').filter(department=department, date=date).distinct()
    else:
        target = models.ProjectStatusInfo.objects.values('pdu').filter(department=department).distinct()
    pduList = []
    for i in target:
        pduList.append(i['pdu'])
    print(department)
    return pduList


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



def get_status_object(date):
    target = models.ProjectStatusInfo.objects.filter(date=date)
    pduList = models.ProjectStatusInfo.objects.values('pdu').distinct()
    pduTotal = {}
    pduReach = {}
    pduTarget = {}
    print(pduList)
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


def get_final_pic_value(date):
    if not date:
        return {'msg': '没选择日期'}
    pduList = selectDepartment('海思半导体', date)
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
                series3.append(pduValueList[1][i]/pduValueList[2][i]*100)
            except Exception as e:
                series3.append(0)
                print(str(e))
        except:
            print(f'当前日期没有pdu:{i}')
    pduList = selectDepartment('上海海思', date)
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
                series6.append(pduValueList[1][i]/pduValueList[2][i]*100)
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
            xData3.append(key)
            series7.append(regionValueList[0][key])
            series8.append(regionValueList[1][key])
            # series9.append(regionValueList[1][key]/regionValueList[2][key] if pduValueList[2][key] != 0 else 0)
            try:
                series9.append(regionValueList[1][key]/regionValueList[2][key]*100)
            except Exception as e:
                series9.append(0)
                print(str(e))
        except Exception as e:
            print(str(e))
    for key in regionValueList[3]:
        try:
            xData4.append(key)
            series10.append(regionValueList[3][key])
            series11.append(regionValueList[4][key])
            # series12.append(regionValueList[4][key]/regionValueList[5][key] if pduValueList[2][key] != 0 else 0)
            try:
                series12.append(regionValueList[1][key]/regionValueList[2][key]*100)
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


def selectPicData1(region, pdu, recommender, date):
    filterData = {}
    filterData1 = {}
    filterData2 = {}
    filterData3 = {}
    if region:
        filterData['region'] = region
    if pdu:
        filterData['pdu'] = pdu
    if recommender:
        filterData['recommender'] = recommender
    if date:
        filterData1['recommend_time__range'] = date
        filterData2['final_time__range'] = date
        filterData3['giveup_time__range'] = date
    target = models.ApplicantInfo.objects.all().filter(**filterData)
    target1 = models.ApplicantInfo.objects.all().filter(**filterData)
    target2 = models.ApplicantInfo.objects.all().filter(**filterData)
    target3 = models.ApplicantInfo.objects.all().filter(**filterData)
    List1 = []
    List2 = []
    List3 = []
    List4 = []
    for i in target:
        if i.process_status and i.resume_status:
            # print(i.name)
            if i.resume_status == 'open':
                if i.process_status == 'created':
                    pass
                else:
                    msg = '流程中'
                    List2.append(i.name)
            else:
                msg = ''
                if i.process_status == 'fellow':
                    pass
                else:
                    pass
            # print(f'状态-{msg}')
        else:
            print('数据错误')
    for i in target1:
        if i.process_status and i.resume_status:
            msg = '创建'
            List1.append(i.name)
        else:
            print('数据错误')
    for i in target2:
        if i.process_status and i.resume_status:
            # print(i.name)
            if i.resume_status == 'open':
                if i.process_status == 'created':
                    pass
                else:
                    pass
            else:
                msg = ''
                if i.process_status == 'fellow':
                    msg = '已入职'
                    List3.append(i.name)
                else:
                    pass
            # print(f'状态-{msg}')
        else:
            print('数据错误')
    for i in target3:
        if i.process_status and i.resume_status:
            # print(i.name)
            if i.resume_status == 'open':
                if i.process_status == 'created':
                    pass
                else:
                    pass
            else:
                msg = ''
                if i.process_status == 'fellow':
                    pass
                else:
                    msg = '淘汰'
                    List4.append(i.name)
            # print(f'状态-{msg}')
        else:
            print('数据错误')
    # a = {
    #     '创建': List1,
    #     '流程中': List2,
    #     '已入职': List3,
    #     '淘汰': List4,
    # }
    a = {
        '创建': len(List1),
        '流程中': len(List2),
        '已入职': len(List3),
        '淘汰': len(List4),
    }
    # print('创建', List1)
    # print('流程中', List2)
    # print('已入职', List3)
    # print('淘汰', List4)
    return a




def getPicData2(req):
    nameList = []
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    chartType = req['chartType']
    date = req['date']
    if chartType == 'pdu':
        department = req['department']
        pduList = selectDepartment(department, None)
        for i in pduList:
            a = selectPicData1(None, i, None, date)
            nameList.append(i)
            x1.append(a['创建'])
            x2.append(a['流程中'])
            x3.append(a['已入职'])
            x4.append(a['淘汰'])
    elif chartType == '招聘顾问':
        region = req['region']
        recommenderList = models.ApplicantInfo.objects.values('recommender').filter(region=region).distinct()
        for i in recommenderList:
            recommender = i['recommender']
            a = selectPicData1(region, None, recommender, date)
            nameList.append(recommender)
            x1.append(a['创建'])
            x2.append(a['流程中'])
            x3.append(a['已入职'])
            x4.append(a['淘汰'])
    elif chartType == '地域':
        regionList = models.ApplicantInfo.objects.values('region').distinct()
        print(regionList)
        for i in regionList:
            region = i['region']
            a = selectPicData1(region, None, None, date)
            nameList.append(region)
            x1.append(a['创建'])
            x2.append(a['流程中'])
            x3.append(a['已入职'])
            x4.append(a['淘汰'])
    res = {
        'xName': nameList,
        'x1': x1,
        'x2': x2,
        'x3': x3,
        'x4': x4,
    }
    return res


