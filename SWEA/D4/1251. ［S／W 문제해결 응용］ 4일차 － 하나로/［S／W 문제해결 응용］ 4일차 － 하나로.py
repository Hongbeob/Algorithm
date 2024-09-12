from heapq import heappush, heappop


def prim(start):
    heap=[]
    MST=[0] *(N+1)

    sum_dist=0

    heappush(heap,(0,start))

    while heap:
        dist, c_island = heappop(heap)
        if MST[c_island]:
            continue

        MST[c_island] = 1
        sum_dist += E * dist

        for next in range(1,N+1):
            if graph[c_island][next] ==0:
                continue

            if MST[next]:
                continue

            heappush(heap,(graph[c_island][next],next))

    return round(sum_dist)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N : 섬의 개수
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    p = [i for i in range(N + 1)]
    position = list(zip(X, Y))
    graph = [[0]*(N+1) for _ in range(N+1)] #인접 리스트
    for i in range(N):
        for j in range(i + 1, N):
            x_sq = (position[i][0] - position[j][0]) ** 2
            y_sq = (position[i][1] - position[j][1]) ** 2
            graph[i+1][j+1]= x_sq + y_sq
            graph[j+1][i+1]= x_sq + y_sq
    print(f'#{tc} {prim(1)}')