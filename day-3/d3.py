from string import ascii_lowercase, ascii_uppercase

letters = ascii_lowercase + ascii_uppercase

# opening input file and storing it in a list
file = open("day-3/input.txt", "r")
data = file.read()
rucksacks = data.split("\n")
compartments = data.split("\n")

# Splitting each rucksack into two compartments separated by a space
# Splitting each element in half separated by a space
i = 0
for compartment in compartments:
    c1 = compartment[0:len(compartment)//2]
    c2 = compartment[len(compartment)//2:]
    compartments[i] = (c1 + " " + c2)
    i += 1

length = len(compartments)
sum = 0

# Separating each rucksack into its own list with 2 elements simbolising the 2 compartments
j = 0
while j < length:
    c = compartments[j].split(" ")
    compartments[j] = c
    j += 1


# checking for letter that appears in both compartments
k = 0

while k < length-1:
    
    for priority, char in enumerate(letters):
        if char in compartments[k][0] and char in compartments[k][1]:
            sum += priority + 1   
            k +=  1

#for i, l in enumerate(letters):
#        if l in rucksacks[length-1][0] and l in rucksacks[length-1][1]:
#            sum += letters.index(l) + 1   
 
print("Answer Part 1: ", sum)



# PART 2 ----------------------------------------------------------------------------------------------------------------------

sum_p2 = 0
for i in range(0, length, 3):
    r = rucksacks[i:(i + 3)]

    for priority, char in enumerate(letters):
        if char in r[0] and char in r[1] and char in r[2]:
            sum_p2 += priority + 1

print("Answer Part 2: ", sum_p2)