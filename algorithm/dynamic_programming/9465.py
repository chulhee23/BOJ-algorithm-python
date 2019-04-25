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


    # print answer form like this way
    temp=1

    ans.append(temp)

print(matrix)
print(*ans, end=" ")