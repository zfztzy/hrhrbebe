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
        newDict['sow_num'] = '0'
        newDict['project_num'] = '0'
        newDict['new_project_num'] = '0'
        newDict['offset_num'] = '0'
        newDict['monthly_target'] = '0'
        newDict['monthly_reach'] = '0'
        print(newDict)
        models.ProjectStatusInfo.objects.create(**newDict)