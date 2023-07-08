length, width, height = map(int, input().split())
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]

total_count = 0
total_volume = 0

for size, count in cubes[::-1]:
    total_volume *= 8
    cube_count = min(count, (length // (2 ** size)) * (width // (2 ** size)) * (height // (2 ** size)) - total_volume)
    total_count += cube_count
    total_volume += cube_count

if(total_volume == length*width*height):
    print(total_count)
else:
    print(-1)