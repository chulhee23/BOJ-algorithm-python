# 동적 계획법의 사용
import sys
input = sys.stdin.readline

n = int(input())
d = [0,0,1,1]

# d[x//3]+1
# d[x//2]+1 의 값과 비교
for i in range(4,n+1):
    d.append(d[i-1]+1)
    if (i%3==0):
        d[i] = min(d[i], d[i//3]+1)
    elif(i%2==0):
        d[i] = min(d[i], d[i//2]+1)

print(d[n])
