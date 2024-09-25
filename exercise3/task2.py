import re

passwords = ["J1234", "I_ab5", "Z9_w4", "A1234", "J12345", "I__"]


def validate_password(passwords):
    # Use 'r' before string to make the string raw
    # So that we can treat backslash as backslash and not a command
    pattern = r"\A[I-Z][\w\s]{2,3}\d\Z"
    r"""
    A specifies for a match at the beginning of the string
    [I-Z] makes sure the first character shoudl equal a capital letter from I to Z
    [\w\s] accepts any character or whitespace 
    {2, 3} for the next 2-3 characters
    \d returns a match if the string contains a digit
    \Z returns match if specified character gotten from \d matches the end of the string
    """

    for password in passwords:
        match = re.match(pattern, password)
        if match:
            print(f"Access granted")
        else:
            print("Invalid password")


validate_password(passwords)
