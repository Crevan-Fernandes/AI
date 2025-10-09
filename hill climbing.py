import random

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

# Hill Climbing algorithm
def hill_climbing(n):
    current_board = random_board(n)
    current_score = evaluate(current_board)
    
    print("Initial Board:")
    display_board(current_board)
    print(f"Initial Conflicts: {current_score}\n")

    while current_score > 0:
        neighbors = get_neighbors(current_board)
        next_board = None
        next_score = float('inf')
        
        for neighbor in neighbors:
            score = evaluate(neighbor)
            if score < next_score:
                next_score = score
                next_board = neighbor
        
        # Print the new state if it has fewer conflicts
        if next_score < current_score:
            print(f"Moving to a better state with {next_score} conflicts:")
            display_board(next_board)
            print(f"Conflicts: {next_score}\n")
        
        # If no better neighbor is found, we stop (local maximum)
        if next_score >= current_score:
            break
        
        current_board = next_board
        current_score = next_score
    
    return current_board, current_score

# Run the algorithm for 4-Queens
n = 4
solution, score = hill_climbing(n)

if score == 0:
    print("Solution found:")
    display_board(solution)
else:
    print("No solution found. Final configuration:")
    display_board(solution)
