#Jason Lambert
#CSI261
#IterationsAndRecursions
def factorial_iterative(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test values
test_numbers = [3, 4, 5, 6, 7]

print("Iterative Factorial Results:")
for num in test_numbers:
    try:
        print(f"{num}! = {factorial_iterative(num)}")
    except ValueError as e:
        print(f"Error for {num}: {e}")

print("\nRecursive Factorial Results:")
for num in test_numbers:
    try:
        print(f"{num}! = {factorial_recursive(num)}")
    except ValueError as e:
        print(f"Error for {num}: {e}")

