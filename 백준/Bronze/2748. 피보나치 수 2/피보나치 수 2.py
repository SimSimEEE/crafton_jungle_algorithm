import sys
input = sys.stdin.readline

n = int(input())

Fibo = [0,1]

for _ in range(n-1):
    Fibo.append(Fibo[-1] + Fibo[-2])

print(Fibo[n])