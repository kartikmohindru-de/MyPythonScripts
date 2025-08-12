#%%writefile myfie.txt
#followed by content
#it works only in jupyter

myfile = open('myfile.txt')
print(myfile.read()) #the coursor comes at the end after first read so the second read is empty
myfile.seek(0)#so we use takes back to zero
print(myfile.readlines())
myfile2 = open('location2\\myfile.txt')
print(myfile2.read())
myfile.close()
myfile2.close()

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)
    #till the time we are under this the file will remian open after that it will close
with open('myfile.txt', mode='r') as my_new_file:
    contents = my_new_file.read() #if mode w is choosen we cannot read the file handy to limit the permissions
    print(contents)
with open('myfile.txt', mode='a') as my_new_file:
    my_new_file.write("\nthird line")  # if mode w is choosen we cannot read the file handy to limit the permissions
with open('myfile.txt', mode='r') as my_new_file:
    contents = my_new_file.read() #if mode w is choosen we cannot read the file handy to limit the permissions
    print(contents)

#r reading
#w writing
#a append
#r+ read and write
#w+ write and read