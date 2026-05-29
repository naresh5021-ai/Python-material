
#a=input("Enter any string:") 
a='Naresh'
print("Center alignment:", a.center(15,'*'))  
print("Left   alignment:", a.ljust(15,'*'))  
print("Right  alignment:", a.rjust(15,'*'))

print('\n')
#a=input("Enter any string:")  
a='****Naresh****'
print("Left  space trim:",a.lstrip('*'))  
print("Right space trim:",a.rstrip('*'))  
print("Left and right trim:",a.strip('*'))

print('\n')
#a=input("Enter any string:")  
a='Naresh1234'
print("Alphanumeric:",a.isalnum())  
print("Alphabetic  :",a.isalpha())  
print("Digits      :",a.isdigit())  
print("Lowecase    :",a.islower())  
print("Upper       :",a.isupper())

