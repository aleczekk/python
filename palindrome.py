string = input('Please enter a string: ')
print(type(string))
a = string[:]  # print the whole string (string is a list)
b = string[::-1]  # reverse print from the sting (list)
print(a)
print(type(a))  # should print str (string)
print(b)
print(type(b))

if a == b:  # check if string is a palindrome
    print('This word "' + string + '" is a palindrome')
else:
    print('This word "' + string + '" is not a palindrome')
