dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def possible(puzzle, match_puzzle):
    for _ in range(4):
        match_puzzle = [list(reversed(i)) for i in zip(*match_puzzle)]
        if puzzle == match_puzzle:
            return True
    return False


def matching_puzzle(puzzle, puzzle_length, puzzle_dict, answer):
    match_puzzles = puzzle_dict[puzzle_length]
    for match_puzzle in match_puzzles:
        if possible(puzzle, match_puzzle):
            answer += puzzle_length
            puzzle_dict[puzzle_length].remove(match_puzzle)
            return answer, puzzle_dict
    return answer, puzzle_dict


def change_puzzle(puzzle):
    puzzle_length = len(puzzle)
    min_x, min_y, max_x, max_y = 100, 100, 0, 0
    for p in range(puzzle_length):
        if puzzle[p][0] < min_x:
            min_x = puzzle[p][0]
        if puzzle[p][0] > max_x:
            max_x = puzzle[p][0]
        if puzzle[p][1] < min_y:
            min_y = puzzle[p][1]
        if puzzle[p][1] > max_y:
            max_y = puzzle[p][1]

    for q in range(puzzle_length):
        puzzle[q][0] -= min_x
        puzzle[q][1] -= min_y

    puzzle_map = [[0] * (max_y - min_y + 1) for _ in range((max_x - min_x + 1))]
    for a, b in puzzle:
        puzzle_map[a][b] = 1
    return puzzle_map, puzzle_length


def find_puzzle(x, y, visited, flag, board):
    board_length = len(board)
    visited[x][y] = 1
    stack = [[x, y]]
    puzzle = [[x, y]]
    while stack:
        x, y = stack.pop()
        for d in range(4):
            next_x, next_y = x + dx[d], y + dy[d]
            if 0 <= next_x < board_length and 0 <= next_y < board_length:
                if not visited[next_x][next_y] and board[next_x][next_y] == flag:
                    stack.append([next_x, next_y])
                    puzzle.append([next_x, next_y])
                    visited[next_x][next_y] = 1
    return visited, puzzle


def table_puzzle(table, puzzle_dict):
    table_length = len(table)
    visit_table = [[0] * table_length for _ in range(table_length)]
    puzzles = []
    for i in range(table_length):
        for j in range(table_length):
            if table[i][j] == 1 and not visit_table[i][j]:
                visit_table, puzzle = find_puzzle(i, j, visit_table, 1, table)
                puzzles.append(puzzle)

    for puzzle in puzzles:
        puzzle_map, puzzle_length = change_puzzle(puzzle)
        puzzle_dict[puzzle_length].append(puzzle_map)
    return puzzle_dict


def solution(game_board, table):
    answer = 0
    puzzle_dict = {}
    for m in range(1, 7):
        puzzle_dict[m] = []
    puzzle_dict = table_puzzle(table, puzzle_dict)
    board_length = len(game_board)
    visit_board = [[0] * board_length for _ in range(board_length)]
    for i in range(board_length):
        for j in range(board_length):
            if game_board[i][j] == 0 and not visit_board[i][j]:
                visit_board, puzzle = find_puzzle(i, j, visit_board, 0, game_board)
                puzzle, puzzle_length = change_puzzle(puzzle)
                answer, puzzle_dict = matching_puzzle(puzzle, puzzle_length, puzzle_dict, answer)
    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))


print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
               [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 0, 1, 1, 0], [1, 1, 0, 0, 0]]))

