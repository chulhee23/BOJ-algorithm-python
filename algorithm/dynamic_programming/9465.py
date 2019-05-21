import sys
input = sys.stdin.readline

repeat = int(input())

# 1회에 대한 알고리즘
col = map(int, input().split())
sticker = []

for _ in range(col):
    sticker.append(list(map(int, input().split())))

sticker[0].insert(0,0)
sticker[1].insert(0,0)
dp=[[0]*(col+1) for i in range(2)]

for i in range(2,col+1):
    dp[0][i]=max(dp[1][i-1],dp[1][i-2]) + sticker[0][i]
    dp[1][i]=max(dp[0][i-1],dp[0][i-2]) + sticker[1][i]

