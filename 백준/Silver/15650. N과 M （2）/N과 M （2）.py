N, M = map(int, input().split())

def back(result, start, N, M):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N + 1):
        if i not in result:
            result.append(i)
            back(result, i + 1, N, M)
            result.pop()

back([], 1, N, M)