import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break

    stack = []
    flag = True

    for ch in s:
        if ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] == "[":
                flag = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif ch == "]":
            if not stack or stack[-1] == "(":
                flag = False
                break
            elif stack[-1] == "[":
                stack.pop()

    if flag == True and not stack:
        print("yes")
    else:
        print("no")
