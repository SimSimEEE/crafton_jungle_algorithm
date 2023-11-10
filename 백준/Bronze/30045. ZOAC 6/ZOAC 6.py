result = 0
for _ in range(int(input())):
    word = input()
    if "01" in word or "OI" in word:
        result += 1
print(result)