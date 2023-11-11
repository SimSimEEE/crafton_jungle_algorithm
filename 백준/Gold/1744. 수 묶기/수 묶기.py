result = 0
plus, minus = [], []
for _ in range(int(input())):
    n = int(input())
    if n > 1:
        plus.append(n)
    elif n <= 0:
        minus.append(n)
    else:
        result += n
        
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        result += plus[i] * plus[i + 1]
    else:
        result += plus[i]
        
for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        result += minus[i] * minus[i + 1]
    else:
        result += minus[i]
        
print(result)