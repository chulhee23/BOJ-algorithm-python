import sys


# repeat = int(input())

# 1회에 대한 알고리즘
col = int(sys.stdin.readline())
sticker = []

for i in range(2):
    sticker.append(list(map(int, input().split())))
    sticker[i].insert(0,0)
    sticker[i].insert(0,0)

print(sticker)
dp=[[0]*(col+2) for i in range(2)]

for i in range(2,col+2):
    dp[0][i]=max(dp[1][i-1],dp[1][i-2]) + sticker[0][i]
    dp[1][i]=max(dp[0][i-1],dp[0][i-2]) + sticker[1][i]

print(max(dp[0][col+1],dp[1][col+1]))