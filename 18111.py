import sys
from sys import stdin


# 완전탐색 사용
def minecraft(arr, target, end, b):
    ret_t = sys.maxsize
    ret_h = 0
    while target <= end:
        cnt = 0
        block = b
        for i in arr:
            for item in i:
                if item >= target:
                    cnt += ((item - target) * 2)
                    block += (item - target)
                else:
                    cnt += (target - item)
                    block -= (target - item)

        if block >= 0 and cnt <= ret_t:
            ret_t = cnt
            ret_h = target
        target += 1
    return ret_t, ret_h


N, M, B = map(int, stdin.readline().split())
li = list()
start = 256
end = 0

for i in range(N):
    li.append(list(map(int, stdin.readline().split())))
    end = max(end, max(li[i]))
    start = min(start, min(li[i]))

result = minecraft(li, start, end, B)
print(result[0], result[1])