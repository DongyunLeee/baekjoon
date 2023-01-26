import sys
# 문제는 그리디 알고리즘을 사용하여 크레인이 옮길 수 있는
# 최대한의 무게의 박스부터 옮겨서 최소의 소요시간을 탐색한다.

# 크레인의 수와 무게제한 입력 및 정렬(내림차순)
N = int(sys.stdin.readline())
cranes = list()
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)

# 박스의 수와 무게 입력 및 정렬(내림차순)
M = int(sys.stdin.readline())
boxs = list()
boxs = list(map(int, sys.stdin.readline().split()))
boxs.sort(reverse=True)

# 크레인의 최대 무게제한보다 박스의 최대 무게가 큰 경우, -1 출력
if cranes[0] < boxs[0]:
    print(-1)
else:
    c_num = 0
    num = 0
    result = 0
    while len(boxs):
        if c_num == len(cranes):
            num = 0
            c_num = 0
            result += 1
        if num == len(boxs):
            cranes.remove(cranes[c_num])
            num = 0
        elif cranes[c_num] >= boxs[num]:
            boxs.remove(boxs[num])
            c_num += 1
        else:
            num += 1

    result += 1
    print(result)

