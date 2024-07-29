N,M = map(int,input().split())
arr = list(map(int, input().split()))
sum_s=[]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            arr_sum = arr[i] + arr[j] + arr[k]
            sum_s.append(arr_sum)

result=0
for s in sum_s:
    if s <= M and s > result:
        result = s

print(result)