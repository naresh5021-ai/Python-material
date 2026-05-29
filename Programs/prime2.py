n=int(input('Enter a number'))
for i in range(2,n):
    if(n%i==0):
        print('The number {0} is not prime'.format(n))
        break
else:
    print('The number {0} is prime'.format(n))
    
    