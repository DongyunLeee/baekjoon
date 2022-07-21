# 입력 후, int 자료형으로 매핑 #
A, B = map(int, input().split(' '))

# 입력 값을 문자열로 변환하여 reverse 후 int형으로 저장 #
A = int(str(A)[::-1])
B = int(str(B)[::-1])

# 둘중 최대값 출력 #
print(max(A, B))