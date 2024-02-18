import re

input_string = "John:123-456-7890, Jane/987-654-3210; Bob-555-1234"

# Define the pattern to match various separators
pattern = r'[:;,/-]'

# Use re.split() to separate names and phone numbers
result = re.split(pattern, input_string)

# Filter out empty strings from the result
result = [part.strip() for part in result if part.strip()]

# Separate names and phone numbers
names = result[::2]
phone_numbers = result[1::2]

print("Names:", names)
print("Phone Numbers:", phone_numbers)

