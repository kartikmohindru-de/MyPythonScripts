'''
#!/usr/bin/python3
default one
''''
#!bin/python3
#if we are running the code from virtual environment path refer linux for this
import shutil
import psutil
du=shutil.disk_usage("/")
used=(du.used/du.total)*100
print("Used Disk :{:.2f} %".format(used))
print("Available Disk :{:.2f} %".format(100-used))

