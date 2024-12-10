import itertools as it

possibilities = []
points = ["a", "b", "c", "d", "e", "f"]
sides = [["a", "b"], ["a", "e"], ["a", "f"], ["e", "f"], ["e", "d"], 
         ["d", "f"], ["d", "c"], ["c", "b"], ["b", "f"], ["d", "b"]]

perm = it.permutations(sides)

def is_valid_path(permutation):
    last = None
    next = None
    for j in range(len(permutation) - 1):
        a, b = permutation[j]
        c, d = permutation[j + 1]

   
        if last and a != last and b != last:
            return False
        if a == c or a == d:
            last = a
            
        elif b == c or b == d:
            last = b
        else:
            return False  # No continuity
    return True


for thing in perm:
    if is_valid_path(thing):
        possibilities.append(thing)

print(f"Valid permutaciok: {len(possibilities)}")
