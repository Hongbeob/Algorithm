T = int(input())
for tc in range(1, T + 1):
    jobcho = input()
    stack = []
    cnt = 0
    top = None
    for string in jobcho:
        if string == '(':
            stack.append(string)
            if stack:
                top = stack[-1]
            else:
                top= None

        elif string == ')':
            if stack and (top == '(' or top == '|'):
                cnt += 1
                stack.pop()
                if stack:
                    top = stack[-1]
                else:
                    top = None

        elif string == '|':
            if stack and top == "(":
                cnt += 1
                stack.pop()
                if stack:
                    top = stack[-1]
                else:
                    top = None
            else:
                stack.append(string)
                if stack:
                    top = stack[-1]
                else:
                    top = None
    print(f'#{tc} {cnt}')