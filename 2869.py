from sys import stdin
from math import ceil

# 이동거리(A), 미끄러지는거리(B), 목표높이(V) 입력
A, B, V = map(int, stdin.readline().split())

# 목표높이까지 걸리는 기간 계산
ret = ceil((V-A)/(A-B)) + 1

print(ret)