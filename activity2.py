#Taking output and Adding variables
string = input("Enter a word or a phrase ")
char = input("Enter a letter present in the word or phrase ")
count = 0
i = 0

#Writing code
for x in string:
    if(x == char):
        count = count + 1

#Writing output
print("The total number of times ",char," has occured is ",count)