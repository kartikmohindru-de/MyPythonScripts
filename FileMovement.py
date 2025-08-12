import os

from zipfile import ZipFile
def fileExtract(src):
    with ZipFile(src, 'r') as zip:
        print("Unziping All Files")

        try:
            zip.extractall("C:\Personal\Task\work")
        except:  # except Type Error you can always put a built in error type
            print("File unzipping Failed")
            return 1
        else :
            print("Success")

            return 0

def fileMove(src,des):
    try:
        print(src)
        print(des)
        os.rename(src,des)
    except:
        print("File Move failed")
        return 1
    else:
        print("File moved successfully")
        return 0
def createDir(srcs):
    try:
        os.mkdir(srcs)
    except FileExistsError:
        print("Directory ", srcs, " This Directory already exists")
        print("\n")



otpt=fileExtract("C:\Personal\Task\work\\text files for project -do not alter.zip")
if(otpt==0):
    otpt1=fileMove("C:\Personal\Task\work\\text files for project -do not alter.zip", os.path.dirname(os.path.split("C:\Personal\Task\work\\text files for project -do not alter.zip")[0]) + "\incoming\\" + os.path.split("C:\Personal\Task\work\\text files for project -do not alter.zip")[1])
if(otpt1==0):
    print("Next Processing begins")
    for dir,pt,files in os.walk("C:\Personal\Task\work\\"):
        print(files[0])
        for file in files:

            fn = "C:\Personal\Task\work\\"+file
            with open(fn, "r") as src:
                fl = src.readline().rstrip()
                print(fl)
                if (len(fl) != 0):
                    dc = fl.split("-")
                    print(dc)
                    np = os.path.join("C:\Personal\Task\\",dc[0])
                    np1 = os.path.join("C:\Personal\Task\\",dc[0],dc[1])
                    np2 = os.path.join("C:\Personal\Task\\", dc[0], dc[1], dc[2])
                    #os.makedirs()#for multi level directory creation at once
                    createDir(np)
                    createDir(np1)
                    createDir(np2)
                    os.system('copy "C:\Personal\Task\work\\"+file,np2')
                    src.close()
                    fileMove("C:\Personal\Task\work\\"+file,os.path.dirname("C:\Personal\Task\work") + "\incoming\\" + file)
                    pass



