##Exercise 1:


# def factorial(x):
#   # Start with 1
#     result = 1
#     for i in range(1,x + 1):
#         result = result * i
#     return result
# number = int(input("Please enter a positive number: "))
# print("The factorial of", number, "is",factorial(number))




##Exercice 2:


# def divisors():
#     x = int(input("Please enter a number:"))
#     #emply list to store div
#     div=[]
#     for i in range(1, x+1):
#         # Check if i is a divisor of num
#         if (x % i == 0): 
#             div.append(i)
#     return div  
# print(divisors())



##Exercice 3:


# def reverseString(s):
#     reversed_str = ""
#     for letter in s:
#         reversed_str = letter + reversed_str
#     return reversed_str

# word = input("Please enter any word: ")
# result = reverseString(word)
# print("Reversed string:", result)



##Exercice 4:


# def get_even_numbers(numbers):
#     even_numbers = []
    
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
    
#     return even_numbers

# inputa = input("Enter the numbers seperated by space: ")
# # Convert input string to list int
# number_list = []
# for num in inputa.split():
#     number_list.append(int(num))

# result = get_even_numbers(number_list)
# print("Even numbers:", result)



##Exercice 5:


# def is_strong_password(password):
#     if len(password) < 8:
#         return False
#     has_uppercase = False
#     has_lowercase = False
#     has_digit = False
#     has_special = False
    
#     for char in password:
#         if char.isupper():
#             has_uppercase = True
#         elif char.islower():
#             has_lowercase = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in '#?!$':
#             has_special = True
    
#     if has_uppercase and has_lowercase and has_digit and has_special:
#         return True
#     else:
#         return False

# password = input("Enter a password: ")
# if is_strong_password(password):
#     print("Your password is strong!")
# else:
#     print("Your password is not strong enough.")



##Exercice 6


# def is_valid_ipv4_address(ip):
#     parts = ip.split('.')

#     if len(parts) != 4:
#         return "Invalid IPv4 address: Must have 4 parts separated by dots."

#     for part in parts:
#         if not part.isdigit() or (len(part) > 1 and part[0] == '0'):
#             return "Invalid IPv4 address: Parts must be integers between 0 and 255."

#         num = int(part)

#         if num < 0 or num > 255:
#             return "Invalid IPv4 address: Parts must be between 0 and 255."

#     return "Valid IPv4 address"

# ip_address = input("Please enter an IP address: ")
# result = is_valid_ipv4_address(ip_address)
# print(result)