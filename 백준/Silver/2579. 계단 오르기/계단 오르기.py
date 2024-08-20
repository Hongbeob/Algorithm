# 탑다운(재귀함수, 메모이제이션)
# 계단 리스트에서 최대 점수를 계산하는 함수
def max_score(stairs, dp, idx):
    if idx < 0:
        return 0

    # 메모이제이션: 이미 계산한 값이 있으면 그 값을 반환
    if dp[idx] != -1:
        return dp[idx]

    # 첫 계단만 밟을 경우
    if idx == 0:
        dp[idx] = stairs[0]
        return dp[idx]

    # 첫 번째 계단과 두 번째 계단만 밟을 경우
    if idx == 1:
        dp[idx] = stairs[0] + stairs[1]
        return dp[idx]

    # 현재 계단을 밟고 두 계단 전에서 올라오는 경우 또는
    # 현재 계단을 밟고 한 계단 전 계단을 밟고 세 계단 전에서 올라오는 경우
    dp[idx] = max(max_score(stairs, dp, idx - 2) + stairs[idx],
                  max_score(stairs, dp, idx - 3) + stairs[idx - 1] + stairs[idx])

    return dp[idx]


N = int(input())
dp = [-1] * N
stairs = [int(input()) for _ in range(N)]

print(max_score(stairs, dp, N - 1))