import sys
input = sys.stdin.readline
for _ in range(int(input())):
    data = list(map(int, input().split()))
    num = data[0]
    score = data[1::]
    avr = sum(score)/num
    result = 0
    for i in range(num):
        if score[i] >avr:
            result+=1
    print("%0.3f%%" % (result/num * 100))