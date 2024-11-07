# Lela Parks
# Nov 5, 2024

# Problem 2, lets_see function. In resources.py, write a function lets_see 
#that takes a number and checks if it's within a range where the difference
# between the top and bottom is 10. Print if the number is in the range, and 
# return True if it is, or False if it's not.

def lets_see(number):
    bottom = 5   # The bottom of the range
    top = bottom + 10  # The top of the range (difference of 10)
    
    if bottom <= number <= top:
        print(f"{number} is in the range.")
        return True
    else:
        print(f"{number} is not in the range.")
        return False

# Problem 5: main function with if __name__ == "__main__"
def main():
    print("This only runs when I run the file directly.")

# Print that will always be executed when the file is imported or run
print("I will always get printed.")

# This conditional ensures that main() only runs when the file is executed directly
if __name__ == "__main__":
    main()