#!/usr/bin/python3


import subprocess
import shutil, os
from subprocess import check_output
from zipfile import ZipFile
print(os.getcwd());
#c=subprocess.Popen(["ls"], stdout=subprocess.PIPE, shell=True).communicate()[0]
c= check_output(["ls"],encoding="utf-8")
print(c)
a=[]
#a=c.split("\n")
a=c.splitlines() #split wheree newlines is a delimeter
print(a)

def fileExtract():
    with zipfile.ZipFile('zipped.zip', 'r') as zo:
        for info in zo.infolist():
            print(info.filename)


for i in a:
    print(i)
    if(i=="test1.csv"):
        print("inside ", i )
        command = "cat "+i;
        #os.system('command')
        #subprocess.run(["cat", i])
        shutil.move(f, 'csvlocation')


