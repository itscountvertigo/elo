rating_a = int(input("What is your rating?\n"))
rating_b = int(input("what is your opponent's rating?\n"))
winner = input("who won? input 'win' if you won, 'lose' if you lost.\n")

if winner == "win":
    winner_a = 1
    winner_b = 0
elif winner == "lose":
    winner_a = 0
    winner_b = 1

probability_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
probability_b = 1 - probability_a

# print("probability of you winning: " + str(round(probability_a, 3)))
# print("probability of your opponent winning: " + str(round(probability_b, 3)))

new_rating_a = rating_a + 64 * (winner_a - probability_a)
new_rating_b = rating_b +64 * (winner_b - probability_b)

diff_a = round(new_rating_a) - rating_a
diff_b = round(new_rating_b) - rating_b


if diff_a > 0:
    diff_a = "+" + str(diff_a)

if diff_b > 0:
    diff_b = "+" + str(diff_b)


print("Your new rating: " + str(round(new_rating_a)) + ", " + str(diff_a))
print("Your opponent's new rating: " + str(round(new_rating_b)) + ", " + str(diff_b))