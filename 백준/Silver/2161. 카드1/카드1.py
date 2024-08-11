from collections import deque
arr=[i for i in range(1,int(input())+1,)]
N=len(arr)
arr=deque(arr)
for i in range(N):
    print(arr.popleft(),end=' ')
    if arr:
        arr.append(arr.popleft())