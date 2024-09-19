line = '-' * 27

tab = "\t"

print(line)
print(f"{tab}x{tab}x^2{tab}x^3")
print(line)
for i in range(11):
    print(f"{tab}{i}{tab}{i**2}{tab}{i**3}")
print(line)
