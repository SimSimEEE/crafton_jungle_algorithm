import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
shoot = sorted(list(map(int, input().split())))
animal = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for animal_x, animal_y in animal:
    start = 0
    end = M - 1
    while start < end:
        mid = (start + end) // 2
        if animal_x > shoot[mid]:
            start = mid + 1
        else:
            end = mid
    if abs(animal_x-shoot[end]) <= L - animal_y:
            cnt += 1

print(cnt)
