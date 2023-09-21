def check_social_distance(place):
    def is_valid(x, y):
        return 0 <= x < 5 and 0 <= y < 5 and place[x][y] == 'P'

    def has_no_adjacent_person(x, y):
        for dx, dy in d1:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                return False
        return True

    def has_no_diagonal_person(x, y):
        for dx, dy in d2:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                if place[new_x][y] != 'X' or place[x][new_y] != 'X':
                    return False
        return True

    def has_no_distant_person(x, y):
        for dx, dy in d3:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                mid_x, mid_y = x + dx // 2, y + dy // 2
                if place[mid_x][mid_y] != 'X':
                    return False
        return True

    d1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    d3 = [(2, 0), (0, 2), (-2, 0), (0, -2)]

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not has_no_adjacent_person(i, j) or not has_no_diagonal_person(i, j) or not has_no_distant_person(i, j):

                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if check_social_distance(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
