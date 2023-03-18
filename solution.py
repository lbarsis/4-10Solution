from itertools import product, permutations

def all_combinations(arr, operators, target):
    if len(arr) != 4:
        return "Input must contain exactly 4 numbers."

    # Generate all permutations of the given array
    number_permutations = permutations(arr)

    # Create a set to store unique combinations
    unique_combinations = set()

    # Generate all possible combinations of operators
    operator_combinations = product(operators, repeat=3)

    # List of possible parenthetical arrangements
    arrangements = [
        "((A1O1A2)O2A3)O3A4",
        "(A1O1(A2O2A3))O3A4",
        "A1O1((A2O2A3)O3A4)",
        "A1O1(A2O2(A3O3A4))",
        "(A1O1A2)O2(A3O3A4)",
        "A1O1A2O2A3O3A4",
        "(A1O1(A2O2A3)O3A4)",
        "((A1O1A2)O2(A3O3A4))",
        "(A1O1A2)O2A3O3A4",
        "A1O1(A2O2A3O3A4)",
        "A1O1A2O2(A3O3A4)",
        "(A1O1A2)O2(A3O3A4)"
    ]

    # Iterate through the generated permutations
    for num_perm in number_permutations:
        for op_comb in operator_combinations:
            for arrangement in arrangements:
                expression = arrangement
                for i in range(1, 5):
                    expression = expression.replace(f"A{i}", str(num_perm[i - 1]))
                for i in range(1, 4):
                    expression = expression.replace(f"O{i}", op_comb[i - 1])
                try:
                    if eval(expression) == target:
                        unique_combinations.add(expression)
                except ZeroDivisionError:
                    continue

    return list(unique_combinations)

# Example usage
arr = [5,2,0,9]
operators = ['+', '-', '*', '/']
print(all_combinations(arr, operators, 10))
