def solve():

    if N == 1:
        return stairs[0]

    dp = [0] * N
    dp[0] = stairs[0]

    if N > 1:
        dp[1] = stairs[0] + stairs[1]

    for i in range(2, N):
        # 현재 계단을 밟고 두 계단 전에서 올라오는 경우와
        # 한 계단 전 계단을 밟고 세 계단 전에서 올라오는 경우 중 최대값 선택
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    # 마지막 계단에서의 최대 점수 반환
    return dp[N - 1]


N = int(input())
stairs = [int(input()) for _ in range(N)]

# 결과 출력
print(solve())