import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special_chars=True):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type should be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
