# <예시문제>
# 철수와 여자친구
# 오랜 기간의 교제 끝에, 철수는 여자친구에게 프로포즈하려고 한다. 그녀는 수학을 매우 잘한다. 그녀는 철수가 이 문제를 풀 때에만 프로포즈를 받아들일 것이다.
# 문제는 다음과 같다. 철수를 도와 문제를 풀게 해 주자. 두 수 N과 M이 주어진다. 1이 N번 연속된 수를 M으로 나눈 나머지는 얼마인가?
# ▶ 입력설명
# 첫번째 줄에는 테스트 케이스의 개수를 뜻하는 T가 주어진다. 이후 T줄에 각 줄마다 N과 M이 주어진다.
# ▶ 출력설명
# 총 T줄에, 각 줄마다 각 테스트 케이스의 정답을 출력하여라.
# ▶ 제한조건
# 1 <= T <= 10001
# 1 <= N <= 10^16
# 2 <= M <= 10^9
# 입력 케이스
# 3
# 3 3
# 4 7
# 5 18
# 출력 케이스
# 0
# 5
# 5


row = int(input())
matrix = []
for i in range(row):
    matrix.append(list(map(int, input().split())))

print(matrix)

for i in range(0, row):
    matrix[i][0] = int('1'*matrix[i][0])

answer=[]
for i in range(0,row):
    a = matrix[i][0]%matrix[i][1]
    answer.append(a)

for item in answer:
    print(item)
