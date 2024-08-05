N = int(input())
stack = []
arr = [input() for _ in range(N)]
for i in arr:
    if i.isalpha():
        if i == 'pop':
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        elif i == 'size':
            print(len(stack))
        elif i == 'empty':
            if len(stack) > 0:
                print(0)
            else:
                print(1)
        elif i == 'top':
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)

    else:
        str,num=i.split(' ')
        stack.append(num)