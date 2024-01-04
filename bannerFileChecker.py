import os
import cv2
from PIL import Image
from PIL import ImageFilter
#import serverConnection
import APS_API

def bannerFileResizer(kraje, catDir, baner_check, b_number, data, format):
   if baner_check[0].endswith(f".{format}") or baner_check[1].endswith(f".{format}"):

    for e in kraje:
      for d in baner_check:
       if d.endswith(f".{format}"):
        if e.lower() in d:
         if((e.upper() == "DE" and e.upper() in d and (d[(d.find("DE") - 2):2] == "CH") or (e == "de" and e in d and (d[(d.find("de") - 2):2] == "ch")))):
           continue

         elif (((e == "fr" and e in d and (d[(d.find("fr") - 2):2] == "ch")))):
            continue

         else:
           print('jest ' + e + ' w ' + d)

           os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.{format}")




        # Skalowanie Pliku baneru zastąpione przez funkcję APS_Api
           # im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.{format}")
           # out1 = im1.resize((610, 242), resample=Image.LANCZOS)
           # out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.{format}")
           #print(f' plik o nazwie {e} został przeskalowany')


        # Wyostrzenie  pliku akutalnie zastapione Photoshopem
           # im2 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.{format}")
           # sharpened_image = im2.filter(ImageFilter.UnsharpMask(0, 0, 0))
           # sharpened_image.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.{format}")
           # print(f' plik {e} został wyostrzony')


        elif e.upper()  in d:
           if (((e.upper() == "FR" and e.upper() in d and (d[(d.find("FR") - 2):2] == "CH")))):
            continue

           else:
            print('jest ' + e + ' w ' + d)
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e.upper()}.{format}")


        # Skalowanie Pliku baneru zastąpione przez funkcję APS_Api
            # im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.{format}")
            # out1 = im1.resize((610, 242), resample=Image.LANCZOS)
            # out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.{format}")
            #print(f' plik o nazwie {e} został przeskalowany')

        # Wyostrzenie  pliku akutalnie zastapione Photoshopem
        #     im2 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.{format}")
        #     sharpened_image = im2.filter(ImageFilter.UnsharpMask(0, 0, 0))
        #     sharpened_image.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}_b_{b_number}_{data}.{format}")
        #     print(f' plik {e} został wyostrzony')

    print(f'***** Paczka banerów nr {b_number} została przygotowana *****')


    APS_API.psBannerResizer(catDir, baner_check, b_number)



