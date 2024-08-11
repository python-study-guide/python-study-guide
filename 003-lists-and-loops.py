fruits=['apples', 'bananas', 'oranges']

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits.append('strawberries')

print(fruits)
print(fruits[3])

fruits.remove('bananas')
print(fruits)


del fruits[1]   # "del" is a python keyword, aka simple statements - https://docs.python.org/3/reference/simple_stmts.html#the-del-statement
print(fruits)


if 'apples' in fruits:
    print('apples is in the list')
else:
    print('apples is not in the list')


if 'oranges' in fruits:
    print('oranges is in the list')
else:
    print('oranges is not in the list')

# here's how to write a for-loop. 
for fruit in fruits:
    print(fruit)

