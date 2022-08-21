# r, M 선언
r = 31
M = 1234567891

# 문자열 길이 선언
L = int(input())

# 문자열 입력 및 소문자 변환(모든 입력문자는 소문자)
T = input().lower()
ret = 0

# 해시값 계산
for i in range(L):
    ret += (ord(T[i])-96) * (r**i)

# 해시값 출력
print(ret%M)