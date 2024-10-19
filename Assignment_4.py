import json

# Function to sum elements of two tuples
def sum_tuples(tup1, tup2):
    """
    Takes two tuples as input and returns a new tuple.
    Each element in the new tuple is the sum of the corresponding elements in the input tuples.
    """
    summed_tuple = []  # Incorrectly using a list instead of a tuple
    for i in range(len(tup1)):
        summed_tuple.append(tup1[i] + tup2[i])
    return summed_tuple  # Missing parentheses for the tuple

# Function to export a dictionary to a JSON file
def export_json(dictionary, filename):
    """
    Takes a dictionary and a filename as input.
    Writes the dictionary to a file in JSON format with the given filename.
    """
    with open(filename, 'w') as file:
        json.dump(dictionary, file)  # Missing indentation for better readability
    print("Dictionary exported to", filename)  # Incorrect string concatenation

# Function to import a JSON file and convert it to a dictionary
def import_json(filename):
    """
    Takes a filename as input and reads the JSON file.
    Returns the data as a dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Main program loop to show the menu and perform actions
while True:
    # Display menu options
    print("Menu:")
    print("1. Sum Tuples")
    print("2. Export JSON")
    print("3. Import JSON")
    print("4. Exit")
    choice = input("Enter your choice: ")

    # Option 1: Sum tuples
    if choice == '1':
        # Get two tuples from the user
        tup1 = tuple(map(int, input("Enter numbers for tuple 1, separated by spaces: ").split()))
        tup2 = tuple(map(int, input("Enter numbers for tuple 2, separated by spaces: ").split()))

        # Call the function to sum the tuples
        result = sum_tuples(tup1, tup2)
        print("The summed tuple is:", result)

    # Option 2: Export a dictionary to a JSON file
    elif choice == '2':
        # Create an empty dictionary
        dictionary = {}
        num_items = int(input("How many items do you want to add to the dictionary? "))

        # Add key-value pairs to the dictionary
        for i in range(num_items):
            key = input(f"Enter key {i + 1}: ")
            value = input(f"Enter value {i + 1}: ")
            dictionary[key] = value

        # Get the filename to save the dictionary
        filename = input("Enter the filename to export (e.g., data.json): ")
        export_json(dictionary, filename)

    # Option 3: Import a JSON file and display its content
    elif choice == '3':
        # Get the filename to import
        filename = input("Enter the filename to import (e.g., data.json): ")

        # Try to read the file and show its contents
        try:
            data = import_json(filename)
            print("Data imported from the JSON file:")
            for key, value in data.items():
                print(f"{key}: {value}")
        except FileNotFoundError:
            print("File not found.")  # Missing error message
        except json.JSONDecodeError:
            print("Error reading JSON file.")  # Missing error message

    # Option 4: Exit the program
    elif choice == '4':
        print("Goodbye!")
        break

    # If the user enters something that is not a valid choice
    else:
        print("Invalid choice. Please select a number from 1 to 4.")