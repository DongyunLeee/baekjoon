from sys import stdin

# 입력값 받기
N = int(stdin.readline())
N_list = map(int, stdin.readline().split())
M = int(stdin.readline())
M_list = map(int, stdin.readline().split())

# 딕셔너리를 이용해 숫자카드의 수를 <키:값>형식으로 구현
dict = dict()
for item in N_list:
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1

# 상근이가 가지고 있는 해당 카드의 수를 공백으로 구분하여 출력
ret = ""
for i in M_list:
    if i not in dict.keys():
        ret += "0 "
    else:
        ret += (str(dict[i]) + ' ')

print(ret)