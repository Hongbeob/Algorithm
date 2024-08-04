n=int(input())
arr=[5,3]
min_kg = 9999

for i in range(n//arr[0]+1):
    X=n-arr[0]*i
    if X % arr[1] ==0:
        if min_kg>i+(X//arr[1]):
            min_kg=i+(X//arr[1])
if min_kg ==9999:
    print(-1)
else:
    print(min_kg)