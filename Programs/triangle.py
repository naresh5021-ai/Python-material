
#a,b,c=input("Enter a three value: ").split()
#a,b,c=4,3,5
a,b,c = [int(x) for x in input("Enter three value: ").split()] 
if a==b==c:
    print("Equilateral Triangle")
elif a*a==(b*b+c*c) or b*b==(a*a+c*c) or c*c==(a*a+b*b):
      print('Right Angled Triangle')
else:
    print('scalane trianqle')
      

