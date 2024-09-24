import re

text = "Ali and Per are friends. Kari and Joe know each other. James has known Peter since school days."
line = "-" * 30

names = []


# Split every word based on whitespace character
words = re.split("\s", text)

# For every word check if it contains a capital letter
for word in words:
    if re.match("[A-Z]", word):
        # If it does contain a capital letter, append this into the names list
        names.append(word)


# Pretty print
print(f"\n\tFriendships: \n{line}")
for i in range(0, len(names), 2):
    print(f"{names[i]:>12} - {names[i+1]}")
