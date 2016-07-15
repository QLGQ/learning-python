#classify which age groups the number  belongs to
def age(n):
    if n >= 6 and n < 18:
       return ('teenager')
    elif n >= 18:
       return ('adult')
    else:
       return ('kid')

print(age(23))
print(age(16))
