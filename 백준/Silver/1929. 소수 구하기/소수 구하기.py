from math import sqrt

M, N = map(int, input().split())
for num in range(M, N + 1):
    if num == 1: continue
    X = int(sqrt(num))
    for i in range(2, X+1):
        if num % i == 0: break
    else: print(num)
