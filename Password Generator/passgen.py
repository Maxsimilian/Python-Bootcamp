#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Create an empty list to store the random password
password = []

if nr_symbols < 0 or nr_numbers < 0 or nr_letters < 0:
  print("You have entered invalid numbers")
else: 
  for s in range(0, nr_symbols):
    password.append(random.choice(symbols))

  for  n in range(0, nr_numbers):
    password.append(random.choice(numbers))
  
  for p in range (0, nr_letters):
    password.append(random.choice(letters))
  random.shuffle(password)
  print(''.join(password))


# Alternative method instead of ''.join()
'''
random_password = ""
for n in password:
  random_password += n
'''
