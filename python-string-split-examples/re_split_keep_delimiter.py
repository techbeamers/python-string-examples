import re

expression = "3 + 5 * 2 - 8 / 4"

# Define the pattern to match operators
pattern = r'(\+|\-|\*|\/)'

# Use re.split() to split the expression while keeping operators
result = re.split(pattern, expression)

# Filter out empty strings from the result
result = [part.strip() for part in result if part.strip()]

print("Result:", result)
