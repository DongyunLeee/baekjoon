# 시간초과
# # 입력된 조건의 집에 거주민 수를 구하는 함수
# def get_result(k, n):
#         if k == 0:
#             return n
#         elif n == 1:
#             return 1
#         else:
#             return get_result(n-2, k+2) + get_result(k, n-1)

# 거주민 수를 구하는 함수
def get_result(k, n):
    result = []
    for i in range(n+1):
        result.append(i)

    for i in range(k):
        for j in range(1, n+1):
            result[j] += result[j-1]

    return result[n]


# 테스트케이스 수를 입력받음
T = int(input())

# 층과 호수를 입력받아 거주민 수를 출력
for i in range(T):
    k = int(input())
    n = int(input())

    print(get_result(k, n))