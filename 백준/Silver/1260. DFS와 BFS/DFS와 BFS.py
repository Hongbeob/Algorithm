def DFS(V, visited, result_dfs):
    visited[V] = 1
    result_dfs.append(V)
    for i in range(1, N + 1):
        if adj[V][i] and not visited[i]:
            DFS(i, visited, result_dfs)
    return result_dfs


def BFS(start, result_bfs):
    visited = [0] * (N + 1)
    q = [start]
    visited[start] = 1

    while q:
        current = q.pop(0)
        result_bfs.append(current)
        for i in range(1, N + 1):
            if adj[current][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] =  1
    return result_bfs


N, M, V = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
visited = [0] * (N + 1)
result1 = DFS(V, visited, [])
print(*result1)
result2 = BFS(V, [])
print(*result2)
