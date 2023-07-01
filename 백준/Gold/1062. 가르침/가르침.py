import re
from itertools import combinations

n, k = map(int, input().split())
alphabet_set = set()
words = [input() for _ in range(n)]
pattern = "[a,c,t,n,i]"
result = 0

if k < 5:
    print(0)
else:
    filtered_words = []
    k -= 5

    for word in words:
        word = re.sub(pattern, "", word)
        if not word:
            result += 1
        else:
            alphabet_set |= set(word)
            filtered_words.append(word)
    if len(alphabet_set) <= k:
        print(n)
        
    else:
        nCr = combinations(alphabet_set, k)
        max_count = 0

        for combination in nCr:
            count = 0
            for word in filtered_words:
                for letter in combination:
                    word = word.replace(letter, "")
                if not word:
                    count += 1
            max_count = max(max_count, count)

        result += max_count
        print(result)