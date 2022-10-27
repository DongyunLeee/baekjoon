from collections import defaultdict


# 제거한 노드와 그 자식노드들을 모두 -1 처리하여 리프노드 계산에서 제외하여 처리함
# DFS 알고리즘을 이용하여 재귀를 이용하여 풀이 진행
def leaf_node(item):
    global count_leaf
    if Tree[item] == []:
        count_leaf += 1

    elif -1 not in Tree[item]:
        for target in Tree[item]:
            leaf_node(target)


N = int(input())
node = list(map(int, input().split()))
rm_ndoe = int(input())

Tree = defaultdict(list)
for x, y in enumerate(node):
    if y == -1:
        start = x

    if -1 in Tree[y] or x == rm_ndoe:
        Tree[x].append(-1)
        continue

    Tree[y].append(x)

global count_leaf
count_leaf = 0
leaf_node(start)

print(count_leaf)
