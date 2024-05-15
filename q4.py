from itertools import product

def find_solutions(n,c):
    solutions = [p for p in product(range (c+1), repeat = n) if sum(p) == c]
    return solutions

n = 3
c = 5
solutions = find_solutions(n,c)
for solution in solutions:
    print(solution)     
