def boy_actions(number, switch_n, switch_s): # 남학생 행동
    for i in range(switch_n):
        if (i + 1) % number == 0: # 스위치 숫자가 자기 번호의 배수일 때
            # 반전
            if switch_s[i] == 1:
                switch_s[i] = 0
            else:
                switch_s[i] = 1

def girl_actions(number, switch_n, switch_s): # 여학생 행동
    a = number - 1 # index는 0부터 시작해서 -1 (변수명 고민하다가 7분 지났길래 그냥 a로...)  
    # 자기 번호는 무조건 반전
    if switch_s[a] == 1: 
        switch_s[a] = 0
    else:
        switch_s[a] = 1

    # 자기 번호 좌우 비교 후 반전
    for i in range(1, switch_n): # 원래 min 써서 배열 범위 안 벗어나려고 했는데 아래 조건식 써서 그냥 switch_n으로 바꿨음.
        if a - i >= 0 and a + i < switch_n: # 배열의 범위 벗어나는지 아닌지 확인
            if switch_s[a - i] == switch_s[a + i]: # 좌우 대칭
                # 반전(좌우가 대칭이어서 왼쪽만 확인 후 반전 그리고 오른쪽에 할당)
                if switch_s[a - i] == 1:
                    switch_s[a - i] = 0
                else:
                    switch_s[a - i] = 1
                switch_s[a+i] = switch_s[a-i]
                
            else:
                break
        else:
            break

switch_count = int(input()) # 스위치 수
switch_state = list(map(int, input().split())) # 스위치 상태
student_count = int(input()) # 학생 수
gender_num = [tuple(map(int, input().split())) for _ in range(student_count)] # 학생 성별과 번호

for gender, num in gender_num:
    if gender == 1:
        boy_actions(num, switch_count, switch_state)
    else:
        girl_actions(num, switch_count, switch_state)

for i in range(len(switch_state)): # 출력
    if i > 0 and i % 20 == 0: # 21번째는 아랫줄로 가라!
        print()
    if (i + 1) % 20 != 0: # 스위치 결과 사이엔 공백!
        print(switch_state[i], end=' ')
    else: # 20번째는 공백 없기.
        print(switch_state[i], end='')