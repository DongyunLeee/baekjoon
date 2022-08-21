# 런타임 에러 발생
# # 팩토리얼 함수 구현(재귀)
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)

# 팩토리얼 함수 구현(반복문)
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i

    return result


# N, K 입력
N, K = map(int, input().split())

# 이항계수 계산 및 출력
ret = factorial(N) // (factorial(K) * factorial(N-K))
print(ret)
