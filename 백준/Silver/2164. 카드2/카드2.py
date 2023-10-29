N = int(input())
card = list(range(1,N+1))
while len(card) != 1:
    ln = len(card)
    del card[0::2]
    if ln%2 == 1:
        card.append(card.pop(0))
print(*card)