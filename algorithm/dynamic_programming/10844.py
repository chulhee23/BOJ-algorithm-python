import sys
input = sys.stdin.readline

# 1자리일 때 arr
arr = [0,1,1,1,1,1,1,1,1,1]
temp = [0]*10

n = int(sys.stdin.readline())
x=1
while( x<n ):
    temp = [0]*10
    for (i,v) in enumerate(arr):
        if (i==0):
            temp[i] += arr[i+1]
        elif (i==9):
            temp[i] += arr[i-1]
        else:
            temp[i] += arr[i-1]+arr[i+1]
    arr = temp
    x+=1

print(sum(arr)%1000000000)
