from typing import List

import functools
class Solution:

    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        def compare_fn(i: int, j: int) -> int:
            if growTime[i] > growTime[j]:
                return -1
            if growTime[i] < growTime[j]:
                return 1
            return 0

        n = len(plantTime)
        idx = list(range(n))
        print(idx)
        idx.sort(key=functools.cmp_to_key(compare_fn))
        print(idx)
        prev = ans = 0

        for i in idx:
            print(ans, prev, plantTime[i], growTime[i])
            ans = max(ans,prev+plantTime[i]+growTime[i])
            prev+=plantTime[i]

        return ans
if __name__ == '__main__':
    plantTime =[3, 5, 2, 7]
    growTime = [26, 9, 14, 17, 6, 14, 23, 24, 11, 6, 27, 14, 13, 1, 15, 5, 12, 15, 23, 27, 28, 12]
    # aa = Solution()
    # bb = aa.earliestFullBloom(plantTime=plantTime,growTime=growTime)
    # print(bb)
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    num1 = 0
    j = 1
    for i in l1:
        num1 += j * i
        j = j * 10
    print(num1)
    num2 = 0
    j = 1
    for i in l2:
        num2 += j * i
        j = j * 10
    print(num2)
    num = num1 + num2
    print(num)
    l3 = []
    while num != 0:
        a = num % 10
        num = num//10
        l3.append(str(a))
    print(l3)