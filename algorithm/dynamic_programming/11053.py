# 가장 긴 부분 수열 찾기 문제
# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.


# 전체를 다시 탐색해도 상관 없음 어차피 n^2
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [0]*n
for i in range(0, n):
    if i == 0:
        d[i] = 1
    else:
        m = 0
        for j in range(i):
            if (arr[j] < arr[i]) and (m < d[j]):
                m = d[j]
        d[i] = m + 1
print(max(d))