# 1. +랑 -를 저장할 리스트
# 2. 숫자를 1부터 n 까지 저장할 stack
# 2-1. 중간에 현재 입력한 숫자값이 나왔는지 확인하는 조건문
def solve():
    cnt = 1
    for _ in range(int(input())):
        num = int(input())
        while cnt <= num:
            stack.append(cnt)
            result.append('+')
            cnt += 1

        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return print('NO')
    else:
        return True


result = []
stack = []
if solve():
    for i in result:
        print(i)
