import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def func(preorder, inorder):
    if not inorder:
        return

    node = preorder.pop(0)  # preorder[0]은 root
    nodeIdx = inorder.index(node)

    func(preorder, inorder[:nodeIdx])
    func(preorder, inorder[nodeIdx+1:])
    print(node, end=" ")


T = int(input())

while T:
    n = int(input())

    preorder = list(map(int, input().rstrip().split()))
    inorder = list(map(int, input().rstrip().split()))

    func(preorder, inorder)
    print()

    T -= 1
