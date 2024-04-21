import itertools

def generate_permutations(digits, repeat=False):
    digits_list = list(digits)

    if repeat:
        permutations = itertools.product(digits_list, repeat=len(digits_list))
    else:
        permutations = itertools.permutations(digits_list)

    for perm in permutations:
        yield ''.join(perm)


def main():

    digits = input("Enter digits (without spaces): ")
    repeat = input("Allow repeation in permutation (y/n): ").strip().lower() == 'y'

    if repeat:
        print("Generating Permutations with Repeations...")

    else:
        print("Generating Permutations without repeation...")


    for perm in generate_permutations(digits,repeat):
        print(perm)

if __name__ == "__main__":
    main()                                