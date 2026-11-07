
import random
import string

def generate_password():

    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4!")
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        print("\nYour Generated Password:", password)
        print("Password generated successfully!")

    except ValueError:
        print("Please enter a valid number!")


while True:

    print("\n1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()

    elif choice == "2":
        print("Thank you for using Password Generator!")
        break

    else:
        print("Invalid choice! Please try again.")