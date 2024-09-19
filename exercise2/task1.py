import csv

filename = "2021-09-14_party_distribution_1_st_2021.csv"
line = "-" * 30


def partiOgStemmer(filename, antall_partier=None):
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";", quotechar="|")
        next(csvfile)

        partiStemmer = {}
        sumVotes = 0

        for row in reader:
            sumVotes += int(row[12])
            if row[6] in partiStemmer:
                partiStemmer[row[6]] += int(row[12])
            else:
                partiStemmer[row[6]] = int(row[12])

    partiStemmerSorted = dict(
        sorted(partiStemmer.items(), key=lambda item: item[1], reverse=True)
    )

    if antall_partier is None:
        antall_partier = len(partiStemmer)
    count = 0

    for key, value in partiStemmerSorted.items():
        prosent = value / sumVotes * 100

        if count >= antall_partier:
            break

        if prosent > 4:
            print(
                f"Marked: * \nPartikode: {key} \nTotalt antall stemmer: {value} \nProsentandel stemmer: {prosent:.2f}% \n{line}"
            )
        else:
            print(
                f"Partikode: {key} \nTotalt antall stemmer: {value} \nProsentandel stemmer: {prosent:.2f}% \n{line}"
            )

        count += 1


partiOgStemmer(filename, 3)
partiOgStemmer(filename, 7)
partiOgStemmer(filename)
