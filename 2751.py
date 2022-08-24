import sys

# 수의 개수 입력
N = int(sys.stdin.readline())
L = set()

# 수 입력
for i in range(N):
    L.add(int(sys.stdin.readline()))

# 오름차순으로 출력
print('\n'.join(str(i) for i in sorted(L)))