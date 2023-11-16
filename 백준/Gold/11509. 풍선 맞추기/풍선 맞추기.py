n = int(input())
h = list(map(int, input().split()))
result = 0
arrow = []
for i in h:
    if i not in arrow:
        result += 1
        arrow.append(i-1)
    else:
        arrow.remove(i)
        arrow.append(i-1)
print(result)