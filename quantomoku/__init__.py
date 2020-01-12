from qiskit import Aer, ClassicalRegister, execute, QuantumCircuit, QuantumRegister


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


def is_full(board):
    """Returns True if there are no empty cells"""
    for row in board:
        for cell in row:
            if cell == "n":
                return False  # foudn empty cell, not full

    return True


def get_winner(board):
    """Returns "x", "o", "tie", or "none" """
    relative_score = calculate_score(board, "x") - calculate_score(board, "o")

    if relative_score > 0:
        return "x"  # more Xs five line-ups than Os, X wins
    elif relative_score < 0:
        return "o"  # mirror case

    # Board is full is a tie
    if is_full(board):
        return "tie"
    else:
        return "none"


def get_max_component(board):
    """Return the number for the next cell_{component}"""
    max_comp = 0
    for row in board:
        for cell in row:
            if "_" in cell:
                cell_comp = int(cell.split("_")[-1])
                if cell_comp + 1 >= max_comp:
                    max_comp = cell_comp + 1
    return max_comp


def check_invalid(board, selected_cells, player_char):
    """Return if a move is invalid, and give appropriate error message"""
    if len(selected_cells) == 0:
        return (True, "You must select a cell to play for your movement!")
    elif len(selected_cells) > 2:
        return (True, "Too many cells were selected!")

    # Check for movements that play with measured cells
    for x, y in selected_cells:
        if board_matrix[x][y] in ["o", "x"]:
            return (True, "Measured cells cannot be selected!")

    # Check if trying to entangle with cell of the same type
    for x, y in selected_cells:
        if "_" in board_matrix[x][y] and board_matrix[x][y][0] == player_char:
            return (True, "You cannot entangle with your own lonely cell!")

    # Check if trying to entangle with entangled cell
    for x, y in selected_cells:
        if board_matrix[x][y][0] == "q":
            return (True, "You cannot entangle with the entangled cell!")

    return (False, "")


def update_board(board, selected_cells, player_char):
    if len(selected_cells) == 1:
        x, y = selected_cells[0]  # classical move
        board[x][y] = player_char
    else:
        """Not implemented yet"""
        pass


def process_board(game_state):
    """Given a dictionary of the game_state containing the keys:

    - board: 2d matrix representation of the board state
    - player_turn: "x" or "o", the player that played
    - selected_cells: list of the coordinates of the cells
    - measurement_turn: an integer from 0 to 4, indicating how many turns until global measurement

    Returns a dictionary containing the following keys:
    - board: updated 2d matrix representation of the board state
    - player_turn: next player to play, "x" or "o"
    - winner: "x", "o", "tie" or None
    - invalid: True if the move was not valid, False otherwise
    - invalid_message: message explaining why the movement is invalid
    - measurement_turn: an integer from 0 to 4, indicating how many turns until global measurement
    """

    board = game_state["board"]
    player_turn = game_state["player_turn"]
    selected_cells = game_state["selected_cells"]
    measurement_turn = game_state["measurement_turn"]

    invalid, invalid_message = check_invalid(board, selected_cells, player_turn)

    # Invalid movement: same player must play again
    if invalid:
        return {
            "board": board,
            "player_turn": player_turn,
            "winner": get_winner(board),
            "invalid": invalid,
            "invalid_message": invalid_message,
            "measurement_turn": measurement_turn,
        }

    update_board(board, selected_cells, player_turn)  #  do movement

    next_turn = "x" if player_turn == "o" else "o"
    next_measurement = (measurement_turn + 1) % 5

    return {
        "board": board,
        "player_turn": next_turn,
        "winner": get_winner(board),
        "invalid": invalid,
        "invalid_message": invalid_message,
        "measurement_turn": next_measurement,
    }
