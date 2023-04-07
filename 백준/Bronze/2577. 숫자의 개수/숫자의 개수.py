import sys
input = sys.stdin.readline
mx = int(input())*int(input())*int(input())
for i in range(10):
    print(str(mx).count(str(i)))