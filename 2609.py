# 본 문제는 유클리 호제법을 활용한 알고리즘을 사용함!
# 최대공약수 함수
def get_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


# 최소공배수 함수
def get_lcm(n1, n2, n3):
    return (n1 * n2) // n3


# 두 수 입력받기
x, y = map(int, input().split())
ret_gcd = get_gcd(x, y)
ret_lcm = get_lcm(x, y, ret_gcd)

print(f"{ret_gcd}\n{ret_lcm}")

# 시간초과
# # 최대공약수 구하기
# for i in range(min(x, y)+1, 0, -1):
#     if x%i == 0 and y%i == 0:
#         print(i)
#         break
#
# # 최소공배수 구하기
# for i in range(max(x, y), x*y+1):
#     if i%x == 0 and i%y == 0:
#         print(i)
#         break

