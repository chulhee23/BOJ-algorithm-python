## DFS
깊이 우선탐색,
말 그대로 그래프에서 가장 최상위 노드부터 하위노드까지 제일 깊게 탐색

## BFS
너비 우선 탐색.
최상위 노드부터 다음 차수의 노드를 탐색.

* BFS

```
def BFS():
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            if cur == target:
                print(cur)
                return
            for elem in child[cur]
                if elem not in visited:
                    queue.append(elem)
                    visited.append(elem)
        # 레벨 업 (깊이 추가)
        cnt += 1 
```


```
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
    
def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

```
