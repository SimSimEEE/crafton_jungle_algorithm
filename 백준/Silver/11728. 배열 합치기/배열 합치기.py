input()
A = input().split()
B = input().split()
print(*sorted(map(int, A + B)))