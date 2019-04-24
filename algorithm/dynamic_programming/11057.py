import sys

n= int(sys.stdin.readline())

arr = [1,1,1,1,1,1,1,1,1,1]
temp=[0]*10
x=1
while(x<n):
    for i,v in enumerate(arr):
        temp[i] = sum(arr[i:])%10007
        # 런타임 에러 해결을 위해 미리 10007로 나눠줬다.
    arr = temp
    x+=1

print(sum(arr)%10007)
