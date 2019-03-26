<h1>bfs 문제 접근</h1>
<ul>
<li>BFS는 층을 기반으로 센다 (거리)</li>
<li>최소 거리를 찾을 때 사용하자</li>
<li>자료구조의 queue를 사용한다</li>
<li>python의 collections의 deque 사용해야 에러가 나지 않는다.</li>

</ul>

<hr>
<p>donsworkout 참고<p>

<h1>큐의 구조 </h1>
<h2>FIFO(선입선출) 구조</h1>

<p>first ->_ _ _ _ _ <-rear </p>

<p>
Enqueue : 큐 맨 뒤에 어떠한 요소를 추가

Dequeue : 큐 맨 앞쪽의 요소를 삭제

front : 큐의 맨 앞의 위치(인덱스)

rear : 큐의 맨 뒤의 위치(인덱스)
</p>