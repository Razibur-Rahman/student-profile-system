# Import the random module to generate random characters
import random
# All possible characters for password generation
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*?/.,;:"

# Display options to the user
print("1. Create your own password")
print("2. Generate a random password")

# Take user choice as input
choice = input("Enter your choice (1/2): ")

if choice == "1":
    # Take password from user
    password = input("Enter your password: ")
    # Display the entered password
    print("Your password is:", password)

# If user chooses option 2
elif choice == "2":
    # Take desired password length from user and convert to integer
    length = int(input("Enter your password length: "))
    # Initialize empty password string
    password = ""

    # Loop runs 'length' times
    for i in range(length):
        # Add a random character from 'chars' to password
        password += random.choice(chars)
    # Display the generated password
    print("\nGenerated password:", password)

# If user enters invalid option
else:
    # Show error message
    print("Invalid choice!")