#Jason Lambert
#CSI261
#IterationsAndRecursions
def factorial_iterative(n):
     result = 1
     for i in range(2, n + 1):
         result *= i
     return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return n * factorial_recursive(n - 1)
    else:
        return n * factorial_recursive(n - 1)

                                
 # Sample numbers to test
test_numbers = [3, 4, 5, 6, 7]

print("Iterative Factorial Results:")
for num in test_numbers:
     print(f"{num}! = {factorial_iterative(num)}")

print("\nRecursive Factorial Results:")
for num in test_numbers:
    print(f"{num}! = {factorial_recursive(num)}")

