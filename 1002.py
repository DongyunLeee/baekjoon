import math

num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    n = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#주어진 지점(중심점)과 목표까지의 거리(반지름)를 하나의 원으로 보고 풀이 진행할 것!
    if n == 0 and r1 == r2: #두 원이 같고 반지름도 같은 경우
        print(-1)
    elif n == abs(r1-r2) or n == r1 + r2: #두 원이 내접하거나 외접할때
        print(1)
    elif abs(r1-r2) < n < r1 + r2: # 두 원이 서로 다른 두 지점에서 만날때
        print(2)
    else: #그 외
        print(0)