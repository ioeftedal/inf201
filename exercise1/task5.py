import matplotlib.pyplot as plt

with open("norway_municipalities_2017.csv", newline="") as csvfile:
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

placePopulationSorted = dict(sorted(placePopulation.items(), key=lambda item: item[1], reverse=True))

plt.figure(figsize=(20, 6))
plt.barh(list(placePopulationSorted.keys()), list(placePopulationSorted.values()))
plt.show()
