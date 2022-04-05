
import paramiko
import datetime

fileType = 'test'
# workBook1 = xlsxwriter.Workbook(f'../downloadFile/{datetime.date.today()}-{fileType}.xlsx')


def checkDownloadFile():
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
        fileList.append({'path': 'static/downloadFile/' + filename, 'name': filename})
    for i in fileList:
        print(i)




if __name__ == '__main__':
    print(datetime.datetime.now())