N = 9   
drawing_lines = 8

with open("day-5/input.txt") as file:
    parts = file.read()[:-1].split("\n\n")      # splitting input file into two parts
    drawing = parts[0].split("\n")              # part 0 for stack drawing
    stacks = [[] for _ in range(N)]
    stacks2 = [[] for _ in range(N)]

    for i in range(drawing_lines):
        line = drawing[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks[s].append(crates[s])
    
    for i in range(drawing_lines):
        line = drawing[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks2[s].append(crates[s])

# Reverse all stacks
stacks = [stack[::-1] for stack in stacks]
stacks2 = [stack2[::-1] for stack2 in stacks2]

# PART 1 --------------------------------------------------------------------------------------------------

# Moving crates
# Getting instructions from input file
for line in parts[1].split("\n"):               # part 1 for moving instructions
    instructions = line.split(" ")
    amount, source, dest = map(int, [instructions[1], instructions[3], instructions[5]])
    source -= 1
    dest -= 1

    for _ in range(amount):
        stacks[dest].append(stacks[source].pop())


answer = ""

# getting the top crate of each stack
i = 0
for i in range(len(stacks)):
    answer += (stacks[i][len(stacks[i])-1])
    i +=1

print("Answer part 1: ", answer)

# PART 2 ---------------------------------------------------------------------------------------------------


for line in parts[1].split("\n"):               # part 1 for moving instructions
    instructions = line.split(" ")
    amount, source, dest = map(int, [instructions[1], instructions[3], instructions[5]])
    source -= 1
    dest -= 1

    stacks2[dest].extend(stacks2[source][-amount:])
    stacks2[source] = stacks2[source][:-amount]

answer_p2 = ""

# getting the top crate of each stack
i = 0
for i in range(len(stacks2)):
    answer_p2 += (stacks2[i][len(stacks2[i])-1])
    i +=1

print("Answer part 2: ", answer_p2)