
l = []
for i in range(int(input())):
    temp= int(input())
    l.append(temp)

dp = [0,1,2,4]

m = max(l)

for i in range(m-3):
    dp.append(dp[-1]+dp[-2]+dp[-3])

for i in l:
    print(dp[i])

# 뒤에 항들을 더해나갈 땐, arr[-1]+arr[-2]와 같은 형태가 훨씬 빠르게 접근한다.