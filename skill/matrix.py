import sys
n= int(sys.stdin.readline())

dp=[[0]*2 for i in range(n)]
print(dp)

col, row = map(int, input().split())
matrix = []

for i in range(col):
    matrix.append(list(map(int, input().split())))
