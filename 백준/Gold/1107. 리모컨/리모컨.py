n = int(input())
m = int(input())
broken_buttons = []
if m != 0:
    broken_buttons = list(map(int, input().split()))
if n == 100:
    print(0)
    exit()
if m == 10:
    print(abs(100 - n))
    exit()
buttons = [i for i in range(10)]
for i in broken_buttons:
    buttons.remove(i)
buttons = list(map(str, buttons))
min_cnt = abs(100 - n)
for i in range(1000001):
    for j in range(len(str(i))):
        if str(i)[j] not in buttons:
            break
        elif j == len(str(i)) - 1:
            min_cnt = min(min_cnt, abs(n - i) + len(str(i)))
print(min_cnt)