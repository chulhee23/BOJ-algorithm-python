import sys
input = sys.stdin.readline
ans=[]


test_cases_number = int(input())
for _ in range(test_cases_number):
    matrix = []
    n = int(input())
    # create matrix
    matrix.append(list(map(int, input().split())))
    matrix.append(list(map(int, input().split())))

    # 점화식의 필연성을 고려할 것.

    # print answer form like this way
    temp=1

    ans.append(temp)

print(matrix)
print(*ans, end=" ")