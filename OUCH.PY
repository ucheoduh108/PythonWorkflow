'''ITERATOR'''

import time

# list = [1,2,3,4]

# a = list.__iter__()
# b = a.__next__()
# c =  a.__next__()
# d = a.__next__()
# e = a.__next__()
# print(b)
# print(c)
# print(d)
# print(e)






'''GENERATOR'''

# def names(uche,tayo,ugo,angel,jide):
#     yield uche
#     yield tayo
#     yield ugo
#     yield angel
#     yield jide

# a = names('uche','tayo','ugo','angel','jide')
# b = a.__iter__()
#
# c = b.__next__()
# d = b.__next__()
# e = b.__next__()
# f = b.__next__()
# g = b.__next__()
#
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

# create a file that will store the user data and use a generator fnx to get the data from the file and use iteration /
# to get the data from the generator object




'''DECORATOR'''

# def read(write):
#     def previous():
#         with open('data.txt','r') as file:
#             result = file.read()
#             print(result)
#         write()
#     return previous
#
#
# @read
# def write():
#     value = input('enter text: ')
#     with open('data.txt','a') as f:
#         f.write(value +'\n')
#
# write()



# PROBLEMS

# 1. write a program with nested dictionaries
# a = {'class A':{'beta lactam':{'penicillin':'amoxicillin'}}},{'class B':{'cephalosporin':'cefixime'}}
# b = a.__iter__()
# c = b.__next__()
# d = b.__next__()
# print(c)
# print(d)
#
#
# # 2. write a program to reverse a list
# d = ['name','program','platform','duration','expectation']
# print(d[::-1])
#
#

# # write a program for list of dictionaries
# e = [{'name':'uche'},{'program':'data science'},{'duration':'10 months'},{'platform':'aptech'},{'course':'python'}]
# print(e[3])
# print(e[-3:])
# print(e[::-2])
# import time


#
# def climate(weather):
#     def flood():
#         weather()
#         print('the storm is coming')
#         print('we have to do something')
#     return flood
#
# #@climate
#


# def duration_decorator(weather):
#     def wrapper():
#         weather()
#         start_time = time.time()
#         duration = time.time() - start_time
#         print(f'the duration is {duration}')
#     return wrapper
# @climate
# @duration_decorator
#
# def weather():
#     print('disaster')
# weather()



'''DOCORATORS IN FUNCTIONS WITH PARAMETERS'''

# def climate(weather):
#     def flood(*args,**kwargs):
#         weather(*args,**kwargs)
#         print('the storm is coming')
#         print('we have to do something')
#     return flood
#
# @climate
#
# def weather(temperature,humidity):
#     print('disaster')
#
#
# weather('x','y')



'''DECORATORS WITH PARAMETERS'''

# def repetition_decorator(repetitions):
#     def decorator(func):
#         def wrapper():
#             for r in range(repetitions):
#                 func()
#         return wrapper
#     return decorator
#
# @repetition_decorator(4)
#


# def func():
#     print('Gladiaors')
# func()


# def priest(amen):
#     def altar(a,b):
#         print('devotion')
#         amen(a,b)
#     return altar
#
# def amen(a,b):
#     print(a+b)
#
# amen = priest(amen)
# amen(3,4)



# def x (*num):
#     print(num[2])
#     print([num])
#
# x(1,2,3)



# def x(avg,sum):
#     print(avg,sum)
# x(4,5)



'''IMPORT OS'''
# import os
# from datetime import datetime
# # os.rename('OUCH.PY','main.py')
# mod_time = (os.stat('OUCH.PY').st_mtime)
# print(datetime.fromtimestamp(mod_time))



# for dirpath,dirnames,filename in os.walk("C:/Users/user/PycharmProjects/pythonProject/OUCH.PY"):
#      print('Current Path:',dirpath)
#      print('Directories:',dirnames)
#      print('files',filename)
#      print()


# print(os.environ.get('HOME'))
# file_path  =os.path.join(os.environ.get('HOME'),'data.txt')
# print(file_path)


# print(os.path.splitext('/tdt/test.txt'))
# print(dir(os.path))


# def add_num(*obj):
#     res=0
#     for i in obj:
#         res += i
#
#     return res
#
# print(add_num(3,4,5,6,7))



# def names(*kwargs):
#     print(kwargs)
#
# names({'university' : 'uniben', 'professsion' : 'Pharmacist'})
# with open(r"Oxford English Dictionary.txt") as f:
#     content = f.read(500)



'''CLOSURE'''
# def outer_func():
#      x = 4
#      def inner(outer_func):
#         a = 3
#          print(x*4)
#     #print(a)
#     return inner
# res =outer_func()
# res(5)



# with open ('Oxford English Dictionary.txt','rb') as f:
#     content = f.read(1000)
#     print(content)



'''arg and kwargs'''

# def func(var):
#     print(var)
#
# func('abc')
#


# def func(*args):
#      for item in args:
#          print(item)
#         # print(type(item))
# func('abc',(1,2,3),['uche','osne','ama'],{'weapon':'sword'})
# func()
#


# def func_a(name,*args):
#     print(name)
#
#     for items in args:
#         print(args)
#


# tup = 10,20,30,40
# func([45,*tup])
#


# def details(**kwargs):
#     print(kwargs)
#
# details(**{'name':'uche','profession':'data scientist','platform':'aptech'})
#
# def odogwu(*args,**kwargs):
#     print(args)
#     print(kwargs)
#

# odogwu(*[10,30,55],**{'category':'pharmaceuticals','defence':'navy'})
#


# class Car:
#     def __init__(self,colour,mileage):
#         self.colour = colour
#         self.mileage = mileage
#
# class AlwaysBlueCar(Car):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.colour = 'blue'



'''COMPREHENSION'''
# nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in nums :
#     my_list.append(n)
# print(my_list)



'''COMPREHENSION'''
# my_list = [n for n in nums]
# print(my_list)


# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)


# my_list = [n*n for n in nums]
# print(my_list)


# my_list = []
# for n in nums:
#     if n % 2==0:
#         my_list.append(n)
# print(my_list)
#

# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)


# my_list = []
# for letter in 'abcd':
#     for nums in range(4):
#         my_list.append(letter)
# print(my_list)
#
# my_list = [(letter,nums) for letter in 'abcd' for num in range (4)]
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)



# num = [1,1,1,2,2,3,3,4,5,5,6,6,7,8,9,10]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)
#
# my_set = {n for n in nums}
# print(my_set)

# try:
#     file = open('myfile.txt')
#     print(file.read)
#
# except:
#     print()



'''GUI'''

# from tkinter import *
#
# root = Tk()
#
'''creatin a label widget by defining it'''
# myLabel = Label(root, text = 'Hello World!')
#
'''shoving it into the screen'''
# myLabel.pack()
#
# root.mainloop()
#
'''postioning with Tkinker's Grid system'''
# from tkinter import *
#
# root = Tk()
#
# myLabel1 = Label(root, text = 'Hello World!')
# myLabel2 = Label(root, text = 'My name is Uche Oduh')
#
#
# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 0)
#
# root.mainloop()

'''creating Buttons'''
# from tkinter import *
#
# root = Tk()
#
# e = Entry(root,width = 227,borderwidth =50,fg = 'black',bg = 'white',)
# e.pack()
# e.insert(0, 'Enter Your Name : ')
#
# def myClick():
#     myLabel = Label(root, text = 'Hello' + e.get())
#     myLabel.pack()
#
# myButton = Button(root, text = 'Enter Your Name',command = myClick,fg = 'blue',bg = 'white',padx=50,pady=20)
#
# myButton.pack()

# root.mainloop()

'''GUI CALCULATOR'''

# from tkinter import *
#
# root = Tk()
# root.title('Simple Calculator')
#
# e = Entry(root, width = 35, borderwidth = 5)
# e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
#
# def button_click(number):
#     current = e.get()
#     e.delete(0,END)
#     e.insert(0,str(current)+str(number))
#
# def button_clear():
#     e.delete(0,END)
#
# def button_add():
#     first_number = e.get()
#     global f_num
#     f_num = int(first_number)
#     e.delete(0,END)
#
# def button_equal():
#     second_number = e.get()
#     e.delete(0,END)
#     e.insert(0,f_num + int(second_number))
#
# button1 = Button(root, text='1', padx=40, pady=20, command =lambda:button_click(1))
# button2 = Button(root, text='2', padx=40, pady=20, command = lambda:button_click(2))
# button3 = Button(root, text='3', padx=40, pady=20, command = lambda:button_click(3))
# button4 = Button(root, text='4', padx=40, pady=20, command = lambda:button_click(4))
# button5 = Button(root, text='5', padx=40, pady=20, command =lambda: button_click(5))
# button6 = Button(root, text='6', padx=40, pady=20, command = lambda:button_click(6))
# button7 = Button(root, text='7', padx=40, pady=20, command = lambda:button_click(7))
# button8 = Button(root, text='8', padx=40, pady=20, command = lambda:button_click(8))
# button9 = Button(root, text='9', padx=40, pady=20, command = lambda:button_click(9))
# button0 = Button(root, text='0', padx=40, pady=20, command = lambda:button_click(0))
# button_add = Button(root, text='+', padx=39, pady=20, command= button_add)
# button_equals = Button(root, text='=', padx=91, pady=20, command = button_equal)
# button_clear = Button(root, text='clear', padx=79, pady=20, command = button_clear)
#
# button1.grid(row=3,column=0)
# button2.grid(row=3,column=1)
# button3.grid(row=3,column=2)
#
# button4.grid(row=2,column=0)
# button5.grid(row=2,column=1)
# button6.grid(row=2,column=2)
#
# button7.grid(row=1,column=0)
# button8.grid(row=1,column=1)
# button9.grid(row=1,column=2)
#
# button0.grid(row=4,column=0)
# button_add.grid(row=5,column=0)
# button_equals.grid(row=5,column=1,columnspan=2)
# button_clear.grid(row=4,column=1,columnspan=2)
#

# root.mainloop()

