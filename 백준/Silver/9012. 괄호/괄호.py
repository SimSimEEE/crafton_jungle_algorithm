for i in range(int(input())):
    PS = input()
    while len(PS) != len(PS.replace("()","")):
        PS = PS.replace("()","")
    if len(PS) == 0:
        print("YES")
    else:
        print("NO")