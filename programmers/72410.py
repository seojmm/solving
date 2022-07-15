def solution(new_id):
    answer = ''

    # step 1
    new_id = new_id.lower()

    # step 2
    for ch in new_id:
        if ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9') or ch == "-" or ch == "_" or ch == ".":
            answer += ch

    # step 3
    tmp = "..............."
    for i in range(15, 1, -1):
        answer = answer.replace(tmp[0:i], ".")

    # step 4
    if len(answer) > 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == ".":
        answer = answer[:-1]

    # step 5
    if len(answer) == 0:
        answer += "a"

    # step 6
    if len(answer) >= 16:
        answer = answer[0:15]
    if len(answer) > 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == ".":
        answer = answer[:-1]

    # step 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer
