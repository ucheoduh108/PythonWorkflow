
#CHANGING THE GLOBAL VARIABLE WITHOUT AFFECTING THE LOCAL VARIABLE

#a = 10

#def something():
#    a = 9

#    X = globals()['a']
#    globals()['a'] = 17

#    print('in fnx', a)

#something()

#print('outside', a)



#PASSING LIST TO FNX
#def count(lst):
 #    even = 0
#     odd = 0

 #    for i in lst:
 #        if i % 2 == 0:
 #            even+=1

 #        else :
#             odd+=1

 #    return even,odd

#lst = [12,23,45,24,57,33,44,68,71]

#even,odd = count(lst)

#print(even)
#print(odd)

#OR

#print('Even: {} and Odd: {}'.format(even,odd))




#FIBONACCI SEQUENCE
#def fib(n):

#    a = 0
#    b = 1

#    if n == 1:
#        print(a)

#    else:
#        print(a)
#        print(b)

#        for i in range(2,n):
#            c = a + b
#            a = b
 #           b = c

#            print(c)

#fib(100)



#printing the 100th fibonacci sequence
#def fib(n):

#    a = 0
#    b = 1

#    if n == 1:
#        print(a)

#    else:
#        print(a)
#        print(b)

 #       for i in range(2,n):
  #          c = a + b
   #         a = b
    #        b = c

     #   print(c)

#fib(100)



#FACTORIAL
#def fact(n):
#    f = 1

 #   for i in range(1,n+1):
 #       f = f * i

  #  return f

#x = 5
#result = fact(x)
#print(result)



#RECURSION

#import sys
#print(sys.getrecursionlimit())
#print(sys.setrecursionlimit(2000))

#i = 0
#def greet():

 #   global i
  #  i+=1

   # print('Hello', i)
    #greet()

#greet()



#FACTORIAL USING RECURSION
#def fact(n):

 #   if n == 0:
  #      return 1

   # return n * fact(n-1) #this is equivalent to 5*4!

#result = fact(5)
#print(result)



#ANONYMOUS FUNCTIONS(Lambda)

#def sqrt(a):
 #   return a * a

#result = sqrt(5)
#print(result)

 #OR

#f = lambda a : a * a
#result = f(6)
#print(result)

#x = lambda a,b : a + b
#result = x(7,9)
#print(result)

#r = lambda  i : i % 2 == 0
#result = r(5)
#print(r)



#FILTER, MAP,REDUCE

#from functools import reduce

#num = [2,4,7,12,32,44,52,33]
#even = list(filter(lambda n : n % 2 == 0, num))
#print(even)

#doubles = list(map(lambda n : n * 2, even))
#print(doubles)

#sum = reduce(lambda a,b : a + b, doubles)
#print(sum)



#DECORATORS
#1
#def div(a,b):
#    print(a / b)

#def smart_div(func):

#    def inner(a,b):
#        if a < b :
#            a,b = b,a
#        return func(a,b)
#    return inner

#div = smart_div(div)
#div(5,25)



#2
#def func():
#    print('The Rock')

#def wrapper(func):
#    func()

#wrapper(func)



#3
#def func():
#    print('Rocks')

#def wrapper(func):
#    print('Jesus')
#    func()
#    print('Extra-ordinary')

#wrapper(func)



#4
#def func():
#    print('Rocks')

#def wrapper(func):
#    print('Jesus')
#    func()
#    print('Extra-ordinary')

#def function_generator():
#    def new_function():
#        print('The Verdict')
#    return new_function

#var = function_generator()
#var()



#5
#def decorator(baller):

#    def wrapper():
#        print('Call')
#        baller()
 #       print('The Boss' )

#    return wrapper

#@decorator # this is replacing the variable baller on line 699
#def baller():
 #   print('Ouch')

#baller = decorator(baller)
#baller()



#6
#def smart_div(div):
#    def inner(a,b):

 #       if a < b:
  #          a,b = b,a

   #     div(a,b)
    #return inner

#@smart_div
#def div(a,b):
 #   print(a/b)

#div(3,6)



#7
#import time

#def decorator(baller):

    #def wrapper():
    #    print('Call')
   #     baller()
  #      print('The Boss' )

 #   return wrapper

#def duration_dec(baller):
    #def inner():

     #   start_time = time.time()

    #    baller()

   #     duration = time.time() - start_time
  #      print(f'duration {duration}')

 #   return inner

#@decorator
#@duration_dec
#def baller():
  #  print('Ouch')
 #   time.sleep(1)

#baller()



#8
#import time

#def decorator(baller):

 #   def wrapper():
  #      print('Call')
   #     baller()
    #    print('The Boss' )

    #return wrapper



#def duration_dec(baller):
 #   def inner():

  #      start_time = time.time()

   #     baller()

    #    duration = time.time() - start_time
     #   print(f'duration {duration}')

    #return inner



#def double_decorator(baller):
 #   def wrapper():
  #      baller()
   #     baller()
    #return wrapper

#@double_decorator
#@decorator
#@duration_dec
#def baller():
 #   print('Ouch')
  #  time.sleep(1)

#baller()



#9 - *ARGS & **KWARGS
#def prdt_modifier(name):

#    def inner(*args, **kwargs):
#        name(*args,**kwargs)
#    return inner

#@prdt_modifier
#def name(product,classA):
#    print('Neurotex forte')

#name('product','category')



#10
#def repetition_decorator(repetition):
#    def decorator(greet):
 #       def wrapper():

  #          for i in range(repetition):
   #             greet()
    #    return wrapper
    #return decorator

#@repetition_decorator(7)
#def greet():
#    print('Hello Uche')

#greet()



#MODULES

#a = 4
#b = 7
#soln1 = add(a,b)
#print(soln1)


#a = 8
#b = 3
#soln2 = div(a,b)
#print(soln2)


#a = 13
#b = 7
#soln3 = sub(a,b)
#print(soln3)



#SPECIAL VARIABLE __name__


#def sponsors():
#    print('Angel1', 'Oso')


#def probability():
#    print('Possibility', 1)


#def main():
#    sponsors()
#    probability()


#main()

#def main():
 #   print('Hello')
  #  print('John')

#if __name__ == '__main__' :
 #   main()


#import demo
#print('Hello',__name__)
#print("You're welcome",__name__)

#def main():
#    print("Hello")
#    print("It's time to calculate")

#if __name__ == '__main__':
#    main()

#from demo import  add
#def func1():
#    add()
#    print('from func1')

#def func2():
#    print('from func2')

#def dev():
#    func1()
#    func2()

#dev()
