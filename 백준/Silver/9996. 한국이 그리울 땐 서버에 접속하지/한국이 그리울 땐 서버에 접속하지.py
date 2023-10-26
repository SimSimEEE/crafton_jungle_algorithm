n = int(input())
pattern = input().split("*")
for _ in range(n):
    word = input()
    if word.startswith(pattern[0]) and word.endswith(pattern[1]) and len(word) >= len(pattern[0]) + len(pattern[1]):
        print("DA")
    else:
        print("NE")