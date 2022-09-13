from sys import stdin
from collections import Counter


def Mean(buf, num):
    print(round(sum(buf) / num))


def Median(buf, num):
    print(buf[(num // 2)])


# Counter 라이브러리 사용
def Mode(buf):
    if len(buf) == 1:
        print(buf[0])
        return
    buf = Counter(buf)
    if buf.most_common(2)[0][1] > buf.most_common(2)[1][1]:
        print(buf.most_common(2)[0][0])
    else:
        print(buf.most_common(2)[1][0])


# 반복문을 통한 직접 비교
def Mode(buf):
    P = [0] * 4001
    M = [0] * 4001
    max_num = 0
    cnt = 0
    ret = 0
    for i in buf:
        if i<0:
            M[abs(i)] += 1
            if M[abs(i)] > max_num:
                max_num = M[abs(i)]
        else:
            P[i] += 1
            if P[i] > max_num:
                max_num = P[i]

    for i in range(-4000, 4001):
        if i < 0 and M[abs(i)] == max_num:
            cnt += 1
            ret = i
            if cnt == 2:
                print(i)
                break
        elif i >= 0 and P[i] == max_num:
            cnt += 1
            ret = i
            if cnt == 2:
                print(i)
                break

    if cnt == 1:
        print(ret)


def Range(buf):
    print(buf[-1] - buf[0])


N = int(stdin.readline())
item_list = []

for item in range(N):
    item_list.append(int(stdin.readline()))
item_list.sort()

Mean(item_list, N)
Median(item_list, N)
Mode(item_list)
Range(item_list)



