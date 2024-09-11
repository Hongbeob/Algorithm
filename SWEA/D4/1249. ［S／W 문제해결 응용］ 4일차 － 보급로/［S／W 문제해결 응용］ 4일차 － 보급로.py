import heapq


def dijkstra(start_r, start_c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    pq = []
    heapq.heappush(pq, (0, start_r, start_c))
    elapsed_time = [[1e9] * N for _ in range(N)]
    elapsed_time[start_r][start_c] = 0

    while pq:
        time, cr, cc = heapq.heappop(pq)

        if elapsed_time[cr][cc] < time:
            continue

        for i in range(4):
            mr = cr + dr[i]
            mc = cc + dc[i]

            if 0 <= mr < N and 0 <= mc < N:
                m_time = lst[mr][mc]
                nested_time = time + m_time

                if nested_time >= elapsed_time[mr][mc]:
                    continue

                elapsed_time[mr][mc]= nested_time
                heapq.heappush(pq,(nested_time,mr,mc))
    # print(elapsed_time)
    return elapsed_time[-1][-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {dijkstra(0,0)}')
