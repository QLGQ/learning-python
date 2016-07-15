#output the square of 0,1,2,3...100 into a list
def square(n):
    return n*n
L1 = range(101)
L2 = list(map(square, L1))
print(L2)
