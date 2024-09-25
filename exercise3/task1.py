import re

# Compile the regex pattern once to ensure efficiency
find_name = re.compile(r"^([A-Z][a-z]+).*?([A-Z][a-z]+)")

sentences = [
    "Ali and Per are friends.",
    "Kari and Joe know each other.",
    "James has known Peter since school days.",
]


# Header
line = "-" * 30
print(f"\n\tFriendships: \n{line}")

for sentence in sentences:
    # Find the match using the compiled regex
    match = find_name.match(sentence)
    if match:
        # Add the names to groups and print them
        name1, name2 = match.groups()
        print(f"{name1:>12} - {name2}")
