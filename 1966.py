from sys import stdin

TC = int(stdin.readline())

for item in range(TC):
    N, M = map(int, stdin.readline().split())
    critical = list(stdin.readline().split())

    # 루프를 돌며 목표한 위치에 있는 문서가 인쇄되는 순번을 계산
    loop_flag = True
    while loop_flag:
        flag = True
        for i in critical[1:]:
            if i > critical[0]:
                critical.append(critical.pop(0))
                flag = False
                if M == 0:
                    M = len(critical)
                break

        if flag == True:
            if M == 0:
                print(N - (len(critical)-1))
                loop_flag = False
                break
            critical.pop(0)
        M -= 1