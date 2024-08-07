def dfs(start):
    visited = [0] * (N)
    stack = [start]
    while stack:
        current = stack[-1]
        for i in range(0, N):
            # adj[current][i] >>>1 이면 current 와 i가 인접한 정점
            # 만약에 인접하면서 방문하지 않았으면 방문한다.
            # 방문하게 되면, 경로에 추가, 방문 표시 하기
            if adj_matrix[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break  # current에 인접한 정점 찾기 중단, 찾은 길로 가려고
        else:  # for else: current 정점에서 더이상 갈 수 있는 정점이 없다.
            stack.pop()
    return visited
N= int(input())
adj_matrix=[list(map(int,input().split())) for _ in range(N)] #인접 행렬

for i in range(N):
    print(*dfs(i))