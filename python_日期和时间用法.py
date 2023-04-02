import time

a = time.time()
print('返回自Epoch以外经过的秒数：',a)
a = time.localtime()
print('返回自Epoch以外以时间格式返回：',a)
a = time.ctime()
print('返回当前时间：',a)
a =time.localtime()
a = time.strftime("%Y/%m/%d %H:%M:%S",a)
print('返回当前时间：',a)

import datetime
time = datetime.datetime.today()
print('返回当前时间：',time)
time = datetime.date(2019,1,1)
print('返回当前时间：',time)