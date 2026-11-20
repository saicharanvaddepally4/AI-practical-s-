
import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Heuristic 1: Misplaced Tiles
def misplaced(state):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

# Heuristic 2: Manhattan Distance
def manhattan(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x, y = divmod(i, 3)
            a, b = divmod(goal.index(state[i]), 3)
            distance += abs(x-a) + abs(y-b)
    return distance

# Generate next states
def neighbors(state):
    result = []
    pos = state.index(0)
    moves = [-3, 3, -1, 1]

    for move in moves:
        new = pos + move

        if 0 <= new < 9:
            if move == -1 and pos % 3 == 0:
                continue
            if move == 1 and pos % 3 == 2:
                continue

            temp = list(state)
            temp[pos], temp[new] = temp[new], temp[pos]
            result.append(tuple(temp))

    return result

# A* Algorithm
def astar(start, heuristic):
    pq = [(heuristic(start), 0, start, [])]
    visited = {}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state], g

        if state in visited and visited[state] <= g:
            continue

        visited[state] = g

        for next_state in neighbors(state):
            new_g = g + 1
            new_f = new_g + heuristic(next_state)

            heapq.heappush(pq, (
                new_f, new_g, next_state, path + [state]
            ))

    return None, -1

# Compare heuristics
for name, h in [("Misplaced Tiles", misplaced),
                ("Manhattan Distance", manhattan)]:

    path, cost = astar(start, h)

    print("\nHeuristic:", name)
    print("Number of moves:", cost)
    print("States explored:", len(path) if path else 0)

    if path:
        for state in path:
            print(state[0:3])
            print(state[3:6])
            print(state[6:9])
            print()
