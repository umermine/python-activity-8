#Taking inputs
lower = int(input("Enter the upper range "))
upper = int(input("Enter the lower range "))
#Writing code
print("The prime numbers between '{upper}' and '{lower}' range are =")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2 , num):
            if (num % i ) == 0:
                break
        else:
            print(num)