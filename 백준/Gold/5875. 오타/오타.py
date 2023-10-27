parentheses = input()
n = len(parentheses)
stack = [0] * n

stack[0] = 1 if parentheses[0] == '(' else -1
for i in range(1, n):
    stack[i] = stack[i - 1] + 1 if parentheses[i] == '(' else stack[i - 1] - 1


cnt = 0
if stack[-1] == -2:
    for i in range(1, n - 1):
        if stack[i] == -1:
            print(cnt + 1)
            break
        elif parentheses[i] == ')':
            cnt += 1
else:
    for i in range(n):
        if stack[i] == 1:
            cnt = 0
        elif parentheses[i] == '(':
            cnt += 1
    print(cnt)
