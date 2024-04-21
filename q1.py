class SET:
    def __init__(self, elements):
        self.elements = set(elements)  # Store elements as a set

    def is_member(self, element):
        """Check if element belongs to the set"""
        return element in self.elements

    def powerset(self):
        """Generate the power set of the set"""
        import itertools
        all_subsets = []
        for size in range(len(self.elements) + 1):
            all_subsets.extend(itertools.combinations(self.elements, size))
        return [set(subset) for subset in all_subsets]

    def subset(self, other_set):
        """Check if self is a subset of other_set"""
        return self.elements <= other_set.elements

    def union(self, other_set):
        """Compute the union of two sets"""
        return SET(self.elements.union(other_set.elements))

    def intersection(self, other_set):
        """Compute the intersection of two sets"""
        return SET(self.elements.intersection(other_set.elements))

    def complement(self, universal_set):
        """Compute the complement of the set relative to a universal set"""
        return SET(universal_set.elements.difference(self.elements))

    def set_difference(self, other_set):
        """Compute the set difference (self - other_set)"""
        return SET(self.elements.difference(other_set.elements))

    def symmetric_difference(self, other_set):
        """Compute the symmetric difference of two sets"""
        return SET(self.elements.symmetric_difference(other_set.elements))

    def cartesian_product(self, other_set):
        """Compute the cartesian product of two sets"""
        return SET({(x, y) for x in self.elements for y in other_set.elements})


def display_menu():
    print("\nMENU")
    print("1. Check if element is a member")
    print("2. Display powerset")
    print("3. Check if one set is a subset of another")
    print("4. Perform union of two sets")
    print("5. Perform intersection of two sets")
    print("6. Compute complement of the set")
    print("7. Compute set difference")
    print("8. Compute symmetric difference")
    print("9. Compute cartesian product of two sets")
    print("0. Exit")


def main():
    elements1 = input("Enter elements of first set (space-separated): ").split()
    set1 = SET(elements1)

    universal_elements = input("Enter elements of universal set (space-separated): ").split()
    universal_set = SET(universal_elements)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            element = input("Enter element to check membership: ")
            print(set1.is_member(element))

        elif choice == '2':
            print("Power set:")
            for subset in set1.powerset():
                print(subset)

        elif choice == '3':
            elements2 = input("Enter elements of second set (space-separated): ").split()
            set2 = SET(elements2)
            print(set1.subset(set2))

        elif choice == '4':
            elements2 = input("Enter elements of second set (space-separated): ").split()
            set2 = SET(elements2)
            print("Union:", set1.union(set2).elements)

        elif choice == '5':
            elements2 = input("Enter elements of second set (space-separated): ").split()
            set2 = SET(elements2)
            print("Intersection:", set1.intersection(set2).elements)

        elif choice == '6':
            print("Complement:", set1.complement(universal_set).elements)

        elif choice == '7':
            elements2 = input("Enter elements of second set (space-separated): ").split()
            set2 = SET(elements2)
            print("Set Difference:", set1.set_difference(set2).elements)

        elif choice == '8':
            elements2 = input("Enter elements of second set (space-separated): ").split()
            set2 = SET(elements2)
            print("Symmetric Difference:", set1.symmetric_difference(set2).elements)

        elif choice == '9':
            elements2 = input("Enter elements of second set (space-separated): ").split()
            set2 = SET(elements2)
            print("Cartesian Product:", set1.cartesian_product(set2).elements)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
