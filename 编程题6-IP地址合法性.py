# -*- coding:utf-8 -*-


def ip4_check(ip):
    ip_4 = ip.strip().split(".")   # 去掉前后空格，按.切割IP地址为一个列表
    print(ip_4)
    if len(ip_4) == 4:  # 判断IP是否为4位数
        for i in range(4):
            # 判断IP是否为0-255的整数
            if ip_4[i].isdigit() and ip_4[i] == str(int(ip_4[i])) and 0 <= int(ip_4[i]) <= 255:
                continue
            else:
                print('IP4地址必须由0-255的整数组成')
                return
        print('{}是合法的IP4地址'.format(ip))
    else:
        print("IP4地址应该由4个字节组成，以'.'分割!")

def ip6_check(ip):
    ip_6 = ip.strip().split(":")   # 去掉前后空格，按.切割IP地址为一个列表
    # 字符是数据或字母
    str = '0123456789abcdefABCDEF'
    if len(ip_6) == 8:  # 判断IP是否为8位数
        for i in range(8):
            if 1<=len(ip_6[i])<=4 :
                for c in ip_6[i]:
                    if c in str:
                        continue
                    else:
                        print('IP6地址必须由十六进制数组成',c)
                        return
            else:
                print('IP6地址每段不能超过4位')
                return
        print('{}是合法的IP6地址'.format(ip))
    else:
        print("IP4地址应该由8个字节组成，以':'分割!")



if __name__ =='__main__':
    ip = '2001:2121:adc:2121:0:0:FF:aa'
    if '.' in ip:
        ip4_check(ip)
    else:
        ip6_check(ip)




