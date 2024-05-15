import numpy as np 

def evaluate_polynomial(coefficients, x):
    p = np.poly1d(coefficients)

    return p(x)

coefficients = list(map(int, input("Enter the value of coefficeints of the polynomial : ").split()))
x = int(input("Enter the value of variable: "))


result = evaluate_polynomial(coefficients, x)

print(f"The value of the polynomial at x = {x} is {result}.")
