import os
if(os.path.exists("file2.txt")):
    os.remove("file2.txt")
    print("The file removed successfuy")
else:
    print("The file does not exist")
    