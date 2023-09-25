from collections import deque

def rotate_square(puzzle_table):
    row_size = len(puzzle_table)
    col_size = len(puzzle_table[0])
    rotated_matrix = [[0] * row_size for _ in range(col_size)]

    for row_idx in range(row_size):
        for col_idx in range(col_size):
            rotated_matrix[col_idx][row_idx] = puzzle_table[row_size - 1 - row_idx][col_idx]

    return rotated_matrix

def is_matched(puzzle_table, rotated_matrix):
    if len(puzzle_table) != len(rotated_matrix) or len(puzzle_table[0]) != len(rotated_matrix[0]):
        return False

    for row_idx in range(len(puzzle_table)):
        if puzzle_table[row_idx] != rotated_matrix[row_idx]:
            return False

    return True

def make_moved_square(square_points, table_type, origin_board_map, puzzle_table_map):
    min_row = min(square_points, key=lambda x: x[0])[0]
    min_col = min(square_points, key=lambda x: x[1])[1]

    row_size = max(square_points, key=lambda x: x[0])[0] - min_row + 1
    col_size = max(square_points, key=lambda x: x[1])[1] - min_col + 1

    game_board = [[0] * col_size for _ in range(row_size)]

    for point in square_points:
        row, col = point
        game_board[row - min_row][col - min_col] = 1

    if table_type == 0:
        origin_board_list = origin_board_map.get(len(square_points), [])
        origin_board_list.append(game_board)
        origin_board_map[len(square_points)] = origin_board_list
    else:
        puzzle_table_list = puzzle_table_map.get(len(square_points), [])
        puzzle_table_list.append(game_board)
        puzzle_table_map[len(square_points)] = puzzle_table_list

def bfs(start_row_idx, start_col_idx, find_value, puzzle_table, visited, queue, dx, dy, origin_board_map, puzzle_table_map):
    square_points = []
    queue.append([start_row_idx, start_col_idx])
    visited[start_row_idx][start_col_idx] = True
    square_points.append([start_row_idx, start_col_idx])

    while queue:
        cur_row_idx, cur_col_idx = queue.popleft()

        for i in range(4):
            next_row_idx = cur_row_idx + dx[i]
            next_col_idx = cur_col_idx + dy[i]

            if (
                next_row_idx < 0
                or next_row_idx >= len(puzzle_table)
                or next_col_idx < 0
                or next_col_idx >= len(puzzle_table[0])
            ):
                continue

            if visited[next_row_idx][next_col_idx]:
                continue

            if puzzle_table[next_row_idx][next_col_idx] == find_value:
                visited[next_row_idx][next_col_idx] = True
                queue.append([next_row_idx, next_col_idx])
                square_points.append([next_row_idx, next_col_idx])

    if find_value == 0:
        make_moved_square(square_points, 0, origin_board_map, puzzle_table_map)
    else:
        make_moved_square(square_points, 1, origin_board_map, puzzle_table_map)

def solution(game_board, table):
    answer = 0
    origin_board_map = {}
    puzzle_table_map = {}
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    game_board_visited = [[False] * len(game_board) for _ in range(len(game_board))]
    table_visited = [[False] * len(table) for _ in range(len(table))]
    queue = deque()

    for row_idx in range(len(game_board)):
        for col_idx in range(len(game_board[0])):
            if not game_board_visited[row_idx][col_idx] and game_board[row_idx][col_idx] == 0:
                bfs(row_idx, col_idx, 0, game_board, game_board_visited, queue, dx, dy, origin_board_map, puzzle_table_map)

            if not table_visited[row_idx][col_idx] and table[row_idx][col_idx] == 1:
                bfs(row_idx, col_idx, 1, table, table_visited, queue, dx, dy, origin_board_map, puzzle_table_map)

    for point_cnt in puzzle_table_map.keys():
        for table_puzzle in puzzle_table_map[point_cnt]:
            rotated_puzzle = table_puzzle

            for _ in range(4):
                rotated_puzzle = rotate_square(rotated_puzzle)
                is_find_matched_puzzle = False

                if point_cnt in origin_board_map:
                    for original_matrix in origin_board_map[point_cnt]:
                        if is_matched(original_matrix, rotated_puzzle):
                            answer += point_cnt
                            origin_board_map[point_cnt].remove(original_matrix)
                            is_find_matched_puzzle = True
                            break

                if is_find_matched_puzzle:
                    break

    return answer
