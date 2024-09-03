import copy  # 깊은 복사를 위해 copy 모듈을 가져옵니다.

def dfs(index, visited, board):
    global cnt
    if index == N:
        cnt += 1
        return

    for i in range(N):
        if visited[index + 1][i + 1] == 0:
            board[index][i] = 1
            new_visited = visited_obstruct(index + 1, i + 1, visited)
            dfs(index + 1, new_visited, board)
            board[index][i] = 0

def visited_obstruct(x, y, visited):
    new_visited = copy.deepcopy(visited)  # 깊은 복사를 사용하여 새로운 visited 생성
    for i in range(1, N + 1):
        new_visited[x][i] = 1
        new_visited[i][y] = 1
        if x + i <= N and y + i <= N:
            new_visited[x + i][y + i] = 1
        if x + i <= N and y - i >= 1:
            new_visited[x + i][y - i] = 1

    return new_visited

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    cnt = 0
    dfs(0, visited, board)
    print(f'#{tc} {cnt}')