import sys
input = sys.stdin.readline

def sol(PS):
    stack = []
    for ps in PS:
        if ps == '(':
            stack.append(ps)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

for _ in range(int(input())):
    if sol(input().strip()):
        print("YES")
    else:
        print("NO")