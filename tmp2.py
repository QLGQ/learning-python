std = {'name':'Michael','score':98}
#std2 = {'name':'Bob','score':81}

def print_score(std):
    print('%s:%s' % (std['name'],std['score']))

print_score(std)


class Student(object):

    def _init_(self,name,score):
        self.name = name
        self.score = score
 
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')   

class Cat(Animal):
    pass

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run() 

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value  

s = Student()
s.set_score(60)
s.get_score()
'''
s1 = Student()
s1.set_score(999)
s.get_score()
'''

class Fib(object):
     def __init__(self):
         self.a, self.b = 0,1
     def __iter__(self):
         return self
     def __next__(self):
         self.a, self.b = self.b, self.a + self.b
         if self.a > 100000:
            raise StopIteration();
         return self.a

for n in Fib():
    print(n)

class Fib(object):
     def __getitem__(self,n):
         if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
               a,b = b,a+b
            return a
         if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
               start = 0
            a,b = 1,1    
            L = []
            for x in range(stop):
                if x >= start:
                   L.append(a)
                a, b = b, a+b
            return L


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self,attr):
        if attr == 'score':
           return 99

s = Student()
s.name
s.score


class Student(object):
 
    def __getattr__(self,attr):
        if attr == 'age':
           return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s.age()


class Student(object):
    def __init__(self,name):
	self.name = name

    def __call__(self):
        print('My name is %s.'% self.name)

s = Student('Michael')
s()


callable(Student())


def fn(self,name='world'):
    print('Hello,%s.'% name)

