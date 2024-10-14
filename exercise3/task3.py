import re

filename = "dummy.py"

pattern1 = re.compile("import")
pattern2 = re.compile("from")

with open(filename) as file:
    for line in file:
        match1 = pattern1.search(line)  # Search for 'import' in each line
        match2 = pattern2.search(line)  # Search for 'import' in each line
        if match1:
            print("Found an 'import' statement:", line.strip())  # Print the line
        if match2:
            print("Found an 'from' statement:", line.strip())  # Print the line
