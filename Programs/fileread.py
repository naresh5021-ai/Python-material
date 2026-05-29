
try:
    f=open("file1.txt",'r')
    #print(f.read()) ---->read whole file
    for x in f:
        print(x)
    #print(f.readline()) ---->read single line
except:
    print("Something went wrong when writing to the file")
finally: 
    f.close()
