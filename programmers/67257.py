def permutation(arr, n):
    ret = []

    if n > len(arr):
        return ret
    if n == 1:
        for e in arr:
            ret.append([e])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in permutation(ans, n-1):
                ret.append([arr[i]] + p)

    return ret


def operate(a, b, op):
    if op == "+":
        return str(int(a) + int(b))
    if op == "-":
        return str(int(a) - int(b))
    if op == "*":
        return str(int(a) * int(b))


def calculate(exp, order):
    array = []
    tmp = ""
    for ch in exp:
        if ch.isdigit():
            tmp += ch
        else:
            array.append(tmp)
            array.append(ch)
            tmp = ""
    array.append(tmp)

    for op in order:
        stack = []
        while array:
            tmp = array.pop(0)
            if tmp == op:
                stack.append(operate(stack.pop(), array.pop(0), op))
            else:
                stack.append(tmp)
        array = stack

    return abs(int(array[0]))


def solution(expression):
    list_ans = []
    orders = permutation(["+", "-", "*"], 3)
    for order in orders:
        list_ans.append(abs(calculate(expression, order)))

    return max(list_ans)


print(solution("100-200*300-500+20"))
