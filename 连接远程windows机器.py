import winrm
import paramiko
import os

shell = r"F:\dmp\output.bat"
s = winrm.Session('10.20.25.166',auth=('administrator','ERTzxc@#$123'),transport='ntlm')
r = s.run_cmd(shell)
resbonse = r.std_out
print(resbonse)
print(r.std_err)

# def win_scp(ip,filepath):
#     try:
#         pass
#         ts = paramiko.transport(ip,22)
#         ts.connect(username='administrator',passwoed='ERTzxc@#$123')
#         sftp = paramiko.SFTPClient.from_transport(ts)
#         print('开始放文件')
#         sftp.put(localpath=filepath,remotepath=r'F:\aaa')
#         ts.close()
#     except Exception as e:
#         return {'error'}
#
# if __name__ == '__main__':
#     a = win_scp(ip='10.20.25.166',filepath=r'D:\PycharmProjects\pythonProject\main.py')
#     print(a)