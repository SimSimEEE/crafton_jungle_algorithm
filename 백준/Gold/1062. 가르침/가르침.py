import re

def backtrack(count, start_idx):
    global max_count
    if count == k:
        temp_count = count_words(filtered_words, visited)
        max_count = max(max_count, temp_count)
        return

    for i in range(start_idx, 26):
        if not visited[i]:
            visited[i] = True
            backtrack(count + 1, i)
            visited[i] = False

def count_words(words, visited):
    temp_count = 0
    for word in words:
        for letter in word:
            if not visited[ord(letter) - ord('a')]:
                break
        else:
            temp_count += 1
    return temp_count

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
        visited = [False] * 26
        visited[ord('a') - ord('a')] = True
        visited[ord('c') - ord('a')] = True
        visited[ord('t') - ord('a')] = True
        visited[ord('n') - ord('a')] = True
        visited[ord('i') - ord('a')] = True

        max_count = 0
        backtrack(0, 0)

        result += max_count
        print(result)