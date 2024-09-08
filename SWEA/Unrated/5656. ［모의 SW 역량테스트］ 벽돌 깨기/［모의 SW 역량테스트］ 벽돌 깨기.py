import copy

T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(board, x, y):
    # 공이 벽을 만났으면 벽의 숫자를 확인하고
    # 벽의 숫자만큼의 범위를 공격한다.
    visited = [[0] * W for _ in range(H)]
    visited[x][y] = 1
    stack = [(x, y, board[x][y])]
    remove_cnt = 0

    while stack:
        cr, cc, power = stack.pop()
        remove_cnt += 1
        board[cr][cc] = 0
        for i in range(4):
            nr, nc = cr, cc
            for _ in range(power - 1):
                nr += dr[i]
                nc += dc[i]
                if nr<0 or nr>=H or nc<0 or nc>=W or visited[nr][nc]: continue
                # if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] == 0:
                if board[nr][nc] <= 0: continue
                stack.append((nr, nc, board[nr][nc]))
                visited[nr][nc] = 1
    for i in range(W):
        new_col = [board[j][i] for j in range(H) if board[j][i] > 0]
        for j in range(H - len(new_col)):
            board[j][i] = 0
        for k in range(H - len(new_col), H):
            board[k][i] = new_col[k - (H - len(new_col))]

    return remove_cnt


def backtracking(depth, board):
    result = sum(board[i][j] > 0 for i in range(H) for j in range(W))

    if result == 0:
        return 0

    if depth == N:
        return result

    min_result = result
    for col in range(W):
        new_board = copy.deepcopy(board)
        for row in range(H):
            if new_board[row][col] > 0:
                dfs(new_board, row, col)
                min_result = min(min_result, backtracking(depth + 1, new_board))
                break
    return min_result


for tc in range(1, T + 1):
    N, W, H = map(int, input().split())  # 구슬, 가로, 세로
    lst = [list(map(int, input().split())) for _ in range(H)]
    print(f'#{tc} {backtracking(0,lst)}')
