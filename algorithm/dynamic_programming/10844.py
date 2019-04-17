import sys
input = sys.stdin.readline

digit = int(input())

a = 10**(digit-1)
b = 10**digit

ans=[0,9,17]

for i in range(3,digit+1):
    ans.append((ans[i-1]-3)*2 + 4)

print(ans[digit])