n = int(input())
postfix = input()
postfix_list = list(postfix)
for i in range(n):
    num = int(input())
    for idx, e in enumerate(postfix_list):
        if e == chr(i + 65):
            postfix_list[idx] = str(num)
            
stack = []
for e in postfix_list:
    if e.isdigit():
        stack.append(int(e))
    else:
        a, b = float(stack.pop()), float(stack.pop())
        stack.append(eval(str(b) + e + str(a)))

print('%.2f' % stack.pop())