while True:
    mylist = sorted(list(map(int, input().split(' ')))) #입력을 받아 오름차순으로 정렬
    if max(mylist) == 0: #입력값 체크(0 0 0)
        break
    elif mylist[0]**2 + mylist[1]**2 == mylist[2]**2: #직사각형인 경우, right 출력
        print("right")
    else: #직사각형이 아닌 경우, wrong 출력
        print("wrong")