
search_buf_pos = 0
class Solution:
    def __init__(self, inputStr):
        self.inputStr = inputStr  # 输入流
        self.searchSize = 3  # 搜索缓冲区(已编码区)大小
        self.aheadSize = 3  # lookAhead缓冲区（待编码区）大小
        self.windSpiltIndex = 0  # lookHead缓冲区开始的索引
        self.move = 0
        self.notFind = -1  # 没有找到匹配字符串

    #判断lookHead缓冲区是否为空
    def isLookHeadEmpty(self):
        return True if self.windSpiltIndex + self.move+1 > len(self.inputStr)-1   else False

    def encoding(self):
        step = 0
        print("Step   Position   Match   Output")
        # 判断待编码区是否为空，若不是，则开始编码
        while not self.isLookHeadEmpty():
            # 1.滑动窗口
            self.windSpiltIndex = self.windSpiltIndex + self.move
            # 2. 得到最大匹配串的偏移值和长度
            (offset, matchLen) = self.findMaxMatch()
            # 3.设置窗口下一步需要滑动的距离
            if matchLen ==0:
                self.move = 1
            else:
                self.move = matchLen

            if matchLen == 0:
                if self.windSpiltIndex+1<len(self.inputStr):
                    # 匹配为0，说明无字符串匹配，输出下一个需要编码的字母
                    nextChar = self.inputStr[self.windSpiltIndex]
                    result = (step, self.windSpiltIndex, '-', '(0,0,' + nextChar +')')
            else:
                # 如果有匹配到字符，则继续往下匹配
                if self.windSpiltIndex+1<len(self.inputStr):
                    nextChar = self.inputStr[self.windSpiltIndex+1]
                    result = (step, self.windSpiltIndex,
                          self.inputStr[self.windSpiltIndex - offset: self.windSpiltIndex - offset + matchLen],
                          '(' + str(offset) + ',' + str(matchLen) +','+nextChar +')')
            # 4.输出结果
            # self.output(result)
            print("%d      %d           %s     %s" % result)
            step = step + 1  # 仅用来设置第几步

    def findMaxMatch(self):
        matchLen = 0
        offset = 0
        # 编码区右边界
        getWinEndIndex = self.windSpiltIndex + self.aheadSize
        if len(self.inputStr)-1<getWinEndIndex:
            minEdge = len(self.inputStr)-1
        else:
            minEdge = getWinEndIndex + 1

        # minEdge = self.minEdge() + 1  # 得到编码区域的右边界
        # 遍历待编码区，寻找最大匹配串
        for i in range(self.windSpiltIndex + 1, minEdge+1):
            # print("i: %d" %i)
            offsetTemp = self.searchBufferOffest(i)
            if offsetTemp == self.notFind:
                return (offset, matchLen)
            offset = offsetTemp  # 偏移值

            matchLen = matchLen + 1  # 每找到一个匹配串，加1

        return (offset, matchLen)

    def searchBufferOffest(self, i):
        searchStart = self.windSpiltIndex - self.searchSize
        searchEnd = self.windSpiltIndex
        # 下面几个if是处理开始时的特殊情况
        if searchEnd < 1:
            return self.notFind
        if searchStart < 0:
            searchStart = 0
            if searchEnd == 0:
                searchEnd = 1
        searchStr = self.inputStr[searchStart: searchEnd]  # 搜索区字符串
        # searchStr字符串查找待搜索字符串，并返回初始索引
        findIndex = searchStr.find(self.inputStr[self.windSpiltIndex: i])
        if findIndex == -1:
            return -1
        return len(searchStr) - findIndex





if __name__ == '__main__':
    lz77 = Solution("ABCBCBCBCA")
    lz77.encoding()

