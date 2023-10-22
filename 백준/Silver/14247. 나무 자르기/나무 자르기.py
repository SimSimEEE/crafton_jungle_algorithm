n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))
trees = list(zip(h, a))
result = 0
for day, (h, a) in enumerate(sorted(trees, key=lambda x: x[1])):
    result += h + a * day
print(result)