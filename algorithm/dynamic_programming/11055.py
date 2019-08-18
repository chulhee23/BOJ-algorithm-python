 # 증가하는 부분 수열(a[j] < a[i]) 중, 
 # 현재 비교기준 값(d[i])이 이전번째까지의 합(d[j]) + 자신의 값(a[i])보다 작을 때, 
 # d[i] = d[j] + a[i]를 해준다
import sys
 
num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
 
d = [0 for i in range(num)]
 
for i in range(num):
    d[i] = arr[i]
 
for i in range(num):
    for j in range(i, -1, -1):
        if arr[j] < arr[i] and d[j] > d[i] - arr[i]:
            d[i] = d[j] + arr[i]
 
sys.stdout.write(str(max(d)))