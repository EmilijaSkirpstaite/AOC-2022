# opening text file in read mode
input = open("day-1/input.txt", "r")

# reading the file
data = input.read()

# storing data from file into list, splitting it at new line
data_list = data.split("\n")

#traversing every string in our data 
max = 0
count = 0
totals = []
for item in data_list:
    if item == '':
        totals.append(count)    # adding total calories carried by each elf to the list
        count = 0   # resetting count
    else:
        num = int(item)
        count += num

    if count > max:
        max = count

# sorting list in descending order    
totals.sort(reverse = True)


top3 = 0
i = 0
while i < 3:
    top3 += totals[i] 
    i += 1
    
print("Answer to part 1: ", max)
print("Answer to part 2: ", top3)




