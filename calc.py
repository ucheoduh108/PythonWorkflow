

#def add(a,b):
#    return a + b


#def sub(a,b):
#    return a - b

#def multi(a,b):
#    return a * b

#def div(a,b):
#    return a / b

#WHILE LOOP

#n = 1
#while n <= 5:
#    v = n * n
#    print(v)
#    n += 1

#EXCEPTION HANDLING
#1

#try:
#    value = eval(input('Enter a number: '))

#except  Exception as e:
#    print('invalid value,', e)

#print('Bye' )

#2

#a = 6
#b = 9

#try:
#    print('Resource Open' )

#    print(a/b)
#    eval(input('Enter a value: '))

#except ZeroDivisionError as e:
#    print('Sorry you cannot divide by zero,', e)

#except ValueError as e:
#    print('Invalid value,', e)

#except Exception as e:
#    print("OOP! Something went wrong,", e)

#finally:
#    print('Resource Close')

#print('Bye')

#MultiThreading

#from time import sleep
#from threading import *

#class Greet(Thread):  # thread should be added as a parameter to the class
#    def run(self):  #there must be run method in multithreading
#        for i in range(5):
#            print('Hello')
#            sleep(1)

#class Name(Thread):
#    def run(self):
#        for i in range(5):
#            print('Uche')
#            sleep(1)

#t1 = Greet()
#t2 = Name()

#t1.start()  #you must also call the object with a start()
#sleep(0.2)
#t2.start()

#t1.join() #to join the main thread with the other threads (t1 & t2)
#t2.join()

#print('Bye')

#FILE HANDLING
#f = open('mydata.py')
#print(f.read())


#print(f.readline())
#print(f.readline())

#f = open('abc','w')
#f.write('Laptop: ')

#f = open('abc','a')
#f.write('Corei5')

#f1 = open("mydata.py",'r')
#f2 = open("abc",'w')

#for data in f1:
#    f2.write(data)


#p = open("C:/Users/user/Desktop/wedding photo/uchepix_wedding.jpg",'rb') # add 'b' to the mode for binary character

#p1 = open("Mypicx .jpg","wb")

#for picx in p:
#    p1.write(picx)

#LINEAR SEARCH USING PYTHON

#pos = - 1
#def search(value,n):

#    i = 0
#    while i < len(value):
#        if value[i] == n:
             #globals()['pos'] = 1
#            return True
#        i += 1

#    return False

#value = [3,4,5,6,7,8,9,33,45,12,60]
#n = 35

#if search(value, n):
#    print('Found',[pos]+1)

#else:
#    print('Not found')

#BINARY SEARCH USING PYTHON
#pos = -1

#def search(list,n):

#    l = 0
#    u = len(list) - 1

#    while l <= u:
#        mid = (l + u) // 2

#        if list[mid] == n:
#            globals()['pos'] = mid
#            return True

#        else:
#            if list[mid] < n:
#                l = mid + 1

 #           else:
 #               u = mid -1

 #   return False

#list = [34,25,65,88,66,90,109,23,125,167,189,199,173,388,467,823,276,456]
#n = 388

#if search(list,n):
#    print('Found',pos +1)

#else:
#    print('Not Found')

#SELECTION SORT USING PYTHON

#def sort(nums):
#    for i in range(5):
#        minpos = i
#        for j in range(i,6):
#            if nums[j] < nums[minpos]:
#                minpos = j

#        temp = nums[i]
#        nums[i] = nums[minpos]
#        nums[minpos] = temp

#        print(nums)


#nums = [5,3,9,2,8,1,10]
#sort(nums)
#print(nums)


#i = 0
#file = open("C:/Users/user/Desktop/MINUTES OF UMUDURUAJOMAI LAGOS txt.txt",'r')

#while  i <= 5:
#    print(file.readline())
#    i += 1

#OR

#for i in range(5):
#    while i == file:
#        i += 1

#    print(file.readline())








