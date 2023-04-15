import sys
nums = []
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    if n:
        nums.append(n)
    else:
        nums.pop()
print(sum(nums))