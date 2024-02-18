# Extract user IDs and actions from a log string
log_data = "123:login|456:logout|789:login|321:logout"

# The string has multiple delimiters '|' and ":'
# Let's use split('|') to separate individual user actions
# And use split(':') to split within each part

user_actions = [entry.split(':') for entry in log_data.split('|')]

print("After splitting the string using the delimiters '|', ':':")
for user_action in user_actions:
    user_id, action = user_action
    print("User ID:", user_id, "Action:", action)
