# 하나 올릴 때 마다 양쪽 비교
import math


def lift_weight(weight_cnt, left, right):
    global combinations_cnt
    if left < right:  # 문제 조건1. 오른쪽은 왼쪽보다 무적권 작아야 한다.
        return
    if left >= total_weight / 2: # 왼쪽 추의 무게가 전체 무게의 절반보다 크면
        leftover_weights = N- weight_cnt # 남은추들을
        combinations_cnt += (2 ** leftover_weights) * math.factorial(leftover_weights) #경우의 수만큼 더해주자.
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            lift_weight(weight_cnt + 1, left + weight_value[i], right)
            if right + weight_value[i]<= left:
                lift_weight(weight_cnt + 1, left, right + weight_value[i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    weight_value = list(map(int, input().split()))
    visited = [0] * N
    combinations_cnt = 0
    total_weight = sum(weight_value)
    lift_weight(0, 0, 0)
    print(f'#{tc} {combinations_cnt}')
