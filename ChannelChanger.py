#print wit
from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
import os
#===============screenshots creation===================
 
#im1 = Image.open("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/Reklama-template.jpg")
#im2 = Image.open("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/Reklama2.jpg")
#diff = ImageChops.difference(im2, im1)
#diff.save("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/reklamaporownianie.jpg")
#statinfo = os.stat("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/reklamaporownianie.jpg")
#print(statinfo.st_size)
#if statinfo.st_size < 10000:
#      print('pliki nie pasuja')
#else:
 #     print('pliki pasuje')
# ==================wczytywanie i porownywanie zapisanych plikow 

while 1:
      for i in range(1,20):
        img = ImageGrab.grab()
        img.save("C:/Users/marcin.idzik/Desktop/Potrzebne/Moja_tworczosc/nowy/screenImage1"+str(i)+".jpg")
        #im = Image.open("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/screenImage1"+str(i)+".jpg")
        #print (im.format, im.size, im.mode)
        #im1 = Image.open("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/Reklama-template.jpg")
        im1 = Image.open("C:/Users/marcin.idzik/Desktop/Potrzebne/Moja_tworczosc/nowy/screenImage1"+str(i)+".jpg")
        im2 = Image.open("C:/Users/marcin.idzik/Desktop/Potrzebne/Moja_tworczosc/nowy/screenImage1"+str(i)+".jpg")
        diff = ImageChops.difference(im2, im1)
        diff.save("C:/Users/marcin.idzik/Desktop/Potrzebne/Moja_tworczosc/nowy/porownianie"+str(i)+".jpg")
        statinfo = os.stat("C:/Users/marcin.idzik/Desktop/Potrzebne/Moja_tworczosc/nowy/porownianie"+str(i)+".jpg")
        print(statinfo.st_size)
        if statinfo.st_size > 100:
            print('pliki nie pasuja')
        else:
            print('pliki pasuje')
        #os.remove("C:/Users/ff/Desktop/Potrzebne/Moja_tworczosc/nowy/porownianie"+str(i)+".jpg")
 
#==========================================================
