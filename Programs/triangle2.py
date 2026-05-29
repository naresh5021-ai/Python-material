a,b,c = [int(x) for x in input("Enter three value: ").split()] 
i=[a,b,c]
i.sort()
if a**2+b**2==c**2:
    print('Right Angled Triangle')
else:
    print('Scalane Triangle')