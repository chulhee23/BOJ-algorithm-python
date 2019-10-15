# n: 정점 , m: 간선, v: 탐색 시작하는 정점의 번호
n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n + 1)]

for _ in range(m):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1
# 간선 표기

def dfs(current_node, graph, visited):
    visited += [current_node]
    row = graph[current_node]
    for search_node in range(len(row)):
        if row[search_node] and search_node not in visited:
            visited = dfs(search_node, graph, visited)
    return visited

def bfs(start):
    queue = [start]
    visited = [start]
    while queue:
        print(queue)
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in visited:
                visited += [search_node]
                queue += [search_node]
    return visited


print(*dfs(v, matrix, []))

print(*bfs(v))