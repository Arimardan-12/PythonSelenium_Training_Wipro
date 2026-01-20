"""	--Assertions, Regular expression modifiers--
 	1. Validates a strong password using regular expressions with the following rules:
	Minimum 8 characters
	At least one uppercase letter
	At least one lowercase letter
	At least one digit
	At least one special character
	2. Uses lookahead assertions (?=)
	"""
import re
def check_password(password):
     #lookahead assertion
    pattern = (
        r"^"                 # Start of string
        r"(?=.*[A-Z])"       # At least one uppercase letter
        r"(?=.*[a-z])"       # At least one lowercase letter
        r"(?=.*\d)"          # At least one digit
        r"(?=.*[@$!%*?&#])"  # At least one special character
        r".{8,}$"            # Minimum 8 characters
    )

    # Return True if password matches the pattern
    return re.search(pattern, password) is not None



password = input("Enter password: ")

if check_password(password):
    print("Strong password")
else:
    print("Weak password")
    print("Password must contain:")
    print("- At least 8 characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One digit")
    print("- One special character")

