# Example log entry
log_entry = "user123 performed action: 'edit' at timestamp: '2022-03-01 08:45:00'"

# Using partition() to split the log entry
user, _, remaining = log_entry.partition(' performed action: ')
action, _, timestamp = remaining.partition(" at timestamp: ")

# Printing the results
print("Original Log Entry:", log_entry)
print("User:", user)
print("Action:", action)
print("Timestamp:", timestamp)

