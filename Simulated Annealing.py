import random
import math

# Function to evaluate the number of conflicts on the board
def evaluate(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if two queens are in the same column or diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Function to generate a random initial board
def random_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

# Function to display the board
def display_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))
    print("\n")

# Function to get neighbors (generate new board states)
def get_neighbors(board):
    neighbors = []
    for i in range(len(board)):
        for j in range(len(board)):
            if j != board[i]:  # Don't move a queen to its own column
                new_board = board[:]
                new_board[i] = j
                neighbors.append(new_board)
    return neighbors

# Simulated Annealing algorithm
def simulated_annealing(n, initial_temp=1000, cooling_rate=0.99, stopping_temp=0.1, max_iterations=1000):
    current_board = random_board(n)
    current_score = evaluate(current_board)
    temperature = initial_temp
    iteration = 0

    print("Initial Board:")
    display_board(current_board)
    print(f"Initial Conflicts: {current_score}\n")

    while temperature > stopping_temp and iteration < max_iterations:
        neighbors = get_neighbors(current_board)
        next_board = random.choice(neighbors)
        next_score = evaluate(next_board)
        
        # Calculate the change in energy (conflicts)
        delta_e = next_score - current_score
        
        # If the new state is better, accept it
        if delta_e < 0:
            current_board = next_board
            current_score = next_score
            print(f"Moving to a better state with {current_score} conflicts:")
            display_board(current_board)
            print(f"Conflicts: {current_score}\n")
        else:
            # Accept worse solution with a certain probability
            acceptance_probability = math.exp(-delta_e / temperature)
            if random.random() < acceptance_probability:
                current_board = next_board
                current_score = next_score
                print(f"Accepted worse state with {current_score} conflicts (probabilistic move):")
                display_board(current_board)
                print(f"Conflicts: {current_score}\n")
        
        # Cool down the temperature
        temperature *= cooling_rate
        iteration += 1

        # If we reach a solution with 0 conflicts, stop early
        if current_score == 0:
            break

    return current_board, current_score

# Run the algorithm for 4-Queens
n = 4
solution, score = simulated_annealing(n)

if score == 0:
    print("Solution found:")
    display_board(solution)
else:
    print("No solution found. Final configuration:")
    display_board(solution)
