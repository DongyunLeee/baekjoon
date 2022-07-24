num = int(input()) #분해합 입력

flag = 0 #생성자 확인 flag
for i in range(1, num):
    if i+sum(map(int, str(i))) == num: #생성자 체크 -> 출력, flag on, 반복문 탈출
        print(i)
        flag = 1
        break

if not flag: #생성자 flag 체크
    print(0)