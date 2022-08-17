# 완전탐색 문제
# input num, goal, card
num, goal = map(int, input().split())
card = list(map(int, input().split()))

# 완전탐색을 진행하며 goal에 가장 가까운 합을 탐색
# (주의)goal을 넘지 않는 합의 값을 탐색해야함!!
result = 0
check = True
for x in range(num-2):
    for y in range(x+1, num-1):
        for z in range(y+1, num):
            tmp = card[x] + card[y] + card[z]
            if tmp == goal:
                result = tmp
                check = False
                break
            if tmp < goal:
                result = max(result, tmp)
        if check is False:
            break
    if check is False:
        break

print(result)