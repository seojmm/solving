import sys
input = sys.stdin.readline

T = int(input())
while(T):
    sides = {
        'U': [
            ['w', 'w', 'w'],
            ['w', 'w', 'w'],
            ['w', 'w', 'w']
        ],
        'D': [
            ['y', 'y', 'y'],
            ['y', 'y', 'y'],
            ['y', 'y', 'y']
        ],
        'F': [
            ['r', 'r', 'r'],
            ['r', 'r', 'r'],
            ['r', 'r', 'r']
        ],
        'B': [
            ['o', 'o', 'o'],
            ['o', 'o', 'o'],
            ['o', 'o', 'o']
        ],
        'L': [
            ['g', 'g', 'g'],
            ['g', 'g', 'g'],
            ['g', 'g', 'g']
        ],
        'R': [
            ['b', 'b', 'b'],
            ['b', 'b', 'b'],
            ['b', 'b', 'b']
        ]
    }
    n = int(input())
    order = list(input().rstrip().split())

    for i in range(n):
        if order[i][0] == "L":
            if order[i][1] == "-":
                sides["B"][0][3], sides["B"][1][3], sides["B"][2][3] = sides['U'][0][0], sides['U'][1][0], sides['U'][2][0]
                sides['D'][0][1], sides['D'][1][1], sides['D'][2][1] = sides['B'][0][3], sides['D'][1][3], sides['D'][2][3]
                sides['F'][0][1], sides['F'][1][1], sides['F'][2][1] = sides['D'][0][1], sides['D'][1][1], sides['D'][2][1]
                sides['U'][0][1], sides['U'][1][1], sides['U'][2][1] = sides['F'][0][1], sides['F'][1][1], sides['F'][2][1]

    T -= 1