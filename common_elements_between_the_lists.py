import random  # import the random module to use function

a = random.sample(range(30), 5)  # generates random list in range 0 to 30
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for element in b:
    if element in a:
        c.append(element)  # add element to list after if
print(c)
