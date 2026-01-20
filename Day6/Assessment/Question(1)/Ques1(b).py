"""	--Match and search functions, Regular expression patterns, Meta-characters, Special sequences--
2. Uses re.search() to find the first occurrence of a valid email address in a given text"""

import re
text = "support_team23@gmail.com"
email_pattern = r"\w+@\w+\.\w+"
match = re.search(email_pattern, text)
if match:
    print("Email found:", match.group())
else:
    print("No email found")