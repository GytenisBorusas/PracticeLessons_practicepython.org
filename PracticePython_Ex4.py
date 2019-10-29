# Exercise 4 from https://www.practicepython.org

# Gets number input from the user
number = int(input('Please enter a number '))
divider = number

# Creates a list of numbers for the output array
x = range(2,number+1)

# Creates two list. For divisors and not
list_a = []
divisors = []

# Circles through the list checking if its a divisor or not
for elem in x:
    if number % elem > 0:
        list_a.append(elem)
    else:
        divisors.append(elem)

# Prints the results
print(list_a)
# print(divisors)







#for elem in x:
#   print(elem)