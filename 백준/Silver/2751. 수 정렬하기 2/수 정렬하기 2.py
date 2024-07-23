N=int(input())
arr =[int(input()) for _ in range(N)] #시간복잡도 N개의 정수 x 입력의 길이L(L은 입력된 각 정수의 평균 길이) O(NxL)
arr.sort() #nlog(n) N=1,000,000 이면 
for i in range(N):
    print(arr[i])
