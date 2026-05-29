d = lambda x:x*2 
print(d(5))

d = lambda x:x+10 
print(d(5))

d = lambda a,b:a+b 
print(d(5,6))

x = lambda a,b,c:a+b+c
print(x(5,6,7))


square=lambda x:x*x
result=square(5)
print(result)

def myfunc(n):
  return lambda a:a*n

m=myfunc(2)
print(m(11))
