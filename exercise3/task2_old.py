import re


# Function to validate password based on all the parameters
def validate_password(password: str) -> bool:
    if (
        re.match("[I-Z]", password[0])  # Begins with a capital letter from I to Z
        and re.match("[a-zA-Z]", password)  # Contains an alphabetical letter
        and len(password) <= 5  # Has a length shorter or equal to 5
        and len(password) >= 4  # Has a length longer or equal to 4
        and re.match("[0-9]", password[-1])  # The last character is a number
        and password[0] != " "  # The first character can not be space
        and password[-1] != " "  # The last character can not be space
    ):
        return True
    else:
        return False


passwords = ["J1234", "I_ab5", "Z9_w4", "A1234", "J12345", "I__"]

for password in passwords:
    print(validate_password(password))
