# Lela Parks
# Nov 5, 2024

#Problem 1,  write a function, say_my_name, which takes 
#the parameter of a name and prints out a friendly greeting half the time and an 
# angry greeting half the time

#Random and Import only need to be placed once at the top
#Reuse randit code from last week
import random
import resources  # Assuming resources.py is available and contains lets_see function

# Problem 1: say_my_name function
def say_my_name(name):
    # Randomly choose between friendly or angry greeting
    greetings = [f"Hi there {name}", f"Go away {name}"]
    print(random.choice(greetings))  # Randomly print one of the two greetings

# Problem 3: multiply_if function
def multiply_if():
    # Generate a list of 10 random numbers between 1 and 20
    rand_nums = [random.randint(1, 20) for _ in range(10)]
    
    # Use lets_see to decide whether to multiply numbers by 5
    updated_list = [num * 5 if resources.lets_see(num) else num for num in rand_nums]
    
    return updated_list

# Problem 4: unique_elements function
def unique_elements(lst):
    unique_list = []
    for item in sorted(set(lst)):  # Remove duplicates by converting to a set, then sort
        unique_list.append(item)  # Use append method to add unique items in order
    return unique_list

# Test the functions
if __name__ == "__main__":
    # Test say_my_name function
    say_my_name("Lela")
    
    # Test multiply_if function (assuming lets_see is available in resources.py)
    updated_list = multiply_if()
    print("Updated list after multiply_if:", updated_list)
    
    # Test unique_elements function
    test_list = [1, 3, 3, 3, 6, 2, 3, 5]
    print("Unique elements in ascending order:", unique_elements(test_list))


