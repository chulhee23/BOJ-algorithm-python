import sys
input = sys.stdin.readline

dp=[1,1]

n=int(input())

for i in range(2,n+1):
    dp.append(dp[i-2]+dp[i-1])

print(dp[n]%10007)