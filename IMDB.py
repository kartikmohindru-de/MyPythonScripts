#!/usr/bin/python3

#import subprocess
import shutil, os
#from subprocess import check_output
import zipfile
import shutil
import gzip
from zipfile import ZipFile

def fileExtract(filenames,ExtractsHere='ExtractionTestMove/'):
    #with zipfile.ZipFile(filenames, 'r') as zo:
        #zo.extractall() #default where code is running
     #   zo.extractall('ExtractionTest')
        print(zipfile.is_zipfile(filenames))
        fn = os.path.basename(filenames)
        if(zipfile.is_zipfile(filenames)):

            shutil.move(filenames, 'TempExtracts')
            with zipfile.ZipFile('TempExtracts/'+fn, 'r') as zo:
                zo.extractall('ExtractionTest')
                shutil.copyfile('TempExtracts/' + fn, ExtractsHere + fn)
            for info in zo.infolist():
                print(info.filename)
                if (zipfile.is_zipfile('ExtractionTest/'+info.filename)):
                    fileExtract('ExtractionTest/'+info.filename)
                zo.close()
        else :
            if(not os.path.isdir(ExtractsHere)):
                os.mkdir(ExtractsHere)
            with gzip.open(filenames,'rb') as gz,open(os.path.join(ExtractsHere,os.path.splitext(fn)[0]),'wb+') as op:
                shutil.copyfileobj(gz,op)

#fileExtract('ExtractionTest/zippedZipped.zip')
for root,dirs,files in os.walk('C:\Personal\IMDB'):
    for file in files:
        fileExtract(os.path.join(root,file),'C:\Personal\IMDB\Extracts')
shutil.rmtree('TempExtracts')