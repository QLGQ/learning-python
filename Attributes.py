#-*-coding:utf-8-*-
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # has attribute 'x' or not ?

print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # has attribute 'y' or not ?

setattr(obj, 'y', 19) # set an attribute 'y'

print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # has attribute 'y' or not ?

print('getattr(obj, \'y\') =', getattr(obj, 'y')) # get attribute 'y'

print('obj.y =', obj.y) #get attribute 'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # get attribute 'z',if not exist,then return default value 404

f = getattr(obj, 'power') # get attribute 'power'

print(f)

print(f())
