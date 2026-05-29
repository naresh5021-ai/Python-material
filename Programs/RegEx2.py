import re
  
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt="The rain in Spain"
x=re.search("^The.*Spain$", txt)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt="The rain in Spain"
x=re.split("\s",txt)
print(x)

txt="The rain in Spain"
x=re.split("r",txt)
print(x)

txt="The rain in Spain"
x=re.sub("\s","-",txt)
print(x)