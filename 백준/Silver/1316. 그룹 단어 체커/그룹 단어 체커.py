result = 0
for _ in range(int(input())):
    word = input()
    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i + 1]:
                continue
            elif word[i] in word[i + 1:]:
                break
        else:
            result += 1
print(result)