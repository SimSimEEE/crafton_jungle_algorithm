nums = set()
num_list = []
for _ in range(int(input())):
    n = int(input())
    nums.add(n)
    num_list.append(n)
max_cnt = 0
for n in nums:
    new_num = [i for i in num_list if i != n]
    cnt = 1
    for i in range(1, len(new_num)):
        if new_num[i] == new_num[i - 1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)