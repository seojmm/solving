import sys

input = sys.stdin.readline

if __name__ == '__main__':
    S = 0b0
    M = int(input())
    for _ in range(M):
        line = input().strip()
        try:
            command, x = line.split()
            x = int(x)
            if command == "add":
                S = S | (0b1 << x)
            elif command == "remove":
                S = S & ~(0b1 << x)
            elif command == "check":
                if S & (0b1 << x):
                    print(1)
                else:
                    print(0)
            elif command == "toggle":
                S = S ^ (0b1 << x)
        except:
            if line == "all":
                S = 0b111111111111111111111
            elif line == "empty":
                S = 0b0


