def factorial(n):
'''
Function to calculate n!
Example:
>>>factorial(0)
Traceback(most recent call last):
...
ValueError
>>>factorial(2)
2
>>>factorial(3)
6
>>>factorial(10)
3628800
'''
if n < 1:
   raise ValueError()
if n == 1:
   return 1
return n * factorial(n-1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
