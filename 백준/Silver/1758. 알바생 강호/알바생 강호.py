import sys
input = sys.stdin.readline

n = int(input())

people = [int(input()) for _ in range(n)]
people.sort(key=lambda x: -x)

answer = 0

for i, e in enumerate(people):
    if e > i:
        answer += e - i

print(answer)