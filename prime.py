#-*-coding:utf-8-*-
#Set a condition for exiting the loop
def main(maximum=1000):
    pr = primes(maximum)
    for n in pr:
        if n < maximum:
            print(n)
        else:
            break

#Construct a sequence of odd numbers starting from 3
def _odd_iter(maximum):
    n = 1
    while n < maximum:
        n = n + 2
        yield n
    
#Construct a filter function to filter the sequence of previous constructs
def _not_divisible(n):
    return lambda x: x % n > 0 
'''
lambda:Anonymous function and The return value is the result of the expression.
'''
#Define a generator, and continue to return to the next prime number
def primes(maximum):
    yield 2
    it = _odd_iter(maximum)
    n = next(it)
    yield n
    while True:
        try:
            it = filter(_not_divisible(n), it)
            n = it.pop(0)
            yield n
        except Exception: 
            break
'''
 Return those items of sequence for which function(item) is true.  If
    function is None, return the items that are true.  If sequence is a tuple
    or string, return the same type, else return a list.
'''
#invoke function
main(10000)
