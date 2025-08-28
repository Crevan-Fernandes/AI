from collections import deque

# Helper function to print puzzle state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Check if goal state is reached
def is_goal(state, goal):
    return state == goal

# Generate neighbors of current state
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)  # Position of blank (0)

    # Possible moves: up, down, left, right
    moves = {
        "UP": -3,
        "DOWN": 3,
        "LEFT": -1,
        "RIGHT": 1
    }

    for move, pos_change in moves.items():
        new_index = zero_index + pos_change

        # Invalid moves
        if move == "UP" and zero_index < 3:
            continue
        if move == "DOWN" and zero_index > 5:
            continue
        if move == "LEFT" and zero_index % 3 == 0:
            continue
        if move == "RIGHT" and zero_index % 3 == 2:
            continue

        # Swap 0 with the adjacent tile
        new_state = state[:]
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        neighbors.append((new_state, move))

    return neighbors

# BFS Algorithm
def bfs(start, goal):
    queue = deque([(start, [], 0)])  # state, path, depth
    visited = set()
    visited.add(tuple(start))

    while queue:
        state, path, depth = queue.popleft()

        if is_goal(state, goal):
            return path, depth

        for neighbor, move in get_neighbors(state):
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                queue.append((neighbor, path + [move], depth + 1))

    return None, -1

if __name__ == "__main__":
    print("Enter the start state (use 0 for blank):")
    start_state = list(map(int, input().split()))
    
    print("Enter the goal state (use 0 for blank):")
    goal_state = list(map(int, input().split()))

    if len(start_state) != 9 or len(goal_state) != 9:
        print("Error: Each state must contain exactly 9 numbers (0-8).")
    else:
        print("\nStart State:")
        print_state(start_state)

        print("Goal State:")
        print_state(goal_state)

        path, depth = bfs(start_state, goal_state)

        if path:
            print("\n✅ Solution found in", depth, "moves")
            print("Moves:", path)
        else:
            print("\n❌ No solution exists for this configuration.")
