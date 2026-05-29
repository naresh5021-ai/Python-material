

def fact(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print('Factorial of {0} is {1}'.format(n,s))

n=int(input('Enter your Number'))
fact(n)