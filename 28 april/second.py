import re

pattern = '.+@gmail.com$'

email = input("Enter email ID to check: ")

print("Valid Email") if re.match(pattern, email) else print("Invalid Email")