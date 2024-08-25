# 0,0 출발
# N X N 정사각형
# dr dc =[[1,0] [0,1]]
# N-1,N-1 도달 시 승리
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
#     우 하
dr = [0, 1]
dc = [1, 0]

q = [(0, 0)]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
while q:
    cr,cc=q.pop(0)
    for k in range(2):
        mr = cr + dr[k] * lst[cr][cc]
        mc = cc + dc[k] * lst[cr][cc]
        if 0 <= mr < N and 0 <= mc < N and visited[mr][mc] == 0:
            q.append((mr,mc))
            visited[mr][mc] += visited[cr][cc] + 1

if visited[-1][-1] !=0:
    print('HaruHaru')
else:
    print('Hing')