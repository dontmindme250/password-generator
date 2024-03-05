import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_special_chars=False, exclude_similar=False, mixed_case_only=False, min_letters=0, min_numbers=0, min_special_chars=0):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    if length < min_letters + min_numbers + min_special_chars:
        raise ValueError("Password length is too short for the specified minimum requirements of letters, numbers, and special characters.")

    characters = ""
    if use_letters:
        if mixed_case_only:
            characters += string.ascii_letters
        else:
            characters += string.ascii_lowercase + string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if exclude_similar:
        characters = characters.translate({ord(c): None for c in 'l1O0I|'})

    password = ''
   
    if min_letters > 0:
        password += ''.join(random.choice(string.ascii_letters) for _ in range(min_letters))
    if min_numbers > 0:
        password += ''.join(random.choice(string.digits) for _ in range(min_numbers))
    if min_special_chars > 0:
        password += ''.join(random.choice(string.punctuation) for _ in range(min_special_chars))

    remaining_length = max(0, length - len(password))
    password += ''.join(random.choice(characters) for _ in range(remaining_length))


    password = ''.join(random.sample(password, len(password)))
    
    return password

# note: sometimes it takes a bit to continue after the include letters question but it works (trust)
def get_user_preferences():
    while True:
        try:
            length = int(input("Enter password length: "))
            use_letters = input("Include letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            exclude_similar = input("Exclude similar characters? (y/n): ").lower() == 'y'
            mixed_case_only = input("Use mixed case letters only? (y/n): ").lower() == 'y'
            
            min_letters = int(input("Minimum number of letters (Enter 0 if no minimum): "))
            min_numbers = int(input("Minimum number of numbers (Enter 0 if no minimum): "))
            min_special_chars = int(input("Minimum number of special characters (Enter 0 if no minimum): "))


            if min_letters + min_numbers + min_special_chars > length:
                print("Error: The sum of minimum letters, numbers, and special characters exceeds the total password length.")
                continue
            
            return (length, use_letters, use_numbers, use_special_chars, exclude_similar, mixed_case_only, min_letters, min_numbers, min_special_chars)
        except ValueError as e:
            print(f"Invalid input: {e}")

def main():
    try:
        prefs = get_user_preferences()
        password = generate_password(*prefs)
        print("Your generated password is:", password)
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()