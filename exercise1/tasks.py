# Task 1:
name = input("Please enter your name: ")

print(f"Welcome to INF201, {name}!")

# Task 2:
def prettyGreeting(name):
    text = f"Welcome to INF201, {name}!"
    nrChar = len(text) + 4  

    dynLine = '*' * nrChar  

    print(dynLine)
    print(f"* {text} *")
    print(dynLine)

prettyGreeting(name)

# Task 3:
line = '-' * 27

tab = "\t"

print(line)
print(f"{tab}x{tab}x^2{tab}x^3")
print(line)
for i in range(11):
    print(f"{tab}{i}{tab}{i**2}{tab}{i**3}")
print(line)

# Task 4:
with open("norway_municipalities_2017.csv", 'r') as csvfile:
    next(csvfile)  

    placePopulation = {} 

    for row in csvfile:
        words = row.split(',')

        place = words[1]  
        population = int(words[2])  

        if place in placePopulation:
            placePopulation[place] += population 
        else:
            placePopulation[place] = population  

line = "-" * 50
placePopulationSorted = dict(sorted(placePopulation.items(), key=lambda item: item[1], reverse=True))

print(f"{'':>5}Fylke:{'':<25}Populasjon:")
for key, value in placePopulationSorted.items():
    print(line)
    print(f"{'':>5}{key:<25}", end="|")
    print(f"{'':>5}{value}")

# Task 5:
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 6))
plt.barh(list(placePopulationSorted.keys()), list(placePopulationSorted.values()))
plt.show()
