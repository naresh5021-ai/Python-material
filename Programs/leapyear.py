n=int(input('enter a year'))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print('Year {0} is a leap year'.format(n))
        else:
            print('Year {0}is not leap year'.format(n))
    else:
        print('Year {0} is a leap year'.format(n))
else:
    print('Year {0}is not leap year'.format(n))
    
