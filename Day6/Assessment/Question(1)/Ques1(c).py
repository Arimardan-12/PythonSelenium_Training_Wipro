"""--Match and search functions, Regular expression patterns, Meta-characters, Special sequences--
3.Demonstrates the use of Meta-characters & Special sequences
Example: Validate a username with optional digits
Format:Starts with letters & May end with numbers"""
import re
username = "admin_45"
#username ="@arvii"
pattern = r"\w+_?\d*"
match = re.fullmatch(pattern, username)
if match:
    print("Valid username")
else:
    print("Invalid username")