def make(start, end, layer):
    if layer == 7:
        return 1

    mid = (start + end) // 2
    for i in range(start, mid + 1):
        monkeys[layer][i] = 'A'
    for i in range(mid + 1, end + 1):
        monkeys[layer][i] = 'B'
    return make(start, mid, layer + 1) + make(mid + 1, end, layer + 1)

N = int(input())
monkeys = [['A'] * N for _ in range(7)]
sb = ['A'] * N

cnt = make(0, N - 1, 0)

for i in range(7):
    str_monkey = ''.join(monkeys[i])
    if str_monkey == ''.join(sb):
        str_monkey = str_monkey[1:] + 'B'
    print(str_monkey)
