import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
A, B = map(int, read().split())
C = int(read())
D = []

for _ in range(N):
    D.append(int(read()))

D.sort(reverse=True)

answer = C / A

for i in range(1, len(D)+1):
    calorie = C + sum(D[0:i])
    price = A + (B * i)

    if calorie / price > answer:
        answer = calorie / price
    else:
        break

print(int(answer))