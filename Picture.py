#pip install pillow
from PIL import Image
im = Image.open('Ayesha.JPG')
print(type(im))
#print(im.show())
print(im.size)
print(im.crop((0,0,100,100)))#(x,y,w,h) x,y are referred as origin w is x axis h is y axis
#we can paste a croped image to a particular cordinates using
im.paste(im=srcimage,box=(coordinates)) #mask option is used to overlap the two images mask comes above.
im.putalpha()# transperacy
im.save("path")