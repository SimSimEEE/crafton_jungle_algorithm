import re
input()
n = re.split(('[^0-9]'), input())
sum = 0
for i in n:
    if i != '':
        sum += int(i)
print(sum)