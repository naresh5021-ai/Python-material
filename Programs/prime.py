
m=int(input('Enter a number'))
i=1
count=0 
while(i<=m):
    if(m%i==0):
        count=count+1
    i=i+1
if(count==2):
    print('The Number {0} is Prime Number'.format(m))
else:
    print('The Number {0} is Not Prime Number'.format(m))
    
    