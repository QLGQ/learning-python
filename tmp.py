
def gen(param='spam'):
    yield param
    while True:
        param = yield param

g = gen()
next(g)
print(g.send("x"))

def move(a, b, c):
    print(a, b, c)

def move2(*args):
    print(len(args))
    print(args[0], args[1], args[2])

move('a', 'b', 'c')
move2('a', 'b', 'c')

import traceback

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact(900)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(1000))


class Application:
    def open_item(self,path):

    def init(self):
        open_func = functoools.partial(self.open_item,item_path)
        popup_menu.apppend(("Open",open_func,1))


def my_decrator(f):
    def wrapper(*args,**kwds):
    	print 'Calling decorated function'
        return f(*args,**kwds)
    functools.update_wrapper(wrapper,f)
    return wrapper

def my_decrator(f):
    @functools.wraps(f):
    def wrapper(*args,**kwds):
        print 'Calling decorated function'
        return f(*args,**kwds)
    return wrapper

if condition:
    x = true_value
else:
    x = false_value

x = true_value if condition else false_value

class TestDict(unittest.TestCase):

    def setUp(self):
    	print('setUp...')
 
    def tearDown(self):
     	print('tearDown...')

def __init__(self,**kw):
    super(Dict,self).__init__(**kw)

def __getattr__(self,key):
    try:
        return self[key]
    except KeyError:
        raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

def __setattr__(self,key,value):
    self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()

with self.assertRaise(KeyError):
    value = d['empty']

with self.assertRaise(AttributeError):
    value = d.empty

if __name__ == '__main__':
    unittest.main()

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
	    print('%s %s():'%(text,func._name_))
  	    return func(*args,**kw)
        return wrapper
    return decorator


import pickle
d = dict(name='Bob',age=20,score=88)
pickle.dumps(d)
 


