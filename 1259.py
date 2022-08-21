# while문을 사용한 반복
while True:
    # 검사할 값 입력
    P = input()
    # 값이 0인경우, 중지
    if P == "0":
        break

    # 팰린드롬수 검사
    a, b = list(P), list(P)
    b.reverse()
    if str(a) == str(b):
        print("yes")
    else:
        print("no")
