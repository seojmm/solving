def solution(numbers, hand):
    answer = ''
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2],
    }
    l, r = keypad['*'], keypad['#']

    for next in numbers:
        if next in [1, 4, 7]:
            l = keypad[next]
            answer += 'L'
        elif next in [3, 6, 9]:
            r = keypad[next]
            answer += 'R'
        else:
            lDist = abs(l[0] - keypad[next][0]) + abs(l[1] - keypad[next][1])
            rDist = abs(r[0] - keypad[next][0]) + abs(r[1] - keypad[next][1])

            if lDist < rDist:
                l = keypad[next]
                answer += 'L'
            elif lDist > rDist:
                r = keypad[next]
                answer += 'R'
            else:
                if hand == "left":
                    l = keypad[next]
                    answer += 'L'
                else:
                    r = keypad[next]
                    answer += 'R'

    return answer
