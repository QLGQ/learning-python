#Implementation of basic operations
# -*- coding: UTF-8 -*- 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x,n):
   # s = 1
   # while n > 0:
   #   n -= 1
   #   s = s*x
   # return s
    return x ** n

def factorial(n):
    if n == 1:
       return 1
    return n * factorial(n-1)
    #TODO Replace with generator

def extract(x,n):
    s = 1
    n = 1/n
    while n > 0:
      n -= 1
      s = s*ox
    return s
    #TODO 

def my_abs(x):
    if not isinstance(x,(int,float)):
       raise TypeError('bad operand type')
    if x >= 0:
       return x
    else:
       return -x

print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
print("5、乘方")
print("6、阶乘")
print("7、开方")
print("8、绝对值")
choice = input("输入你的选择(1/2/3/4/5/6/7/8):")
print("如果为一元运算只需输入第一个数字，如果为二元运算则需输入两个数字！")
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
input_string = "choice:%d, num1:%d, num2:%d" % (choice, num1, num2)
print(input_string)

if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 4:
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == 5:
   print(num1,"^",num2,"=", power(num1,num2))

elif choice == 6:
   print(num1,"!","=", factorial(num1))

elif choice == 7:
   print(num1,"√","=", extract(num1,num2))

elif choice == 8:
   print("|",num1,"|","=", my_abs(num1))

else:
   print("错误输入！")
