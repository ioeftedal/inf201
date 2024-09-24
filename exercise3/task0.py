filename = "textfile.txt"

information = {
    "name": [],
    "institution": [],
    "domain": [],
}

with open(filename) as file:
    # Skip first two lines
    next(file)
    next(file)

    emails = []

    for row in file:
        words = row.split(" ")
        for word in words:
            # If the word contains an '@', treat it as an email
            if "@" in word:
                # Clean the word by stripping unnecessary characters
                email = word.strip()
                emails.append(email)

    # Process the emails to extract the name, institution, and domain
    for email in emails:
        # Split by '@' to get name and the rest
        name, rest = email.split("@", 1)
        institution, domain = rest.split(
            ".", 1
        )  # Split the rest into institution and domain

        # Append each part to the respective list in the dictionary
        information["name"].append(name)
        information["institution"].append(institution)
        information["domain"].append(domain)

# Print header
print(f"{'Name':<15} {'Institution':<20} {'Domain':<15}")
print("-" * 50)

# Print information in a table-like format
for i in range(len(information["name"])):
    print(
        f"{information['name'][i]:<15} {information['institution'][i]:<20} {information['domain'][i]:<15}"
    )
