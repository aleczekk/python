num = int(input('Enter number to devide: '))
x = list(range(1, num+1))  # convert iterable string to list 
k = []
for element in x:
    if num % element == 0:  # if reminder num/element from list x is = 0, then append it to new list k
        k.append(element)  # list to store deviders
print('Dzielniki: ', k)
