import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0] * n

for i in range(n):
    if i == 0:
        d[i] = 1
    else:
        tmp = 0
        for j in range(i):
            if(arr[j] > arr[i]) and (tmp < d[j]):
                tmp = d[j]
        d[i] = tmp + 1

print(max(d))