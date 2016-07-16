#calculate n power of x
def power(x,n):
  s = 1
  while n > 0:
    n -= 1
    s = s*x
  return s
