# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
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