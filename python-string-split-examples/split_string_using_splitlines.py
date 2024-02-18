# Eg. 1
poem = "The path not used\nTwo paths splitted in a wood,\nAnd sorry he could not walk both"
lines = poem.splitlines()
print(lines)
# Output: ['The path not used', 'Two paths splitted in a wood,', 'And sorry he could not walk both']

# Eg. 2
address = "786 Ind St.\nBlock 4\nAmbience"
lines = address.splitlines()
print(lines)
# Output: ['786 Ind St.', 'Block 4', 'Ambience']

# Eg. 3
multiline_string = """This is a
multiline
string."""
lines = multiline_string.splitlines()
print(lines)
# Output: ['This is a', 'multiline', 'string.']
