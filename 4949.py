from sys import stdin

while True:
    sentence = stdin.readline().rstrip()
    if sentence == ".":
        break

    item_list = []
    for item in sentence:
        if item == "(" or item == "[":
            item_list.append(item)

        elif item == ")":
            if len(item_list) == 0:
                print("no")
                break
            if item_list.pop() != "(":
                print("no")
                break
        elif item == "]":
            if len(item_list) == 0:
                print("no")
                break
            if item_list.pop() != "[":
                print("no")
                break
        elif item == ".":
            if len(item_list) == 0:
                print("yes")
            else:
                print("no")
            break

