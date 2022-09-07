from sys import stdin
N = int(stdin.readline())
A = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
ML = list(map(int, stdin.readline().split()))

ret = ""
for item in ML:
    if item in A:
        ret += "1\n"
    else:
        ret += "0\n"

print(ret)