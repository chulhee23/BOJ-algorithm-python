<h1>bfs 문제 접근</h1>
<ul>
<li>BFS는 층을 기반으로 센다 (거리)</li>
<li>최소 거리를 찾을 때 사용하자</li>
<li>자료구조의 queue를 사용한다</li>
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


<h1>실제 사용</h1>
<p>
```
python
queue = []
```

위와 같이 사용하면 에러가 발생하기도 하며, 굉장히 느리다.
그렇기에 실제로는 deque(덱)을 사용해야 한다.
double ended queue는 양 방향에서 요소의 추가, 삭제 가능하다.
그렇기에 오히려 선입선출 구조를 갖는 큐를 만들기에 적합하다.
```
python
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)

queue.appendleft(3)
queue.appendleft(4)

print(queue)

queue.pop()
queue.popleft()

print(queue)
```
양 방향에서 활용이 가능하지만, 큐보다 덱이 훨씬 빠르기 때문에 덱을 통해 큐를 구현하여 사용하면 된다.
</p>