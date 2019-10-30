# Exercise 5 from https://www.practicepython.org

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 3, 3, 3]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Creates a list to put elements that are repeating in both lists
list_of_commons = []

# checks if the elements in list b is also in lost a, but not in list_of_comons yet.
for i in b:
    if i in a:
        if i not in list_of_commons:
            list_of_commons.append(i)

# prints the new lost_of_commons to the screen
print(list_of_commons)