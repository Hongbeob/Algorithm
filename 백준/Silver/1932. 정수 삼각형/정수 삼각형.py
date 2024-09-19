N = int(input())
top = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            top[i][j] += top[i - 1][j]
        elif j == i:
            top[i][j] += top[i - 1][j - 1]
        else:
            top[i][j] += max(top[i - 1][j - 1], top[i - 1][j])

print(max(top[-1]))