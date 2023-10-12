n = int(input())
file_list = [input() for _ in range(n)]

file_set = {}
for file in file_list:
    extension = file.split('.')[1]
    if extension in file_set:
        file_set[extension] += 1
    else:
        file_set[extension] = 1

for ext, count in sorted(file_set.items()):
    print(f"{ext} {count}")