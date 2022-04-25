import datetime
from hr_manage_db import models
from django.forms.models import model_to_dict


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
        print(newDict)
        models.ProjectStatusInfo.objects.create(**newDict)


def selectDepartment(department, date):
    target = models.ProjectStatusInfo.objects.values('pdu').filter(department=department, date=date).distinct()
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

