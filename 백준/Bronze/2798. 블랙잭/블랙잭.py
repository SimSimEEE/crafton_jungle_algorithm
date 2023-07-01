import itertools
result = 0
N,M = map(int,input().split())
cards = list(map(int,input().split()))
nCr = itertools.combinations(cards, 3)
for card in nCr:
    if sum(card) <= M:
        result = max(result,sum(card))
print(result)
