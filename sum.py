#calculate the value of 1+2+...+100

def sum(n):
    result = 0
    while n > 0:
       result = result + n
       n -= 1
    return result    

print(sum(100))
print(sum(99999))
