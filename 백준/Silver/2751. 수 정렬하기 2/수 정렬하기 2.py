import sys
num = []
for _ in range(int(input())):
    num.append(int(sys.stdin.readline()))
num.sort()
for i in num:
    print(i)