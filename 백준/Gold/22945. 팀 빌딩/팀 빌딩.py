n = int(input())
programmers = list(map(int, input().split()))
left, right = 0, n - 1
result = 0
while left < right:
    result = max(result, min(
        programmers[left], programmers[right]) * (right - left - 1))
    if programmers[left] < programmers[right]:
        left += 1
    else:
        right -= 1
print(result)