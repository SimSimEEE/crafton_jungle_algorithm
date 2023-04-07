import sys
input = sys.stdin.readline
result = 0
index = 0
for i in range(9):
    n = int(input())
    if n > result:
        result = n
        index = i+1
print(result)
print(index)