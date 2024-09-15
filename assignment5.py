
# Function to remove odd numbers from an array
def remove_odd_numbers(arr):
    # Use a list comprehension to keep only even numbers
    new_arr = [num for num in arr if num % 2 == 0]
    return new_arr

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_odd_numbers(numbers)
print("Array after removing odd numbers:", result)

def user_function(n):
    if n < 0:
        print("Negative numbers do not have factorials.")
        return None
    
    result = 1
    while n > 0:
        result *= n
        n -= 1
    
    return result

# Test the function
factorial = 5
modified_result = user_function(factorial)
print("Factorial:", modified_result)

def add_numbers(numbers):
    total_sum = 0
    index = 0

    # Use a while loop to calculate the sum
    while index < len(numbers):
        total_sum += numbers[index]
        index += 1

    return total_sum

# Example usage
numbers = [10, 20, 30, 40, 50]
result = add_numbers(numbers)
print("Sum of all numbers:", result)

#  Write a program that has an array of numbers; if the number is 
# negative, it should remove the negative number from the array.
def remove_nagative_number(numbers):
    # use the list comprehensiion
    return("num for num in array if the num >= 0")
    
# numbers
numbers = [1, -2, 3, 4, 5, -6, -8,]
modified_result = remove_nagative_number(numbers)
print(modified_result)


def print_even_numbers():
    count = 0  # To keep track of how many even numbers have been printed
    n = 2      # Start with the first even number
    
    while count < 10:  # Loop until we've printed 10 even numbers
        print(n)
        n += 2         # Move to the next even number
        count += 1     # Increment the count of even numbers printed

print_even_numbers()


def print_integers():
    count = 1
    while count <= 25:
        print(count)  # Print the current value of count
        count += 1    # Increment count to move to the next integer

print_integers()

# Shopping Cart Program
cart = []

# Function to add an item to the cart
def add_item(item, quantity):
    cart.append({'item': item, 'quantity': quantity})
    print(f"Added {quantity} of {item} to the cart.")
    print_cart()

# Function to remove an item from the cart
def remove_item(item):
    for i in range(len(cart)):
        if cart[i]['item'] == item:
            del cart[i]
            print(f"Removed {item} from the cart.")
            break
    else:
        print(f"{item} not found in the cart.")
    print_cart()

# Function to update the quantity of an item in the cart
def update_quantity(item, quantity):
    for i in range(len(cart)):
        if cart[i]['item'] == item:
            cart[i]['quantity'] = quantity
            print(f"Updated {item}'s quantity to {quantity}.")
            break
    else:
        print(f"{item} not found in the cart.")
    print_cart()

# Function to print the contents of the cart
def print_cart():
    if cart:
        print("\nCurrent cart contents:")
        for entry in cart:
            print(f"{entry['item']}: {entry['quantity']}")
    else:
        print("\nThe cart is empty.")
    print("\n")

# Example usage
add_item("Apple", 3)
add_item("Banana", 2)
update_quantity("Apple", 5)
remove_item("Banana")
add_item("Orange", 4)
remove_item("Grapes")  # Trying to remove an item not in the cart

def insert_value(arr, index, value):
    # Insert the value at the specified index
    arr.insert(index, value)
    return arr

# Example usage
my_array = [1, 2, 3, 5, 6]
new_array = insert_value(my_array, 3, 4)  # Insert 4 at index 3
print(new_array)
