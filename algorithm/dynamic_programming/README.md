<h1>동적계획법(DP)의 핵심</h1>
</p>
<h2>동적계획법</h2>
<p>
그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
<br>
입력크기가 작은 단계부터 해결하고 이를 이용하여 큰 크기의 부분 문제를 해결.
<br>
<h3>Top-down | Bottom-up</h3>
<ul>
    <li>Top-down</li>
    <p>n번째 항이 어디서 비롯되었는지 떠올리면서, 끝부분을 예외처리하여 재귀 처리</p>
    <li>Top-down</li>
    <p>n번째 항을 통해 n+1번째 항을 만든다 생각하면 좋을 듯하다.</p>
</ul>

<h3>skill</h3>
런타임 에러를 막기위해, 배열의 뒷부분을 호출할 때

'''python
for i in range(m-3):
    dp.append(dp[-1]+dp[-2]+dp[-3])


for i in range(4,m):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
'''
<br>윗 부분의 코드를 선호한다.