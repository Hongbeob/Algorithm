def boy_actions(number, switch_n, switch_s):
    for i in range(switch_n):
        if (i + 1) % number == 0:
            if switch_s[i] == 1:
                switch_s[i] = 0
            else:
                switch_s[i] = 1

def girl_actions(number, switch_n, switch_s):
    a = number - 1
    if switch_s[a] == 1:
        switch_s[a] = 0
    else:
        switch_s[a] = 1

    for i in range(1, min(a, switch_n - a - 1) + 1):
        if a - i >= 0 and a + i < switch_n:
            if switch_s[a - i] == switch_s[a + i]:
                if switch_s[a - i] == 1:
                    switch_s[a - i] = 0
                else:
                    switch_s[a - i] = 1
                switch_s[a+i] = switch_s[a-i]
                
            else:
                break
        else:
            break

switch_count = int(input())
switch_state = list(map(int, input().split()))
student_count = int(input())
gender_num = [tuple(map(int, input().split())) for _ in range(student_count)]

for gender, num in gender_num:
    if gender == 1:
        boy_actions(num, switch_count, switch_state)
    else:
        girl_actions(num, switch_count, switch_state)

for i in range(len(switch_state)):
    if i > 0 and i % 20 == 0:
        print()
    if (i + 1) % 20 != 0:
        print(switch_state[i], end=' ')
    else:
        print(switch_state[i], end='')