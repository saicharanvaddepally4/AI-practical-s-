
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Breadth First Search
def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for child, cost in graph[node]:
                queue.append((child, path + [child]))

# Depth First Search
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for child, cost in graph[node]:
                stack.append((child, path + [child]))

# Uniform Cost Search
def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for child, weight in graph[node]:
                heapq.heappush(
                    pq, (cost + weight, child, path + [child])
                )

start = 'A'
goal = 'G'

b = bfs(start, goal)
d = dfs(start, goal)
u, cost = ucs(start, goal)

def path_cost(path):
    total = 0
    for i in range(len(path)-1):
        for node, weight in graph[path[i]]:
            if node == path[i+1]:
                total += weight
                break
    return total

print("BFS Path:", b)
print("BFS Cost:", path_cost(b))

print("DFS Path:", d)
print("DFS Cost:", path_cost(d))

print("UCS Path:", u)
print("UCS Cost:", cost)

print("\nSearch Comparison")
print("BFS finds shortest path in number of edges")
print("DFS explores depth first")
print("UCS finds minimum cost path")
