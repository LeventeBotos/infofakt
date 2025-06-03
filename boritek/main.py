# import itertools as it

# possibilities = []
# points = ["a", "b", "c", "d", "e", "f"]
# sides = [["a", "b"], ["a", "e"], ["a", "f"], ["e", "f"], ["e", "d"], 
#          ["d", "f"], ["d", "c"], ["c", "b"], ["b", "f"], ["d", "b"]]

# perm = it.permutations(sides)

# def is_valid_path(permutation):
#     last = None
#     next = None
#     for j in range(len(permutation) - 1):
#         a, b = permutation[j]
#         c, d = permutation[j + 1]

   
#         if last and a != last and b != last:
#             return False
#         if a == c :
#             last = a
#             next=c

#         elif a== d:
#             last= a
#             next=d
            
#         elif b == c :
#             last = b
#             next= c
#         elif b == d :
#             last = b
#             next= d
#         else:
#             return False  # No continuity
#     return True


# for thing in perm:
#     if is_valid_path(thing):
#         possibilities.append(thing)

# print(f"Valid permutaciok: {len(possibilities)}")

# 40 / 44/ 80/ 88
from collections import defaultdict

# Graph representation: a box with a point in the center and an upside-down triangle on top
points = ["a", "b", "c", "d", "e", "f"]
sides = [["a", "b"], ["b", "c"], ["a", "c"],  # Triangle on top
         ["a", "d"], ["b", "d"], ["c", "d"],  # Central edges
         ["d", "e"], ["d", "f"]]  # Bottom connections

# Build a graph representation
graph = defaultdict(list)
for a, b in sides:
    graph[a].append(b)
    graph[b].append(a)

# Function to find all valid paths using DFS
def find_paths(start, visited, path, all_paths):
    if len(visited) == len(sides):  # All edges used
        all_paths.append(path[:])
        return

    # Explore neighbors
    for neighbor in graph[start]:
        edge = frozenset({start, neighbor})  # Use frozenset to represent edges
        if edge not in visited:
            visited.add(edge)  # Mark edge as visited
            path.append((start, neighbor))
            find_paths(neighbor, visited, path, all_paths)
            path.pop()  # Backtrack
            visited.remove(edge)  # Unmark edge

# Generate all valid paths
all_paths = []
for a, b in sides:
    visited = set()
    visited.add(frozenset((a, b)))  # Mark starting edge as visited
    find_paths(b, visited, [(a, b)], all_paths)

print(f"Valid paths for the letter shape: {len(all_paths)}")
