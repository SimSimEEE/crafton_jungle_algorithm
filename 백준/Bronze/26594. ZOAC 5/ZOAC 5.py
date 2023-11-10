word = input()
result = 1
start = word[0]
for i in range(1, len(word)):
    if start == word[i]:
        result += 1
    else:
        break
print(result)