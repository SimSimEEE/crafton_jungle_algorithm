import sys
input = sys.stdin.readline

def sol(PS):
    result = 0
    median = 1
    stack = []
    for i in range(len(PS)):
        ps = PS[i]
        if ps == '(' or ps == '[':
            median *= 2 + ord(ps) % 2
            stack.append(ps)
        else:
            if not stack:
                return 0
            if ps == ')' and stack[-1] == '(':
                if PS[i-1] == '(':
                    result += median
                    median //= 2
                    stack.pop()
                else:
                    median //= 2
                    stack.pop()
            elif ps == ']' and stack[-1] == '[':
                if PS[i-1] == '[':
                    result += median
                    median //= 3
                    stack.pop()
                else:
                    median //= 3
                    stack.pop()

    if stack:
        return 0
    return result

print(sol(input().rstrip()))