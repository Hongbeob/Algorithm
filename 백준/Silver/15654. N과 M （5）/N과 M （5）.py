N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))


def backtrack(result):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(len(numbers)):
        if numbers[i] not in result:
            result.append(numbers[i])
            backtrack(result)
            result.pop()

backtrack([])