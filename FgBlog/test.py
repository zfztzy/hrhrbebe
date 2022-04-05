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


if __name__ == '__main__':
    target = models.ApplicantInfo.objects.all()
    total = len(target)
    print(f'total:{total}')
    yearTarget = target.filter(recommend_time__year=2022, recommend_time__month=3)
    year2022Total = len(yearTarget)
    print(f'year2022Total:{year2022Total}')
    for i in yearTarget:
        print(i.recommend_time)