import random
import string
def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_characters = letters + digits + punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
