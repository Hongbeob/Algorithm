from collections import deque
A,B = map(int,input().split())
q = deque() #입력 숫자와 연산 수를 저장할 deque
q.append((A,1))
r = 0

while(q):
    n,t = q.popleft()
    if n > B:
        continue
    if n == B:
        print(t)
        break
    q.append((int(str(n)+"1"),t+1))
    q.append((n*2,t+1))
else:
    print(-1)