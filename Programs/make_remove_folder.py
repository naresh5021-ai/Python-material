import os
if(os.path.exists("myfolder")):
    os.rmdir("myfolder")
    print("The folder removed successfuy")
else:
   os.mkdir('myfolder')
   print("The folder does not exist so it is created now")


