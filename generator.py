import secrets
import string

def validInput(length):
    if (not length.isdigit()):
        print(f"You need to enter a positive int.\n")
        return 0
    elif int(float(length)) not in range(1,30,1):
        print(f"Length needs to be between 1 and 30.\n")
        return 0
    else:
        print(f"Password length will be {length}\n")
        return int(float(length))

def generate_password(characters, password_length):
    password = ''.join(secrets.choice(characters) for i in range (1,password_length + 1, 1))
    return password

def main():
    desired_length = input("How many characters would you like in your password?\n")
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password_length = validInput(desired_length)
    if password_length != 0:
        password = generate_password(valid_characters, password_length)
        print(f"Your password is: {password}")

if __name__ == "__main__":
    main()