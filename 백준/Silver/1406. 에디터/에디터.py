import sys

pstr = input()
ptr = len(pstr)
left_stack = list(pstr)
right_stack = []

for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd == 'B':
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[2])

result = ''.join(left_stack + right_stack[::-1])
print(result) 