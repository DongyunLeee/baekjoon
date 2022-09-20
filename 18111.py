import sys
from sys import stdin


# 완전탐색 사용
def minecraft(arr, target, end, b):
    ret_t = sys.maxsize
    ret_h = 0
    while target <= end:
        cnt = 0
        block = b
        for item, num in enumerate(arr):
            if num < start and num > end:
                continue
            if item >= target:
                cnt += ((item - target) * 2 * num)
                block += ((item - target) * num)
            else:
                cnt += ((target - item) * num)
                block -= ((target - item) * num)

        if block >= 0 and cnt <= ret_t:
            ret_t = cnt
            ret_h = target
        target += 1
    return ret_t, ret_h


N, M, B = map(int, stdin.readline().split())
li = [0]*257
start = 256
end = 0

for i in range(N):
    t = list(map(int, stdin.readline().split()))
    for i in t:
        li[i] += 1
    end = max(end, max(t))
    start = min(start, min(t))

result = minecraft(li, start, end, B)
print(result[0], result[1])