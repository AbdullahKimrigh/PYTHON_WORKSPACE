# # DataTypes
# int = 78899, -43254
# float = -.0, 2423.23
# string = 'th', 'string', "Hello"
# bool = True, False

# # OUTPUT & PRINTING 
# print('HELLO WORLD')
# print('HELLO WORLD', 87, False, end='|')
# print(4.5)

# # VARIABLES
# x = 5
# hello = 'time'
# var = Value

# ## FUNCTION
# # USER INPUT
# input()
# x = int(input('Enter a number: '))
# y = int(input('Enter another number: '))

# # ARTHMETIC OPERATOR
# x = 9
# y = 5
# SUMresult = x + y
# DIVISONresult = int(x / y)
# SUBresult = x - y
# MULTresult = x * y
# EXPresult = x ** y
# result = x // y
# MODresult = x % y
# result = (x % y) * 2
# num = input('Number: ')
# print(float(num) - result)

# # STRING METHODS
# hello = 'hello'
# print(type(hello))
# print(hello.upper())
# print(hello.lower())
# print(hello.title())
# print(hello.isupper())
# print(hello.islower())
# print(hello.istitle())
# print(hello.isalnum())
# print(hello.isalpha())
# print(hello.isnumeric())
# print(hello.isspace())
# print(hello.capitalize())
# print(hello.count('l'))
# print(hello.find('h'))
# print(hello.index('e'))
# print(hello.replace('l', 'o'))
# print(hello.split(' '))
# print(hello.split(' ', 2))
# print(x * y)
# print(x + y) #concat

# # CONDITIONAL OPERATORS (comparison)
# x = 'hello'
# y = 'hello'

# print(x == y)
# print(x != y)
# print(x <= y)
# print(x >= y)
# print(x > y)
# print(x < y)
# print(ord('a'))

# # CHAINED CONDITIONALS
# x = 5
# y = 10
# z = 0

# print(result = y or not z)
# print(result = y or z)
# print(result = y and z)
# print(result = y and not z)

# # IF/ELSE/ELIF
# x = input('Name: ')

# if x == 'tim':
#     print('You are great!')
# elif x == 'john':
#     print('You are awesome!')
# elif x == 'abdullah':
#     print('You are scientist!')
# else:
#     print("NO")

# # LIST/TUPLE
# x = ['a', 'b', False, 5, 'e'] #list
# x.append('hello')
# x.extend(['e',5,5,5,5])
# print(x.pop())
# print(x.pop(2))
# print(len(x))
# print(x[0])
# print(x[:3])
# print(x[3:])

# y = ('a', 'b', True, 8, 'e') #tuple are immutable list

# ## LOOPS
# # FOR #know how many we'll looping
# start, stop, step
# for i in range(1, 10, +1):
#     print(i)
# for i in [3, 4, 5, 6, 7, 8]:
#     print(i)
# x = [3, 4, 5, 6, 7, 8]
# for i in range(len(x)):
#     print(i)
# for i, element in enumerate(x):
#     print(i, element)

# # WHILE # unknow how many we'll looping
# while i < 10:
#     print(i)
#     i += 1
#     # BREAK
#     if i == 10:
#         break
#     # CONTINUE
#     if i == 5:
#         continue

# # SLICE OPERATOR
# take a slice of something and do thing on it
# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# s = "hello"

# sliced = x[0:3:2] #start:stop:step
# sliced = x[:4] #end at 4
# sliced = x[2:] #start at 2
# sliced = x[::-1] #step reverse
# sliced = (1,2,3,4,5,0,9,8)[::-1] #step reverse

# print(sliced)

# just to show if exist or not
# # SETS
# x = set()
# s = {4, 23, 6, 6}
# s2 = [3, 6, 76]
# print(s)

# # DICTIONARIES
# x = {'key': 4}
# print(x['key'])

# # COMPREHENSIONS
# x = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# x = [i for i in x 
#      if i not in y]
# x = [i for i in x 
#      if i not in y 
#      if i not in x]
# print(x)

# # FUNCTIONS
# def add(x, y, z=None):
#     return x + y

# print(add(5, 8, 1))

# # ARGS $ **KWARGE
# def func(x):
#     def func2():
#         print(x)

#     return func2

# func(3)()

# def func(*args, **kwargs):
#     pass
#     print(args, kwargs)

# def func(x, y):
#     print(x, y)
# x = [(1,23), (2345,4745)]
# for x in x:
#     func(*x) #unpacked list or tuple
#     func(**{'x':2, 'y':5}) #unpacked dictionary

# # SCOPE & GLOBALS
# x = 5
# def func(name):
#     global x
#     x = 6
    
# print(x)
# func('changes')
# print(x)

# # EXCEPTION
# raise Exception('Bad')
# raise FileExistsError('')

# try:
#     x = 7 / 0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')

# # LAMBDAS
# x = lambda x: x * 2
# print(x(2))

# # MAP & FILTER
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mp = map(lambda i: i * 2, x)
# print(list(mp))

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mp = filter(lambda i: i + 2 == 2, x)
# print(list(mp))

# # F STRING
# x = 5
# y = 6
# z = 7
# print(f'{x} + {y} = {x + y}')
# print(f'{x} - {y} = {x - y}')
# print(f'{x} * {y} = {x * y}')
# print(f'{x} / {y} = {x / y}')
# print(f'{x} // {y} = {x // y}')
# print(f'{x} % {y} = {x % y}')

# # READ FILES
# with open('test.txt', 'r') as f:
#     print(f.read())
    
# # WRITE FILES
# with open('test.txt', 'w') as f:
#     f.write('Hello World')
#     close()

# # READ WRITE FILES
# with open('test.txt', 'a') as f:
#     f.write('Hello World')
#     close()
