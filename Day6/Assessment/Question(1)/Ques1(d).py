"""--Match and search functions, Regular expression patterns, Meta-characters, Special sequences--
4. Prints matched groups using capturing parentheses
example-Extract date parts from a date string
Format: DD-MM-YYYY"""

import re
date = "18-01-2026"
pattern = r"(\d{2})-(\d{2})-(\d{4})"
match = re.search(pattern, date)
if match:
    print("Full Date:", match.group(0))
    print("Day:", match.group(1))
    print("Month:", match.group(2))
    print("Year:", match.group(3))
else:
    print("Invalid date format")
