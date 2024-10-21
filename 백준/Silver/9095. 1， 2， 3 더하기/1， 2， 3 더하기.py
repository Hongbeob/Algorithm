def solve(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    if dp[n] != -1:
        return dp[n]

    dp[n] = solve(n - 1) + solve(n - 2) + solve(n - 3)
    return dp[n]
dp = [-1] * 11
T = int(input())
for i in range(T):
    num = int(input())
    print(solve(num))

