

def rec_fact(n):
    if(n==1):
        return 1
    else:
        return n*rec_fact(n-1)
    
n=int(input('Enter your Number'))
f=rec_fact(n)
print('Factorial of {0} is {1}'.format(n,f))

