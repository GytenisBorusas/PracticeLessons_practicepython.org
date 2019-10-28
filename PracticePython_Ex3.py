# Exercise 3 from https://www.practicepython.org

# A list of elements
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = []

number = int(input('Please define the comparison number '))

# Adds an element to the list_a
list_a.append(99)
# print(list_a)

# Checks the "list_a" for all the elements that are smaller than "number" and puts them back in the new array called
# "list_b"
for element in list_a:
    if element > number:
        list_b.append(element)

print(list_b)


