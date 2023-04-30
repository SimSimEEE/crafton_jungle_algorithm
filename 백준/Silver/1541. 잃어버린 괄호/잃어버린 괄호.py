expressions = list(input().split('-'))
result_arr = []
for ex_divided_by_sub in expressions:
    ex_divided_by_add = ex_divided_by_sub.split('+')
    result_by_add = 0
    for digit in ex_divided_by_add:
        result_by_add += int(digit)
    result_arr.append(result_by_add)
result = result_arr[0]
for i in range(1, len(result_arr)):
    result -= result_arr[i]
print(result)