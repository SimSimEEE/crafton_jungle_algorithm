import sys
input = sys.stdin.readline


N, K = map(int, input().split())
numbers = input().rstrip()
stack, k = [], K

for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k-=1
    stack.append(number)

print(''.join(stack[:N-K]))