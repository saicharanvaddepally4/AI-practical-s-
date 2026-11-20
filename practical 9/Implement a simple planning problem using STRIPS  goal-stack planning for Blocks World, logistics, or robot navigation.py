
# Blocks World using STRIPS Planning

# Initial State
initial_state = {
    ('ON', 'A', 'TABLE'),
    ('ON', 'B', 'TABLE'),
    ('CLEAR', 'A'),
    ('CLEAR', 'B'),
    ('ARMEMPTY',)
}

# Goal State
goal_state = {
    ('ON', 'A', 'B')
}

# STRIPS Action
def move(block, source, destination):
    action = {
        'name': "Move " + block + " from " + source + " to " + destination,
        'preconditions': {
            ('ON', block, source),
            ('CLEAR', block),
            ('CLEAR', destination) if destination != 'TABLE' else ('ARMEMPTY',),
            ('ARMEMPTY',)
        },
        'add': {
            ('ON', block, destination),
            ('CLEAR', source)
        },
        'delete': {
            ('ON', block, source),
            ('CLEAR', destination)
        } if destination != 'TABLE' else {
            ('ON', block, source)
        }
    }
    return action

# Apply action
def apply_action(state, action):
    if action['preconditions'].issubset(state):
        state.difference_update(action['delete'])
        state.update(action['add'])
        print("Action:", action['name'])
        return True
    return False

# Planning
state = initial_state.copy()

print("Initial State:", state)

action = move('A', 'TABLE', 'B')

if apply_action(state, action):
    print("Goal Achieved!")
else:
    print("Action Failed!")

print("Final State:", state)
print("Goal State:", goal_state)
