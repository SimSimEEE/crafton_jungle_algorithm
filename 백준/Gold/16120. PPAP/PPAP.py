str_ppap = input()
stack = []
ppap = ["P","P","A","P"]
for char_ppap in str_ppap:
    stack.append(char_ppap)
    if stack[-4:] == ppap:
        for _ in range(3):
            stack.pop()
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")