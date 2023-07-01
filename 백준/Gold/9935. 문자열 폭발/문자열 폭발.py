pstr = input()
bomb = input()

stack = []

for char in pstr:
    stack.append(char)
    if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

result = ''.join(stack)

if result == "":
    print("FRULA")
else:
    print(result)