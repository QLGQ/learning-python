#calculate n!
def func(n):
  if n==1:
    return 1
  return n*func(n-1);
n=100;
print(func(n))
