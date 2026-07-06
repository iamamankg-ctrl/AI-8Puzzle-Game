from collections import deque
import heapq

# ==========================
# GOAL STATE
# ==========================

GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# ==========================
# CHECK GOAL
# ==========================

def is_goal(state):
    return state == GOAL_STATE


# ==========================
# SWAP
# ==========================

def swap(state, i, j):
    state = list(state)

    state[i], state[j] = state[j], state[i]

    return tuple(state)


# ==========================
# GET NEIGHBORS
# ==========================

def get_neighbors(state):

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    neighbors = []

    # Up
    if row > 0:
        neighbors.append(swap(state, zero, zero - 3))

    # Down
    if row < 2:
        neighbors.append(swap(state, zero, zero + 3))

    # Left
    if col > 0:
        neighbors.append(swap(state, zero, zero - 1))

    # Right
    if col < 2:
        neighbors.append(swap(state, zero, zero + 1))

    return neighbors


# ==========================
# BFS
# ==========================

def bfs(start_state):

    if is_goal(start_state):
        return [start_state]

    queue = deque([start_state])

    visited = {start_state}

    parent = {}

    while queue:

        current = queue.popleft()

        if is_goal(current):
            break

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    else:
        return None

    path = []

    while current != start_state:

        path.append(current)

        current = parent[current]

    path.append(start_state)

    path.reverse()

    return path


# ==========================
# TEST
# ==========================

if __name__ == "__main__":

    start = (
        1, 2, 3,
        4, 5, 6,
        7, 0, 8
    )

    path = bfs(start)

    if path is None:

        print("No solution found!")

    else:

        print("Steps:", len(path) - 1)

        for i, state in enumerate(path):

            print(f"\nStep {i}")

            for r in range(3):
                print(state[r * 3:(r + 1) * 3])