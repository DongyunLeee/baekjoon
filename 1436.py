from sys import stdin

# 입력값 입력(N번째 종말)
N = int(stdin.readline())

# N번째 종말의 숫자 구하기
# 브루트 포스(완전탐색) 알고리즘 사용
ret = 665
while N:
    ret += 1
    if "666" in str(ret):
        N -= 1

print(ret)
