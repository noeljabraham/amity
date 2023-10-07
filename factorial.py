# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main function
def main():
    try:
        # Get input from the user
        num = int(input("Enter a non-negative integer: "))

        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
