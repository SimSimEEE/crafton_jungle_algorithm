str_ppap = input()
stack = []
ppap = ["P","P","A","P"]
for i in range(len(str_ppap)):
    stack.append(str_ppap[i])
    if stack[-4:] == ppap:
        for _ in range(3):
            stack.pop()
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")