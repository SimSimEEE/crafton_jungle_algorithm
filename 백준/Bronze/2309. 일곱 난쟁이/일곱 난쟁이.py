import sys
input = sys.stdin.readline
n = 9
arr = [int(input()) for _ in range(n)]
arr_sum = sum(arr)
for i in range(n):
    for j in range(i+1, n):
        if arr_sum - (arr[i] + arr[j]) == 100:
            temp1 = arr[i]
            temp2 = arr[j]
 
arr.remove(temp1)
arr.remove(temp2)
 
print('\n'.join(map(str, sorted(arr))))