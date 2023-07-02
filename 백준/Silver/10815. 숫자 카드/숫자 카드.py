n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
m_nums = list(map(int, input().split()))

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return 0

for m in m_nums:
    print(binary_search(cards, m),end=" ")
print()