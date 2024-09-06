import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    m = list(input().split())
    if m[0] == 'add':
        s.add(int(m[1]))
    elif m[0] == 'remove':
        try:
            s.remove(int(m[1]))
        except:
            pass
    elif m[0] == 'check':
        if int(m[1]) in s:
            print(1)
        else:
            print(0)
    elif m[0] == 'toggle':
        if int(m[1]) in s:
            s.remove(int(m[1]))
        else:
            s.add(int(m[1]))
    elif m[0] == 'all':
        s = set([i for i in range(1,21)]) 
    else:
        s = set()