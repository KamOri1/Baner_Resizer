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

        elif e.upper()  in d:
           if (((e.upper() == "FR" and e.upper() in d and (d[(d.find("FR") - 2):2] == "CH")))):
            continue

           else:
            print('jest ' + e + ' w ' + d)
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e.upper()}.{format}")




    print(f'***** Paczka banerów nr {b_number} została przygotowana *****')


    APS_API.psBannerResizer(catDir, baner_check, b_number)



