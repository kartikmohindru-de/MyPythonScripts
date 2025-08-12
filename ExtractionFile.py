#!/usr/bin/python3

#import subprocess
import shutil, os
#from subprocess import check_output
import zipfile
#import shutil
from zipfile import ZipFile

def fileExtract(filenames):

    #with zipfile.ZipFile(filenames, 'r') as zo:
        #zo.extractall() #default where code is running
     #   zo.extractall('ExtractionTest')
        print(filenames)
        if(zipfile.is_zipfile(filenames)):
            fn = os.path.basename(filenames)
            shutil.move(filenames, 'TempExtracts')
            with zipfile.ZipFile('TempExtracts/'+fn, 'r') as zo:
                zo.extractall('ExtractionTest')
                shutil.copyfile('TempExtracts/' + fn, 'ExtractionTestMove/' + fn)
            for info in zo.infolist():
                print(info.filename)
                if (zipfile.is_zipfile('ExtractionTest/'+info.filename)):
                    fileExtract('ExtractionTest/'+info.filename)
            zo.close()
fileExtract('ExtractionTest/zippedZipped.zip')
#shutil.rmtree('TempExtracts' )shutil.rmtree('TempExtracts' )
#os.rmdir('TempExtracts')

try:
    shutil.rmtree('TempExtracts' )
except OSError as e:
    print("Error: %s : %s" % ('TempExtracts', e.strerror))
