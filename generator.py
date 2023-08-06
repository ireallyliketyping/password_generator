import secrets
import string

# Check to make sure the password length input is correct.
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

# Ask the user for their password character selection.
def include_punctuation():
    answer = input("Would you like to include punctuation? (y/n)\n")
    if answer == "y":
        print(f"Password will include punctuation.\n")
        return True
    else:
        print(f"Password will not include punctuation.\n")
        return False

# Generate the password, of correct length and including correct characters.
def generate_password(characters, password_length):
    password = ''.join(secrets.choice(characters) for i in range (1,password_length + 1, 1))
    return password

def main():
    desired_length = input("How many characters would you like in your password?\n")
    password_length = validInput(desired_length)
    punctuation = include_punctuation()
    if password_length != 0:
        # Ask if the user wants to include punctuation in the password
        if punctuation:
            valid_characters = string.ascii_letters + string.digits + string.punctuation
        elif not punctuation:
            valid_characters = string.ascii_letters + string.digits
        
        # Generate the password of the right length and character selection.
        password = generate_password(valid_characters, password_length)
        print(f"Your password is: {password}")
    return 0

if __name__ == "__main__":
    main()