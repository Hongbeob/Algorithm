#인접 리스트
from heapq import heappush, heappop


def prim(start):
    heap=[]
    MST=[0] * (N+1)

    sum_dist=0

    heappush(heap,(0,start))

    while heap:
        dist, c_island = heappop(heap)
        if MST[c_island]:
            continue

        sum_dist += E * dist

        for next in range(N-1):
            next_island,next_dist = graph[c_island][next]
            if MST[next_island]:
                continue

            heappush(heap,(next_dist,next_island))
        MST[c_island] = 1
    return round(sum_dist)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N : 섬의 개수
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    p = [i for i in range(N + 1)]
    position = list(zip(X, Y))
    graph = [[] for _ in range(N+1)] #인접 리스트
    for i in range(N):
        for j in range(N):
            if i==j:continue
            x_sq = (position[i][0] - position[j][0]) ** 2
            y_sq = (position[i][1] - position[j][1]) ** 2
            graph[i+1].append((j+1,x_sq + y_sq))
    print(f'#{tc} {prim(1)}')