import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[0]*(n+1) for _ in range(n+1)]
all_node = list(range(1, n+1))

for _ in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

def BFS():

    while queue:

