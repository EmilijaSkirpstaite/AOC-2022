# Key -------------------
# A  X   Rock	    X loss
# B  Y   Paper		Y draw
# C  Z   Scissors   Z win

# Points ----------------
# 1 A      0 lost
# 2 B      3 draw
# 3 C      6 won

# ALL OUTCOMES part 1
# A vs X = DRAW = (1 + 3) = 4 
# A vs Y = WIN  = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN  = (3 + 6) = 9
# C vs X = WIN  = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

# Storing data from txt file to list
file = open("day-2/input.txt", "r")
data = file.read()
rounds = data.split("\n")

# Creating dictionary of all outcomes
outcomes = {
    "A X" : 4, "A Y" : 8, "A Z" : 3,
    "B X" : 1, "B Y" : 5, "B Z" : 9,
    "C X" : 7, "C Y" : 2, "C Z" : 6
}

# Calculating total score
total_score = 0
for round in rounds:
    total_score += outcomes[round]

print("Answer Part 1: ", total_score)

# PART 2 ---------------------------------------------------------------------------

# ALL OUTCOMES part 2
# A vs X = LOSS = C (3 + 0) = 3 
# A vs Y = DRAW = A (1 + 3) = 4
# A vs Z = WIN  = B (2 + 6) = 8
# B vs X = LOSS = A (1 + 0) = 1
# B vs Y = DRAW = B (2 + 3) = 5
# B vs Z = WIN  = C (3 + 6) = 9
# C vs X = LOSS = B (2 + 0) = 2
# C vs Y = DRAW = C (3 + 3) = 6
# C vs Z = WIN  = A (1 + 6) = 7

# Creating dictionary of all outcomes
outcomes_p2 = {
    "A X" : 3, "A Y" : 4, "A Z" : 8,
    "B X" : 1, "B Y" : 5, "B Z" : 9,
    "C X" : 2, "C Y" : 6, "C Z" : 7
}

# Calculating total score
total_score_p2 = 0
for round in rounds:
    total_score_p2 += outcomes_p2[round]

print("Answer Part 2: ", total_score_p2)