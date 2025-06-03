min_val = 45
num_terms = 5  # Change this to increase the number of terms
possibilities = {min_val}  # Using a set for uniqueness


def generate_sums(current_terms, start):
    if len(current_terms) == num_terms:
        total = min_val - sum(current_terms) + 10 * sum(current_terms)
        possibilities.add(total)
        return

    for i in range(start, 10):
        generate_sums(current_terms + [i], i + 1)


generate_sums([], 0)

print(len(possibilities))
print(sorted(possibilities))

# min = 45
# a1 = 0 
# a2 = 0
# possibilities = [45]

# for i in range(0, 9):
#     for j in range(i+1, 10):
#         sum = min - (i + j) +10 * (i + j)
#         if sum not in possibilities:
#             possibilities.append(sum)

# print(len(possibilities))
# print(possibilities)