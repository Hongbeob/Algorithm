T=int(input())
ans=[]
for i in range(T):
    k=int(input())
    n=int(input())
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    dummy = lst[:]
    if k ==1:
        sum_1 = sum(lst)
    else:
        for j in range(k-1):
            for i in range(n):
                lst[i]=sum(dummy[0:i+1])
            dummy=lst[:]
        sum_1 = sum(lst)
    ans.append(sum_1)
for i in range(len(ans)):
    print(ans[i])