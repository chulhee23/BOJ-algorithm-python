# 문제
# 2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.



# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

import sys
input = sys.stdin.readline

dp=[1,1]

n=int(input())

for i in range(2,n+1):
    dp.append(dp[i-2]*2+dp[i-1])

print(dp[n]%10007)
