# 알파벳 소문자 리스트 라이브러리 #
from string import ascii_lowercase

# 입력 #
S = input()

# 각 알파벳 포함 여부 및 위치 출력 #
for alpa in list(ascii_lowercase):
    if S.count(alpa):
        print(S.index(alpa), end=' ')
    else:
        print(-1, end=' ')