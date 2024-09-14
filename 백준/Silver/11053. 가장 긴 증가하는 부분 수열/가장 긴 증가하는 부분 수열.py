N = int(input())
lst = list(map(int, input().split()))
cnt_list=[1]*N
for i in range(1,N):
    for j in range(i):
        # 나보다 index 도 작고 값도 작은 놈들 중에
        # 수열 길이 +1 이 나보다 큰녀석이 있다면
        if lst[i] <= lst[j] or cnt_list[i] >= cnt_list[j] + 1: continue
        cnt_list[i] = cnt_list[j]+1 # 나는 그녀석의 수열 길이에 +1이 된다.
print(max(cnt_list))