import pymysql
import xlsxwriter
import xlwt
import datetime
import time
import datetime
from hr_manage_db import models
from django.forms.models import model_to_dict
import paramiko

fileType = 'test'
# workBook1 = xlsxwriter.Workbook(f'../downloadFile/{datetime.date.today()}-{fileType}.xlsx')




def getFileList(excelType):
    if excelType == 'ApplicantInfo':
        excelTypeName = '候选人管理'
    if excelType == 'ProjectInfo':
        excelTypeName = '项目信息'
    if excelType == 'ProjectStatusInfo':
        excelTypeName = '项目满足度'
    if excelType == 'RecruitmentInfo':
        excelTypeName = '招聘需求'
    # 获取transport传输实例, sftp服务器 ip + 端口号
    tran = paramiko.Transport(('139.9.160.24', 22))
    # 连接ssh服务器, user + password
    tran.connect(username='root', password='lunchFeng@07177')
    # 获取sftp实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    path = '/tmp/hr_manage/FgBlog/dist/static/downloadFile/'
    filesAttr = sftp.listdir_attr(path)
    filesAttr.sort(key=lambda f: f.filename)
    filesAttr = filesAttr[::-1]
    fileList = []
    for fileAttr in filesAttr:
        filename = fileAttr.filename
        print(fileAttr.longname)
        if excelType in filename or excelTypeName in filename:
            fileList.append({'path': 'static/downloadFile/' + filename, 'name': filename})
    return fileList


def newDownloadExcel(excelType):
    if excelType == 'ApplicantInfo':
        dbTarget = models.ApplicantInfo
        target = models.ApplicantInfo
        excelTypeName = '候选人管理'
    if excelType == 'ProjectInfo':
        dbTarget = models.ProjectInfo
        target = models.ProjectInfo
        excelTypeName = '项目信息'
    if excelType == 'ProjectStatusInfo':
        dbTarget = models.ProjectStatusInfo
        target = models.ProjectStatusInfo
        excelTypeName = '项目满足度'
    if excelType == 'RecruitmentInfo':
        dbTarget = models.RecruitmentInfo
        target = models.RecruitmentInfo
        excelTypeName = '招聘需求'
    try:
        dbTarget = dbTarget._meta.get_fields()
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        keyList = []
        for i in range(len(dbTarget)):
            query = dbTarget[i]
            name = query.name
            print(query.name)
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
        filename = f'{now}-{excelTypeName}.xlsx'
        wbk.save(f'FgBlog/dist/static/downloadFile/{filename}')
        return {'path': 'static/downloadFile/' + filename, 'name': filename}
    except Exception as e:
        print(str(e))
        print('error', excelType)
