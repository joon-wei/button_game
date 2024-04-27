import numpy as np

print(
    "This will calculate the probability of attaining a certain high score in button_game."
)

# Get user's input, loop is repeated until a valid number is entered.
while True:
    try:
        N = int(input("Enter the number from 1 - 100: "))
        if N <= 100:
            if N < 0:
                print("Please entera positive integer.")
            else:
                break
        else:
            print("Please enter a number <= 100.")
    except ValueError:
        print("Please enter a valid number.")

#Create array of passing probabilities [1, 0.99, 0.98, ..., 0.01]
arr = np.arange(1, 0, -0.01)

# Product the elements in the array up to N 
product = np.prod(arr[:N])

print(f"Probability: {product}")
