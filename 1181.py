# 입력할 단어의 수 입력
N = int(input())

# 2안
# 단어를 저장할 집합 생성
L = set()

# 입력된 단어를 집합에 저장
for i in range(N):
    L.add(input().lower())

# 단어가 저장된 집합 정렬 및 출력
L = sorted(L)
L = sorted(L, key=len)
print('\n'.join(L))


# # 1안 -> 비효율적
# # 단어를 저장할 리스트 생성
# L = []
# for i in range(51):
#     L.append([])
#
# # 단어 입력 후, 리스트에 저장
# for i in range(N):
#     T = input().lower()
#     if L[len(T)].count(T) < 1:
#         L[len(T)].append(T)
#
# # 리스트 정렬 후, 출력
# for i in L:
#     i.sort()
#     for j in i:
#         print(j)