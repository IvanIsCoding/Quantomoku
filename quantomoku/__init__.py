import os

try:
    from qiskit import Aer, ClassicalRegister, execute, QuantumCircuit, QuantumRegister

    found_qiskit = True
except ModuleNotFoundError:
    found_qiskit = False
except ImportError:
    found_qiskit = False


def decode_bitstring(bitstring):
    """Recover the Xs, Os and Ns from a bit string"""

    conversion = {"00": "n", "10": "x", "01": "o", "11": "n"}

    answer = []

    for i in range(len(bitstring), 2):
        bit_pair = bitstring[i] + bitstring[i + 1]
        answer.append(conversion[bit_pair])

    return answer

def get_circuit_result(backend, circuit):
    """Given a circuit, executes it one time and gets the measurement"""
    job = execute(circuit, backend=backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    return list(counts.keys())[0]    

def handle_measurement(component):
    """Given a component, return the measurements for it"""
    sorted_symbols = sorted(component)

    symbol_case = [x[0] for x in sorted_symbols]

    N = len(component) * 2

    circuit = QuantumCircuit(QuantumRegister(N), ClassicalRegister(N))

    # Discover which circuit to build
    if symbol_case == ["x"]:
        circuit.x(0)
    elif symbol_case == ["o"]:
        circuit.x(1)
    elif symbol_case == ["q", "q"]:
        circuit.h(0)
        circuit.x(1)
        circuit.cx(0, 1)
        circuit.cx(0, 3)
        circuit.cx(1, 2)
    elif symbol_case == [">", ">"]:
        circuit.h(0)
        circuit.x(2)
        circuit.cx(0, 2)
    elif symbol_case == ["(", "("]:
        circuit.h(1)
        circuit.x(3)
        circuit.cx(1, 3)

    circuit.measure(
        list(range(N)),
        list(reversed(range(N))),
    )

    if os.getenv("IBM_Q_API_KEY"):
        backend = Aer.get_backend("qasm_simulator")
    else:
        backend = Aer.get_backend("qasm_simulator")

    # answer_symbols = ["n" for i in range(len(component))]
    answer_symbols = decode_bitstring(
        get_circuit_result(backend, circuit)
    )

    print("BEFORE {}\nAFTER {}".format(symbol_case, answer_symbols))

    for index, symbol_answer in enumerate(answer_symbols):
        print("{} -> {}".format(sorted_symbols[index][0], symbol_answer))
        sorted_symbols[index][0] = symbol_answer

    return sorted_symbols


def global_measurement(board):
    """Collapse all states"""
    global found_qiskit
    if not found_qiskit:
        return  # we need qiskit installed to collapse the states

    components = [[] for i in range(5)]

    for row_nuber, row in enumerate(board):
        for col_number, cell in enumerate(row):
            if "_" in cell:
                cell_type, cell_component = cell.split("_")
                cell_component = int(cell_component)
                components[cell_component].append([cell_type, row_nuber, col_number])

    for component in components:
        if len(component) == 0:
            continue  # empty component, nothing to do
        measurement_result = handle_measurement(component)
        for cell_tuple in measurement_result:
            row_number = cell_tuple[1]
            col_number = cell_tuple[2]
            board[row_number][col_number] = cell_tuple[0]


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
        if board[x][y] in ["o", "x"]:
            return (True, "Measured cells cannot be selected!")

    # Check if trying to entangle with cell of the same type
    for x, y in selected_cells:
        if "_" in board[x][y] and board[x][y][0] == player_char:
            return (True, "You cannot entangle with your own lonely cell!")

    # Check if trying to entangle with entangled cell
    for x, y in selected_cells:
        if board[x][y][0] == "q":
            return (True, "You cannot entangle with the entangled cell!")

    return (False, "")


def update_board(board, selected_cells, player_char, measurement_turn):
    """Find the next state of the board"""
    if len(selected_cells) == 1:
        x, y = selected_cells[0]  # classical move
        component = get_max_component(board)
        board[x][y] = player_char + "_{}".format(component)
    else:
        x0, y0 = selected_cells[0]
        x1, y1 = selected_cells[1]

        if board[x1][y1] == "n":
            """x0 and y0 must always be "n" if possible"""
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        if board[x0][y0] == "n" and board[x1][y1] == "n":
            """Superposition case"""
            cell_symbol = ">"  # superposition for x

            if player_char == "o":
                cell_symbol = "("  # superposition for o

            component = get_max_component(board)
            board[x0][y0] = "{}_{}".format(cell_symbol, component)
            board[x1][y1] = "{}_{}".format(cell_symbol, component)
        elif board[x1][y1][0] == "x" or board[x1][y1][0] == "o":
            """Simple entanglement case"""
            component = int(board[x1][y1].split("_")[-1])
            board[x0][y0] = "q_{}".format(component)
            board[x1][y1] = "q_{}".format(component)

    if measurement_turn == 0:
        global_measurement(board)  # time to collapse states


def decode_board(original_board):
    """Decode board from 2d matrix of JSONs format"""
    board = []

    for row in original_board:
        board.append([])
        for json_cell in row:
            board[-1].append(json_cell["value"])

    return board


def encode_board(board):
    """Encode matrix into 2d matrix of JSONs format"""

    json_board = []

    for row_number, row in enumerate(board):
        json_board.append([])
        for col_number, cell in enumerate(row):
            json_board[-1].append(
                {"id": "{},{}".format(row_number, col_number), "value": cell}
            )

    return json_board


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

    original_board = game_state["board"]
    board = decode_board(game_state["board"])
    player_turn = game_state["playerTurn"]
    selected_cells = game_state["selectedCells"]
    measurement_turn = game_state["measurementTurn"]

    invalid, invalid_message = check_invalid(board, selected_cells, player_turn)

    # Invalid movement: same player must play again
    if invalid:
        return {
            "board": original_board,
            "playerTurn": player_turn,
            "winner": get_winner(board),
            "invalid": invalid,
            "invalidMessage": invalid_message,
            "measurementTurn": measurement_turn,
        }

    next_turn = "x" if player_turn == "o" else "o"
    next_measurement = (measurement_turn + 1) % 5

    update_board(board, selected_cells, player_turn, next_measurement)  #  do movement

    return {
        "board": encode_board(board),
        "playerTurn": next_turn,
        "winner": get_winner(board),
        "invalid": invalid,
        "invalidMessage": invalid_message,
        "measurementTurn": next_measurement,
    }
