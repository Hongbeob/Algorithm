def solve(cnt=0):
    if tuple(result) in memo:
        return

    if len(result) == M:
        memo.add(tuple(result))
        print(* result)
        return

    for i in range(cnt,N):
        result.append(lst[i])
        solve(i)
        result.pop()



N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []
memo=set()
solve()