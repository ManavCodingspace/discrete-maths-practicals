class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if not self.matrix[i][i]:  # Check if matrix[i][i] is False (0)
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] and self.matrix[j][i] and i != j:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j]:  # If there is a relation from i to j
                    for k in range(self.size):
                        if self.matrix[j][k] and not self.matrix[i][k]:  # Check i to k relation
                            return False
        return True

    def check_relation_type(self):
        is_equivalence = self.is_reflexive() and self.is_symmetric() and self.is_transitive()
        is_partial_order = self.is_reflexive() and self.is_antisymmetric() and self.is_transitive()

        if is_equivalence:
            return "Equivalence Relation"
        elif is_partial_order:
            return "Partial Order Relation"
        else:
            return "None"


# Example usage:
if __name__ == "__main__":
    # Example matrix representing a relation
    matrix = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    relation = RELATION(matrix)

    print("Reflexive:", relation.is_reflexive())
    print("Symmetric:", relation.is_symmetric())
    print("Antisymmetric:", relation.is_antisymmetric())
    print("Transitive:", relation.is_transitive())

    print("Type of Relation:", relation.check_relation_type())
