import re

pattern = '@.+$'

email = input("Enter email ID: ")

domain_name = re.search(pattern, email)

print(domain_name.group(0)[1:])
