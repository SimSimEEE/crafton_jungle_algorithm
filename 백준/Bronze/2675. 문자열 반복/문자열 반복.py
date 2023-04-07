import sys
input = sys.stdin.readline
for _ in range(int(input())):
    t,s = input().split()
    for i in s:
        print(i*int(t),end="")
    print()