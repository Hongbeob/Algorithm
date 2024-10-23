from collections import deque

T = int(input())


def solve(r, c):
    global cnt
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    q = deque([(r, c)])
    if (r,c) in arr:
        arr.remove((r,c))
    while q:
        r_p, c_p = q.popleft()

        for i in range(4):
            mr_p = r_p + dr[i]
            mc_p = c_p + dc[i]
            if (mr_p, mc_p) in arr:
                q.append((mr_p, mc_p))
                arr.remove((mr_p, mc_p))

    if arr:
        r, c = arr.pop()
        cnt += 1
        solve(r, c)


for tc in range(1, T + 1):
    cnt = 1
    M, N, K = map(int, input().split())
    arr = set()
    for _ in range(K):
        r, c = map(int, input().split())
        arr.add((r, c))
    solve(r, c)
    print(cnt)
