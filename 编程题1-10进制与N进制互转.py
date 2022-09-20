#N进制转10进制
from array import array


class Solution:
    def BaseNToBase10(charnum, iBase):
        if (iBase>35 or iBase<2):
            print('输入的进制数需要在2-35之间')
            return
        # 如果输入的进制小于数据，则提示输入异常，
        product = 1
        deca = 0
        length = len(charnum)
        if iBase <= 10:
            for a in range(length):
                if ord(charnum[a])-48 >= iBase:
                    return '输入错误',charnum[a],iBase
        else:
            for a in range(length):
                if ord(charnum[a])>=65:
                    if ord(charnum[a])-65+10 >= iBase:
                        return '输入错误',charnum[a],iBase

        for a in range(length):
            i = length-a-1
            print('i的值，a的值',i,a)
            print('数据中的值，位数',charnum[i],a)
            ch = ord(charnum[i])-48
            print('ch的值',ch)
            if (ch in range(0,10)):
                print('当前值charnum',ch)
                ch = int(charnum[i])
                deca = deca + ch * product
                print('打印0-9对应值',deca)
            else:
                ch = ord(charnum[i])-65+10
                print(ch)
                print(charnum[i], i)
                deca = deca + ch * product

            print('i的值',i)
            print('当前值：', deca)
            product = product * iBase
            print(product)

        return deca

    def Base10ToBaseN(Intnum, iBase):
#         如果iBase大于35则提示异常
        if iBase>35 or iBase<2:
            return '输入的进制数异常，请重新输入'
        b = 1
        c = []
        while(b >= 1):
            a = Intnum % iBase   #余数
            b = int(Intnum / iBase)   #除数
            print('余数是：', a, '除数是：', b)
            Intnum = b
            # c.extend(a)
            if a >9 :
                a = chr(a+55)
                print(a)
            c.append(a)
            c.reverse()
            # for i in len(c):
            #     print('c的值是',c[i])
        print(c)
        arr1 = "".join('%s' %id for id in c)
        print('十进制数转Ibase进制数为',arr1)




if __name__ == '__main__':
    # a = Solution.BaseNToBase10('9B',11)
    a = Solution.Base10ToBaseN(0,1)
    print('最终结果',a)




