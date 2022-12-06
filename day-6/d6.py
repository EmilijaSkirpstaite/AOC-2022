# opening input file and saving content as a string 
with open("day-6/input.txt") as file:
    input = file.read()

# PART 1 --------------------------------------------------------------------------------------------------

i = 0
while True:
    s = input[i:(i+4)]
    # if none of the 4 characters in the string are the same, break loop and get answer
    if s[0] != s[1] and s[0] != s[2] and s[0] != s[3] and s[1] != s[2] and s[1] != s[3] and s[2] != s[3]:
        ans = i + 4
        break
    i += 1

print("answer part 1: ", ans)

# PART 2 --------------------------------------------------------------------------------------------------

# function to iterate through characters in string to check for duplicates / faster than previous method for large strings
def checkChar(s):

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if(s[i] == s[j]):   # if 2 char are the same, return false and keep looping
                return False;
    return True;

count = 0
while True:
    s = input[count:(count+14)]
    if(checkChar(s)):
        ans2 = count + 14
        break    
    count += 1

print("answer part 2: ", ans2)
