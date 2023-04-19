import sys
input = sys.stdin.readline

N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]
coordinates.sort()

def get_coordinate_distance(first, second):
    return (first[0]-second[0])**2 + (first[1]-second[1])**2

def get_min_distance(coordinates):
    n = len(coordinates)
    if n == 1:
        return sys.maxsize
    if n == 2:
        return get_coordinate_distance(coordinates[0],coordinates[-1])
    min_distance = min(get_min_distance(coordinates[:n//2]),get_min_distance(coordinates[n//2:]))

    coordinates = [i for i in coordinates if (i[0]-coordinates[n//2][0])**2 < min_distance ]
    coordinates.sort(key=lambda x:x[1])

    for i in range(len(coordinates)-1):
        for j in range(i+1,len(coordinates)):
            if (coordinates[i][1] - coordinates[j][1])**2 < min_distance:
                min_distance = min(min_distance, get_coordinate_distance(coordinates[i], coordinates[j]))
            else:
                break
    return min_distance

print(get_min_distance(coordinates))