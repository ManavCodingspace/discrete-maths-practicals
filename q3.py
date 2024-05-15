from itertools import permutations

# without repetations
def permutate_without_repetations(digits):
    perms = [' '.join(p) for p in permutations (digits)]
    return perms

# with repetations

from itertools import product 

def permutate_with_repeations(digits,length):
    perms = [' '.join(p) for p in product(digits, repeat = length)]
    return perms

digits = '123'    
print("permutate_with_repeations: ")
print(permutate_with_repeations(digits, len(digits)))

print("Permutation_without_repeations: ")
print(permutate_without_repetations(digits))
