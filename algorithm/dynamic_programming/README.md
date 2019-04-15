<h1>동적계획법(DP)의 핵심</h1>
</p>
<h2>동적계획법</h2>
<p>
그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
<br>
입력크기가 작은 단계부터 해결하고 이를 이용하여 큰 크기의 부분 문제를 해결.
<br>


<h3>skill</h3>
런타임 에러를 막기위해, 배열의 뒷부분을 호출할 때

'''python
for i in range(m-3):
    dp.append(dp[-1]+dp[-2]+dp[-3])


for i in range(4,m):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
'''
<br>윗 부분의 코드를 선호한다.