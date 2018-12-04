lista = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []
for element in lista:
    if element % 2 == 0:  # check if reminder (element/2) == 0, then append it to even list
        even.append(element)
print(even)

# write the code above in one line
even = [element for element in lista if element % 2 == 0]
print(even)
print(type(even))

# case when generate random length list, random list elements and use random module

numlist = []
list_length = random.randint(5, 15)  # generates random length of the list

while len(numlist) < list_length:  # while loop with condition
    numlist.append(random.randint(1, 75))  # appends a new element to the numlist while when while loop condition is true

even = [element for element in numlist if element % 2 == 0]
print(even)
