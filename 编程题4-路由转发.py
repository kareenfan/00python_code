
class Solution:
    def isMatch(s: str, p: str) :
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                print(i,j,'dp[i][j]',format(dp[i][j]))
        dp[0][0] = True
        # 如果匹配规则中首字符是*，则匹配True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        print(dp[1][0])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 如果j-1是*，怎么上一个字段无论何值都为true，
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]




if __name__ == '__main__':
    a =Solution.isMatch(s='abs', p='*s')
    print(a)