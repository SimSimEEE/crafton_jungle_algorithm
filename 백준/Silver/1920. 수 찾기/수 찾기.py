N = int(input())
A = set(map(int,input().split()))
M = int(input())
for B in list(map(int,input().split())):
    if B in A:
        print(1)
    else:
        print(0)