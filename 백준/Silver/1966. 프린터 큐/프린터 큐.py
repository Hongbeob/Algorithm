T = int(input()) #test 케이스 수
result=[]
for i in range(T):
    N, M = map(int,input().split()) #N = 문서의 개수, M = 확인하고 싶은 자료의 위치
    arr =list(map(int,input().split())) #입력을 받을 때 (i,i) 이런식으로 저장할 수 있나?
    point = [(i,arr[i]) for i in range(N)] #있다 튜블로 받으면 됨

    print_1 = 0 #제일 큰 중요도 발견 시 프린트 할건데그 때 프린트 횟수 체크 용

    while True:
        a=point.pop(0) # 첫 번째 값 빼서 이제 비교할거임
        success = False
        for j in point: #point 안의 튜플들로 비교돌리기.
            if a[1] < j[1]: #[1]인 이유는 point가 튜플로 이루어진 list이고 1이 중요도가 저장되어있음.제일 중요도가 높은게 앞으로 올 수 있도록 만들기.
                point.append(a) #나보다 높은 중요도가 있어? 난 뒤로갈게
                success =True
                break # 나보다 높은 놈 찾았으니까 비교 끝낼게
            

        #나보다 큰놈dl 없다면
        if not success:
            print_1 +=1
            if a[0]==M:
                result.append(print_1)
                break

for i in result:
    print(i)
