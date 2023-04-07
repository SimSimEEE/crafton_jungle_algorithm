import sys
input = sys.stdin.readline
N = input().strip()
for i in range(1, 10):
    print(N+" * "+str(i)+" = "+str(int(N)*i))