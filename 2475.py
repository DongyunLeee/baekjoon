# 입력 받은 후, int 자료형으로 맵핑 #
num = map(int, input().split(' '))
result = 0

# 각 입력된 수의 제곱값의 합 구하기 #
for n in num:
    result += n ** 2

# 제곱값의 합에 10을 나눈 나머지 출력 #
result %= 10
print(result)