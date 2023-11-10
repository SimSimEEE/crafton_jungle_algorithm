word = input()
start = ord('A')
result = 0
for i in word:
    distance = min(abs(start - ord(i)), abs(start - ord(i) + 26), abs(start - ord(i) - 26))
    result += distance
    start = ord(i)
print(result)