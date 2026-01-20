"""	3. Uses regular expression modifiers such as:
re.IGNORECASE, re.MULTILINE, re.DOTALL
	4. Demonstrates how modifiers affect pattern matching with examples
"""
import re
text = "Hello World\nhello Python\nHELLO Regex"

# IGNORECASE: matches regardless of case
result1 = re.findall("hello", text, re.IGNORECASE)
print("\nIGNORECASE result:", result1)

# MULTILINE: ^ matches start of each line
result2 = re.findall("^hello", text, re.IGNORECASE | re.MULTILINE)
print("MULTILINE result:", result2)

# DOTALL: . matches newline character
result3 = re.search("Hello.*Regex", text, re.DOTALL)
print("DOTALL result:", result3.group() if result3 else "No match")


print("-------4 part solution below------")
#Demonstrate How Modifiers Affect Pattern Matching
# Without IGNORECASE
print(re.findall("hello", text))  # matches only lowercase 'hello'

# With IGNORECASE
print(re.findall("hello", text, re.IGNORECASE))  # matches all cases

# Without MULTILINE
print(re.findall("^hello", text, re.IGNORECASE))  # checks only first line

# With MULTILINE
print(re.findall("^hello", text, re.IGNORECASE | re.MULTILINE))  # checks every line

# Without DOTALL
print(re.search("Hello.*Regex", text))  # no match

# With DOTALL
print(re.search("Hello.*Regex", text, re.DOTALL).group())  # matches across lines
