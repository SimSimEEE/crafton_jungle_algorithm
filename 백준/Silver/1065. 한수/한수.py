import sys
input = sys.stdin.readline
N = int(input())
result = 0
if N < 100:
    print(N)
else :
    result = 99
    for i in range(100, N+1):
        if i//100+i%10 == 2*(i//10%10):
            result += 1
    print(result)