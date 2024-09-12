def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return p[x]


def union(x, y):  # 대표자를 비교해서 같은 그래프인지 알아보자
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:  # 같다면 같은 그래프다.
        return

    if root_x > root_y:  # 같지 않고 x 루트가 더 크면 x의 루트는 y의 루트로 바꾼다.
        p[root_x] = root_y
    else:
        p[root_y] = root_x


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N : 섬의 개수
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    p = [i for i in range(N + 1)]
    position = list(zip(X, Y))
    graph = []
    for i in range(N):
        for j in range(i + 1, N):
            x_sq = (position[i][0] - position[j][0]) ** 2
            y_sq = (position[i][1] - position[j][1]) ** 2
            graph.append((i + 1, j + 1, x_sq + y_sq))  # 가중치
    graph.sort(key=lambda x: x[2])
    cnt = 0
    total = 0
    for start, end, dist in graph:
        if find_set(start) != find_set(end):
            cnt += 1
            union(start, end)
            total += (E * dist)
            if cnt == N - 1:
                break
    print(f'#{tc} {round(total)}')