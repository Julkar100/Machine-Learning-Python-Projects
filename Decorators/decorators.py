# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:11:00 2018

@author: CodersMine
"""
#part 1
def succ(x):
    return x+1

succer=succ
succer(10)
#part 2
def f():
    def g():
        print("hi its g")
        print("Thanks for calling me")
    print("this is f")
    print("calling g now")
    g()
    
f()
#part 3
def temp(t):
    def cels2fahr(x):
        return 9*x/5 + 32
    result ="its "+str(cels2fahr(t))+" degrees"
    return result

print(temp(-40))

#part 4
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
          
f(g)

#part 5
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now  " +func.__name__)
    func()
          
f(g)

#part 6
import math 
def foo(fun):
    print("the func "+ fun.__name__ + " was passsed to foo")
    res=0
    for x in [1,2,2.5]:
        res+=fun(x)
    return res
print(foo(math.sin))
print(foo(math.cos))


#part 7
def f(x):
    def g(y):
        return y + x + 3 
    return g

nf1= f(1)
nf2 = f(3)

print(nf1(2))
print(nf2(1))
"""
f(1)(1)
"""
#part 8 polynomial factory function

def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial
    
p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))
    
#decorator 9
 
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))



#before decoration
foo("high")

#decorate with foo
#foo=our_decorator(foo)



foo(42)

#after decoration
"""
Summarizing we can say that a decorator in Python is a callable Python object that is used to modify a function, method or class definition. The original object, the one which is going to be modified, is passed to a decorator as an argument. The decorator returns a modified object, e.g. a modified function, which is bound to the name used in the definition. 
"""


def sum(a):
    print(a)
    return a

sum=our_decorator(sum)


sum(2)


#part 10

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y=1):
    return x*y + 1

print(succ.calls)
for i in range(10):
    succ(i)
mul1(3, 4)
mul1(4)
mul1(y=3, x=2)
    
print(succ.calls)
print(mul1.calls)


from functools import __name__

@__name__
def new():
    print("hellos")

foo("hello")
new()

