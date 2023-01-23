import sys
from itertools import combinations

# N을 입력한다.
N = int(sys.stdin.readline())

# 감소하는 수를 저장할 리스트를 등록한다.
nums = list()

# combinations 함수를 사용하여 감소하는 수를 찾아 리스트에 추가한다.
for i in range(1, 11):
    for comb in combinations(range(0,10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str, comb))))

# 감소하는 수를 내림차순으로 정렬한다.
nums.sort()

# 입력한 순번의 감소하는 수가 존재하면 감소하는 수를 출력하고
# 그렇지 못한 경우, -1을 출력한다.
try:
    print(nums[N])
except:
    print(-1)