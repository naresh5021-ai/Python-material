
try:
    f=open("file.txt",'a')
    f.write("\nhello Python Program")
except:
    print("Something went wrong when writing to the file")
finally:
    print("File written successfully")  
    f.close()
