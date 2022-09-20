
class Solution:
    def get_max_profit(input1,input2,input3):
        money = input1
#         盈利的价格=卖出-买入
#         如果只能买卖一次，取最大差值
        profit = 0
        input3=input3.split(',')
        print("三天价格：",input3)
        print(len(input3))
        for i in range(len(input3)):
            for j in range(i+1,len(input3)):
                profit = max(profit,int(input3[j])-int(input3[i]))
                print(profit)
        return profit

        # for i in range():
        #     i = int(i)
        #     length = len(input3)
        #     if i in range(length):
        #         if input3[i]<input3[i+1]:
        #             print(i)






if __name__=='__main__':
    # 输入金额，天数，价格
    input1='1000'
    input2='3'
    input3='1,2,1'
    a = Solution.get_max_profit(input1,input2,input3)
    print('最终获利：',a)


