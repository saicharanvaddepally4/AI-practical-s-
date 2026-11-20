
# Value Iteration in Grid World

rows = 3
cols = 3

goal = (2, 2)
gamma = 0.9
reward = -1

actions = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

# Initialize values
V = {}

for r in range(rows):
    for c in range(cols):
        V[(r, c)] = 0

# Value Iteration
for iteration in range(100):
    new_V = V.copy()

    for state in V:
        if state == goal:
            continue

        values = []

        for action in actions:
            dr, dc = actions[action]
            nr = state[0] + dr
            nc = state[1] + dc

            # Check grid boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                next_state = (nr, nc)
            else:
                next_state = state

            value = reward + gamma * V[next_state]
            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Display values
print("Value Iteration Results")
print("-----------------------")

for r in range(rows):
    for c in range(cols):
        print(round(V[(r, c)], 2), end="\t")
    print()

# Display best policy
print("\nOptimal Policy:")

for state in V:
    if state == goal:
        print(state, ": GOAL")
        continue

    best_action = None
    best_value = float('-inf')

    for action, (dr, dc) in actions.items():
        nr = state[0] + dr
        nc = state[1] + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            value = reward + gamma * V[(nr, nc)]
            if value > best_value:
                best_value = value
                best_action = action

    print(state, ":", best_action)
