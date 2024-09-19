import random as rd

scorecard = {
    "Sarah": {"sum": 0, "rolls": []},
    "Titus": {"sum": 0, "rolls": []},
    "Hanna": {"sum": 0, "rolls": []},
}


def roll(scorecard: dict, rounds=None):
    if rounds is None:
        rounds = 4

    for i in range(rounds):
        for key in scorecard:
            diceRoll = rd.randint(1, 6)
            scorecard[key]["sum"] += diceRoll
            scorecard[key]["rolls"].append(diceRoll)


roll(scorecard)

sortedScorecard = dict(
    sorted(scorecard.items(), key=lambda item: item[1]["sum"], reverse=True)
)

count = 1

for player, data in sortedScorecard.items():
    print(
        f"{count}. plass går til {player}. De kastet følgende tall: {data['rolls']}, dette gjorde at de endte med en sum på: {data['sum']}"
    )
    count += 1
