import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_special_chars=False):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    return length, use_letters, use_numbers, use_special_chars

def main():
    length, use_letters, use_numbers, use_special_chars = get_user_preferences()
    password = generate_password(length, use_letters, use_numbers, use_special_chars)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()