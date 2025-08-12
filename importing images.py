
import xlsxwriter
import os
from PIL import Image
import re
workbook = xlsxwriter.Workbook('test.xlsx')

worksheet = workbook.add_worksheet()
worksheet.set_column("A1:D1",50)
worksheet.set_default_row(200)
images = ["C:\Personal\linux\python scriting\Ayesha.JPG","C:\Personal\\722-7227134_tress-lounge-png-download-tress-lounge-logo-png.png"]
image_row=1
image_col=0
fn_col=3
pat=re.compile(".*.png$")
for (rootss,dirss,files) in os.walk("C:\Personal\linux\python scriting\Sprites\\"):
    for dirs in dirss:
        for(roots,dirs,files)in os.walk(rootss+dirs):
            for image in files:
                if(pat.search(image)!=None):
                    print(image_row)
                    print(roots)
                    print(image)
                    im = Image.open(roots+"\\"+image)
                    resized_im = im.resize((185, 209))
                    resized_im.save(roots+"\\"+image)
                    worksheet.insert_image(image_row,image_col,roots+"\\"+image,{'x_scale':0.3,'y_scale':0.3,'x_offset':5,'y_offset':5,'positioning':1})
                    worksheet.write(image_row, fn_col, roots+"\\"+image)
                    image_row=image_row+1
header=['Image','FeedBack','ReferenceImage','FilePath']
image_row=0
image_col=0
for head in header:
    worksheet.write(image_row,image_col,head)
    image_col = image_col+1
workbook.close()

