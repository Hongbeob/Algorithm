def solve(N):
    if N - int(N) >= 0.5:
        return int(N) + 1
    else:
        return int(N)


N = int(input())
lst = [int(input()) for _ in range(N)]
if N == 0:
    print(0)
elif N < 4:
    print(solve(sum(lst) / N))
else:
    lst.sort()
    x = solve(N * 0.15)
    lst_sum, n = sum(lst[x:N - x]), N - (x * 2)
    result = solve(lst_sum / n)
    print(result)
