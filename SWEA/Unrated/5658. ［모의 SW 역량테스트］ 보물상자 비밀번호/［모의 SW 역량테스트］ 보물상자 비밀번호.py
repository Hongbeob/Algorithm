from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num=deque(input())
    result=set()
    for _ in range(N//4):
        num.append(num.popleft())
        for X in range(0,N,N//4):
            tmp=list(num)
            if int(''.join(tmp[X:X+N//4]),16) in result: continue
            result.add(int(''.join(tmp[X:X+N//4]),16))
    result=list(result)
    result.sort(reverse=True)
    print(f'#{tc} {result[K-1]}')