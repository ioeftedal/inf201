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
