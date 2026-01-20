"""	--Match and search functions, Regular expression patterns, Meta-characters, Special sequences--
1.Uses re.match() to check whether a string starts with a valid employee ID in the format
 EMP followed by 3 digits (e.g., EMP123)
"""
import re
employee_id = "EMP123"
pattern = r"^EMP\d{3}$"
if re.match(pattern, employee_id):
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")