import sys
n= int(sys.stdin.readline())

dp=[[0]*2 for i in range(n+1)]
dp[1][1]=1

for i in range(0,n+1):
    if (i<2):
        continue
    for j in range(2):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

print(sum(dp[n]))

