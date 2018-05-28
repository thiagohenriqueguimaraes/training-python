words = ['abc', 'b', 'c']
# for w in words:
#     print(w)

# for w in words[:]:
#     if len(w) > 2:
#             words.insert(0,w)

# print(words)

# for i in range(5,50, 5):
#     print(i)

# for index in range(len(words)):
#     print(words[index])

# for n in range(2,20):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#         else:
#             print(n, 'is a primer number')


# for n in range(2, 10):
#     if n % 2 == 0:
#         print("Found an even number", n)
#         continue
#     print('Found a number', n)

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# fib(2000)


# def fib(n):
#     r = []
#     a, b = 0, 1
#     while a < n:
#         r.append(a)
#         a, b = b, a+b
#     return r

# print(fib(100))


# def aks_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# aks_ok('Do you really want to quit?')

# i = 5

# def f(arg=i):
#     print(arg)
# i=6
# f(7)

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=1, action="V00000M")
# parrot(action='V00000M', voltage=100000)
# parrot('a million', 'bereft of life', 'jump')
# parrot('a thousand', state='pushing up the daisies')

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", 
#            "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

# def concat(*args, sep="/"):
#     return sep.join(args)

# print(concat("earth", "mars", "venus", sep="-"))
# args = [3, 6]
# print(list(range(*args)))


# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)


# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(0))
# print(f(1))

# pairs = [(1, 'one'), (2,'two'), (3, 'three')]
# pairs.sort(key=lambda pair: pair[0], reverse=True)
# print(pairs)

# def my_function():
#     """
#     Favela is Here!

#     Thiago
#     """
#     pass
# print(my_function.__doc__)

# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs

# f('spam')

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# print(fruits.count('apple'))
# print(fruits.count('apple2'))
# print(fruits.index('banana'))
# print(fruits.index('banana', 4))
# fruits.reverse()
# print(fruits)
# fruits.append('grape')
# print(fruits)
# fruits.sort()
# print(fruits)
# print(fruits.pop())

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("thiago")
# queue.append("Guimaraes")
# print(queue.popleft())
# print(queue.popleft())
# print(queue)

# squares = [x**2 for x in range(10)]
# print(squares)

# print([(i, j) for i in [1,2,3] for j in [3,2,1] if i != j])


# import math

# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)

# print(filtered_data)


# print((1, 2, 5) < (1, 2, 4))

# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     return result


# from fibo import fib as fibonacci

# fibonacci(1000)
    
# table = {'x': 1, 'y': 3, 'w' : 8}
# for name, phone in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, phone))

#f = open('wf', 'w')
# import json
# with open('wf', 'w') as f:
#     json.dumps([1, 'simple', 'list'])
#     f.writeline(json.dumps([1, 'simple', 'list']))
#     # for line in f.read():
#     #     print(line, end='')
# f.closed

# while True:
#     try:
#         x = int(input("Entre com um número"))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After glocal assignment:", spam)

# scope_test()
# print("In global scope:", spam)

# class MyClass:
#     """A simple example class"""
#     i = 12345
#     def __init__(self):
#         self.i = 1
#     def f(self):
#         return self.i

# x = MyClass()
# print(x.f())


# class Comlex:
#     def __init__(self, r2, i2):
#         self.r = r2
#         self.i = i2

# x = Comlex(3.0, 2.0)
# # print(x.r)

# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2

# print(x.counter)
# del x.counter


# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []

#     def add_trick(self, trick):
#         self.tricks.append(trick)


# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)


# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'

#     h = g

# print(C().h())

# class Bag:
#     def __init__(self):
#         self.data = []
    
#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)



# bag = Bag()
# bag.add(1)
# bag.addtwice(2)
# print(bag.data)


# class A:
#     def __init__(self):
#         self.name = 'thiago'

# class B(A):
#     def __init_subclass__(self):
#         self.name = 'Henrique'

# print(A().name)
# print(B().name)


# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
    
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
    
#     __update = update

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.items_list.append(item)

# class Employee:
#     pass

# john = Employee()

# john.name = 'x'
# john.dept = 'y'
# john.salary = 10
# import sys
# sys.stderr.write('Warning, log file not found starting a new one\n')

import os
colors = {
        'red'       :   '\033[91m',
        'green'     :   '\033[92m',
        'yellow'    :   '\033[93m',
        'blue'      :   '\033[94m',
        'purple'    :   '\033[95m',
        'cyan'      :   '\033[96m',
        'white'     :   '\033[97m',
        'wild'      :   '',
        'dwild'     :   '',
        'dred'       :   '\033[31m',
        'dgreen'     :   '\033[32m',
        'dyellow'    :   '\033[33m',
        'dblue'      :   '\033[34m',
        'dpurple'    :   '\033[35m',
        'dcyan'      :   '\033[36m',
        'dwhite'     :   '\033[37m',
    }
print('\033[91mThiago')



