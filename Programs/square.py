import numpy
s=0
i=1
n=int(input("Enter a Number"))
while(i<=n):
    s=(i*i)
    print('The square of {0} is {1}'.format(i,s) )
    i=i+1

print('Printing Sum of squares:')
i=1
s=0
while(i<=n):
    s=s+(i*i)
    i=i+1
print('The Sum of the squares upto {0} is {1}'.format(n,s))
    
s=0
i=1
while(i<=n):
    s=numpy.sqrt(i)
    print('The square root of {0} is {1}'.format(i,s) )
    i=i+1