import sys
input = sys.stdin.readline

n= int(sys.stdin.readline())

arr = [1,1,1,1,1,1,1,1,1,1]
temp=[0]*10
x=1
while(x<n):
    for i,v in enumerate(arr):
        temp[i] = sum(arr[i:])
    arr = temp
    x+=1

print(sum(arr))