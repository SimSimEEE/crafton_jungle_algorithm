n, h, w = map(int, input().split())
ln = n
result = ['?'] * ln
for _ in range(h):
    word = input()
    for i, e in enumerate(word):
        if e != '?':
            result[i//w] = e
print(''.join(result))