import os
import shutil
f = open("practices.text",'w+')
f.write("First line")


print(os.getcwd()) #works like pwd
print(os.listdir()) #ls
print(os.listdir("C:\Personal\\"))
#shutil.move("practice.text","C:\Personal\\") #mv
#os.unlink(path)#deletes file
#os.rmdir(path)#delete directory
#shutil.rmtree(path)#deletes all the internal ones difficult to recover carefull!!!!!!!!
#shutil.move("C:\Personal\practice.text",os.getcwd())
for folder, sub_folder,files in os.walk("C:\Personal\linux\python scriting"):
    print(f"currently looking ar {folder}")
    print('Subfolders are:')
    for sub_fold in sub_folder:
        print(sub_fold)
    for f in files:
        print(f"file: {f}")
