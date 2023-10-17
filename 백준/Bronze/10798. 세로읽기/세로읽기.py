words = [] * 5
for i in range(5):
    word = input()
    for j in range(len(word)):
        if len(words) <= j:
            words.append('')
        words[j] += word[j]
print("".join(words))
