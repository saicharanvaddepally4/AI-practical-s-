
# Map Coloring using Backtracking

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
color_map = {}

# Check consistency
def is_safe(region, color):
    for neighbor in graph[region]:
        if color_map.get(neighbor) == color:
            return False
    return True

# Backtracking algorithm
def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            color_map[region] = color

            if solve(regions[1:]):
                return True

            del color_map[region]

    return False

# Main program
regions = list(graph.keys())

if solve(regions):
    print("Map Coloring Solution:")
    for region, color in color_map.items():
        print(region, ":", color)
else:
    print("No solution exists")
