T = int(input())

for t in range(1, T+1):
    # N과 M 입력
    N, M = map(int, input().split())
    
    # N x N 배열 입력
    array = []
    for _ in range(N):
        array.append(list(map(int, input().split())))
    
    # 최대 파리 개수 초기화
    max_flies = 0
    
    # M x M 크기의 부분 배열의 합을 계산하여 최대 파리 개수 찾기
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies = 0
            for x in range(M):
                for y in range(M):
                    flies += array[i + x][j + y]
            if flies > max_flies:
                max_flies = flies
    
    # 결과 출력
    print(f"#{t} {max_flies}")