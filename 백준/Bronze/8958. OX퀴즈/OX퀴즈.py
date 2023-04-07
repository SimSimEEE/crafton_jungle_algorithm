import sys
input = sys.stdin.readline
for _ in range(int(input())):
    Q = input().rstrip().split('X')
    score = 0
    for q in Q:
        score += sum(range(0,len(q)+1))
    print(score)