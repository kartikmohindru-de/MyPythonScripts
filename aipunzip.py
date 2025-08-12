import zipfile
import shutil
f = open("practices.text",'w+')
f.write("First line")
f.close()
f = zipfile.ZipFile('zipped.zip','w')
f.write('practices.text',compress_type=zipfile.ZIP_DEFLATED)
f.close()
zo = zipfile.ZipFile('zipped.zip','r')
zo.extractall('extarted') #path where extracted file needs to be kept
dtoz = 'C:\Personal\linux\python scriting\extarted'
opfile = 'Example'
shutil.make_archive(opfile,'zip',dtoz) #zips whole folder
shutil.unpack_archive('Example.zip','Unzip','zip') #filename,outpur foulder, format of file