# Exercise 4 from https://www.practicepython.org

# Gets number input from the user
number = int(input('Please enter a number '))
divider = number

# Creates a list of numbers for the output array
list = []

if divider > 0 :
    var1 = number % divider
    if var1 ==1:
        list.append(divider)
        divider = divider - 1
    else:
        divider = divider - 1
else:
    print('Program finished')

print(list)

