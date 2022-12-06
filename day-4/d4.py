with open("day-4/input.txt") as file:
    pairs = file.read().splitlines()

# PART 1 ------------------------------------------------------------------------------------------------
# Find out amount of pairs for which atleast one elfs assigned range overlaps fully 

answer = 0

for pair in pairs:      # iterating through each element in list
    one, two = pair.split(",")      # splitting each element in half / elf 1 and elf 2
    elfoneL, elfoneR = one.split("-")   # separates each elfs section assignment ranges to 
    elftwoL, elftwoR = two.split("-")   # / left-right start-finish
    elfoneL, elfoneR, elftwoL, elftwoR = [int(x) for x in [elfoneL, elfoneR, elftwoL, elftwoR]]
    # check for pairs that FULLY overlap
    if elfoneL <= elftwoL and elftwoR <= elfoneR or elftwoL <= elfoneL and elfoneR <= elftwoR:
        answer += 1

print("Answer part 1: ", answer)


# PART 2 ------------------------------------------------------------------------------------------------
# Find out amount of pairs whose assigned ranges overlap in some way

answer_p2 = len(pairs) # initially saves the answer as the total amount of pairs / length of input

for pair in pairs:      
    one, two = pair.split(",")      
    elfoneL, elfoneR = one.split("-")   
    elftwoL, elftwoR = two.split("-")    
    elfoneL, elfoneR, elftwoL, elftwoR = [int(x) for x in [elfoneL, elfoneR, elftwoL, elftwoR]]
    # check for pairs that DONT overlap
    if elfoneR < elftwoL or elftwoR < elfoneL:
        answer_p2 -= 1 # subtract one from the total pairs

print("Answer part 2: ", answer_p2)