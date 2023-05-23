import sys
from collections import deque
input = sys.stdin.readline
rot = 0
def sol(arr):
    global rot
    arr = deque(arr)
    for order in orders:
        if order == 'R':
            rot += 1
        else:
            if len(arr) == 0:
                return "error"
            else:
                if rot % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    return list(arr)

for _ in range(int(input())):
    rot = 0
    orders = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    if n == 0 and 'D' in orders:
        print("error")
    else:
        result = sol(arr)
        if result == "error":
            print("error")
        else:
            if rot % 2 == 1:
                result = result[::-1]
            print("[" + ",".join(result) + "]")