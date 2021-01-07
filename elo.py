ratingA = int(input("What is your rating? "))
ratingB = int(input("what is your opponent's rating? "))
winner = input("who won? input 'win' if you won, 'lose' if you lost. ")

if winner == "win":
    winner = 1
elif winner == "lose":
    winner = 0

probability = 1 / (1 + 10 ** ((int(ratingB) - int(ratingA)) / 400))

print("probability of you winning: " + str(round(probability, 3)))

newRatingA = ratingA + 32 * (winner - probability)

diff = round(newRatingA) - ratingA

if diff > 0:
    diff = "+" + str(diff)
else:
    diff = str(diff)

print("new rating: " + str(round(newRatingA)) + " - " + diff)