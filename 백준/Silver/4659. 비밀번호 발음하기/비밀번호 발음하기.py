while True:
    word = input()
    if word == "end":
        break

    is_acceptable = True
    consecutive_vowels = 0
    consecutive_consonants = 0
    prev_char = None

    for char in word:
        if char in 'aeiou':
            consecutive_vowels += 1
            consecutive_consonants = 0

            if consecutive_vowels >= 3 or (consecutive_vowels == 2 and char == prev_char and char not in ['e', 'o']):
                is_acceptable = False
                break
        else:
            consecutive_consonants += 1
            consecutive_vowels = 0

            if consecutive_consonants >= 3 or (consecutive_consonants == 2 and char == prev_char):
                is_acceptable = False
                break

        prev_char = char

    if is_acceptable and len(word) != consecutive_consonants:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
