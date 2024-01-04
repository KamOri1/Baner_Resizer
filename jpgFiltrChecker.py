import os
import cv2
from PIL import Image
from PIL import ImageFilter
import serverConnection


def jpgResizer(kraje, catDir, baner_check, b_number, data):
   if baner_check[0].endswith(".jpg") or baner_check[1].endswith("jpg"):

    for e in kraje:

      for d in baner_check:
       if d.endswith(".jpg"):


        baner_check1 =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
        if e.lower()  in d:

         if((e.upper() == "DE" and e.upper() in d and (d[(d.find("DE") - 2):2] == "CH") or (e == "de" and e in d and (d[(d.find("de") - 2):2] == "ch")))):
           continue

         elif (((e == "fr" and e in d and (d[(d.find("fr") - 2):2] == "ch")))):
            continue

         else:
           print('jest ' + e + ' w ' + d)

           os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.jpg")

           im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.jpg")
           out1 = im1.resize((610, 242), resample=Image.LANCZOS)
           out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.jpg")
           print(f' plik o nazwie {e} został przeskalowany')
           im2 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.jpg")
           sharpened_image = im2.filter(ImageFilter.UnsharpMask(0, 0, 0))
           sharpened_image.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.jpg")
           print(f' plik {e} został wyostrzony')


        elif e.upper()  in d:
           if (((e.upper() == "FR" and e.upper() in d and (d[(d.find("FR") - 2):2] == "CH")))):
            continue

           else:
            print('jest ' + e + ' w ' + d)
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e.upper()}.jpg")
            im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.jpg")
            out1 = im1.resize((610, 242), resample=Image.LANCZOS)
            out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.jpg")
            print(f' plik o nazwie {e} został przeskalowany')
            im2 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.jpg")
            sharpened_image = im2.filter(ImageFilter.UnsharpMask(0, 0, 0))
            sharpened_image.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.jpg")
            print(f' plik {e} został wyostrzony')




    print(f'***** Paczka banerów nr {b_number} została przygotowana *****')






