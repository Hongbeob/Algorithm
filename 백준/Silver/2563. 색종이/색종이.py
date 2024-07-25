arr=[] #튜플 저장할 리스트
def area_calculate(x,y): #넓이를 구하는데, 튜블을 넓이만큼 생성시키면 튜블 갯수가 넓이가 될거다.
    for i in range(10):
        for j in range(10):
            arr.append((x+i,y+j))

T=int(input())# 색종이 수

for i in range(T): #색종이 수만큼 반복
    x,y=map(int,input().split()) #색종이 시작 위치
    area_calculate(x,y)# 색종이 넓이로 쓰일 튜블들 생성하고 리스트에 저장하기.

print(len(set(arr))) #set함수는 중복을 제거해준다. 이걸로 겹치는 부분 제거
