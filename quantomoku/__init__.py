# from qiskit import *


def calculate_score(board_matrix, player_char):
    """Calculate how many five line-ups there are in a board for a given player"""

    N = len(board_matrix)  # N rows
    M = len(board_matrix[0])  # M columns

    # Utility to check if everything is equal
    check_equal = lambda x: sum([k == player_char for k in x]) == 5

    # Utility to check if a cell (x, y) is valid
    is_valid = lambda x, y: (0 <= x < N) and (0 <= y < M)

    score = 0

    relative_pairs = [
        [(i, 0) for i in range(5)],  # horizontal
        [(0, i) for i in range(5)],  # vertical
        [(i, i) for i in range(5)],  # diagonal \
        [(-i, i) for i in range(5)],  # diagonal /
    ]
    print(relative_pairs)

    for x in range(N):
        for y in range(N):
            for direction in relative_pairs:
                cells = []
                for dx, dy in direction:
                    cell_x = x + dx
                    cell_y = y + dy
                    if is_valid(cell_x, cell_y):
                        cells.append(board_matrix[cell_x][cell_y])
                    else:
                        break
                score += check_equal(cells)

    return score
