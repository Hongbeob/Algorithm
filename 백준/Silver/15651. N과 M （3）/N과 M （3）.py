N, M = map(int, input().split())

def back(result, N, M):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        back(result, N, M)
        result.pop()

back([], N, M)