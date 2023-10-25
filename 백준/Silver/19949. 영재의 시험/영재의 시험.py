from itertools import product
nums = list(map(int, input().split()))
answer = 0
for i in product(range(1, 6), repeat=len(nums)):
    result = 0
    for j in range(len(i)):
        if j > 1:
            if (i[j - 2] == i[j - 1] == i[j]):
                break
        if i[j] == nums[j]:
            result += 1
    else:
        if result >= 5:
            answer += 1
print(answer)
