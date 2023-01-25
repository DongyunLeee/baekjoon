import sys

N = int(sys.stdin.readline())
cranes = list()
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)

M = int(sys.stdin.readline())
boxs = list()
boxs = list(map(int, sys.stdin.readline().split()))
boxs.sort(reverse=True)

c_num = 0
num = 0
result = 1
print(cranes)
print(boxs)
if cranes[0] < boxs[0]:
    print(-1)
else:
    while len(boxs):
        while len(boxs):
            if num == len(boxs):
                cranes.remove(cranes[c_num])
                c_num -= 1
                break
            elif cranes[c_num] >= boxs[num]:
                print(result, cranes[c_num], boxs[num])
                boxs.pop(num)
                break
            else:
                num += 1
        if len(boxs):
            c_num += 1
            if c_num == len(cranes):
                result += 1
                c_num = 0
                num = 0

print(result)

