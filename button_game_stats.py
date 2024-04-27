import numpy as np

#print(arr)
print("This will calculate the probability of attaining a certain high score in button_game.")

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

    
arr = np.arange(1,0,-0.01)

product = np.prod(arr[:N])

print(f"Probability: {product}")


