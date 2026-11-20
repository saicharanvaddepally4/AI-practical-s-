
# Simple Reflex Agent in Python

# Environment
rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Agent
def simple_reflex_agent(location, status):
    if status == 'Dirty':
        return 'Clean'
    elif location == 'A':
        return 'Move Right'
    else:
        return 'Move Left'

# Starting position
location = 'A'

print("Initial Environment:", rooms)

# Agent actions
for i in range(4):
    status = rooms[location]

    action = simple_reflex_agent(location, status)

    print("\nLocation:", location)
    print("Status:", status)
    print("Action:", action)

    if action == 'Clean':
        rooms[location] = 'Clean'
    elif action == 'Move Right':
        location = 'B'
    elif action == 'Move Left':
        location = 'A'

print("\nFinal Environment:", rooms)
print("All Rooms Cleaned!")
