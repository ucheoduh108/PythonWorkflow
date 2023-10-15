# INTRODUCTION TO POLYMORPHISM
#1.  DUCK TYPING
#class Pycharm:
#    def execute(self):
#        print('Compilling')
#        print('Running')

#class MyEditor:
#    def execute(self):
#        print('Spell check')
#        print('Convention check')
#        print('Compilling')
#        print('Running')

#class Laptop:
#    def code(self,ide):
#        ide.execute()

#ide = MyEditor()

#lap1 = Laptop()
#lap1.code(ide)



#2. OPERATOR OVERLOADING
#a = 3
#b = 4
#print(a *  b)
#print(int.__mul__(a,b))




#class Student:
#    def __init__(self,m1,m2):
#        self.m1 = m1
#        self.m2 = m2

#    def __add__(self, other):
#        m1 = self.m1 + other.m1
#        m2 = self.m2 + other.m2
#        s3 = m1 + m2
#        return s3

#    def __gt__(self, other):
#        s1 = self.m1 + other.m2
#        s2 = self.m1 + other.m2
#        return s1 > s2

#s1 = Student(56,78)
#s2 = Student(64,89)

#s3 = s1 + s2
#comp = s1 > s2

#print(s3)
#print(comp )




#class Book:
#    def __init__(self,price):
#        self.price = price

#    def __add__(self, other):
#        return self.price + other.price

#    def __lt__(self, other):
#        return self.price < other.price

#book1 = Book(30)
#book2 = Book(40)

#total_price = book1.price + book2.price
#print(total_price)

#OR

#total_price = book1 + book2
#comp = book1 < book2
#print(total_price)
#print(comp)



#ITERATORS
#1
#obj = ['Chima','Ikenna','Chikodi','Daniel','Nkeiru']
#obj_ite = iter(obj)

#print(next(obj_ite))
#print(next(obj_ite))
#print(next(obj_ite))
#print(obj_ite.__next__())



#2
#class TopTen:
#    def __init__(self):
#        self.num = 1

#    def __iter__(self):
#        return self

#    def __next__(self):

        #if self.num <=10:
 #           val = self.num
 #           self.num += 1
 #           return val

        #else:
         #   raise StopIteration

#values = TopTen()

#print(values.__next__())
#print(values.__next__())

#for i in values:
#    print(i)



#YIELD
#def topTen():
#    yield 1
#    yield 2
#    yield 3
#    yield 4


#value = topTen()
#print(value.__next__())
#print(value.__next__())

#def topTen():

#    n = 1
#    while n <= 10:
#        w = n * n
#        n += 1
#        yield w

#values = topTen()
#print(values.__next__())
#print(values.__next__())

#for i in values:
#    print(i)



#Zip function
#names = ("Ebuka","Emeka","Sammy")
#compy = ("Phamatex","Hovid","Nimeth")

#zipped = zip(names,compy) #you can use list,set,dict before the zip funx etc
#print(zipped)

#or

#for (a,b) in zipped:
#    print(a,b)







