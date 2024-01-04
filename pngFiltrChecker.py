import os
import cv2
from PIL import Image
#import serverConnection
#cataDir = 'C:\\Users\\Kaspi\\Desktop\\Nowy folder'               
kraje = ['chde','at', 'de', 'fr', 'uk', 'pl', 'nl', 'es', 'it', 'pt', 'fi', 'hu', 'dk', 'cz', 'no', 'sk', 'se','chfr']
#weryfikacja  = input("Czy banery zostały dodane we właściwych folderach? ")
catDir = 'C:\\Users\\User\\Desktop\\PyWyP\\Testowe pliki\\mp4Test'
# baner1_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 1\\Org"))
# baner2_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 2\\Org"))
    

     
#     # skalowanie i zmiana nazwy baneru nr 1
# def jpgResizer(kraje, catDir, baner_check, b_number, data):
#   if baner_check[0].endswith(".jpg") or baner_check[1].endswith("jpg"):    
#     for v in baner_check:
#             im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{v}")
#             out1 = im1.resize((610, 242))
#             out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{v}")
#             print(f' plik o nazwie {v} został przeskalowany')
#     print(f' Paczka banerów nr {b_number} została przygotowana ########################################################################################')
#     baner1a_check =  list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\New"))
      
#     for va in baner1a_check:
#            for ww in kraje:
#              if va.find(ww) or va.find(ww.upper()):
#                continue 
#              else: 
#                os.rename(f"{catDir}\\Banery\\Baner {b_number}\\New\\{va}", f"{catDir}\\Banery\\Baner {b_number}\\New\\{ww}_{data}_b{b_number}.png")    

    
# #jpgResizer(kraje, catDir, baner2_check, 2, '25-08-2023')




        
def pngResizerq(kraje, catDir, baner_check, b_number): 
   if baner_check == 'baner1_check':
      baner_check = list(os.listdir(f"{catDir}\\Banery\\Baner 1\\Org")) 
   elif baner_check == 'baner2_check':
       baner_check = list(os.listdir(f"{catDir}\\Banery\\Baner 2\\Org"))
   
   if baner_check[0].endswith(".png") or baner_check[1].endswith("png"):  

    for e in kraje:
      for d in baner_check:
        if e.lower()  in d:
          print('jest ' + e + ' w ' + d)
          if d == (e + ".png"):
             continue
          else:
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.png")
         
            im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.png")
            out1 = im1.resize((610, 242))
            out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}.png")
            print(f' plik o nazwie {e} został przeskalowany')
          
        elif e.upper()  in d:
            print('jest ' + e + ' w ' + d)
        
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e.upper()}.png")
            im1 = Image.open(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.png")
            out1 = im1.resize((610, 242))
            out1.save(f"{catDir}\\Banery\\Baner {b_number}\\New\\{e.upper()}.png")
            print(f' plik o nazwie {e} został przeskalowany')




    print(f' Paczka banerów nr {b_number} została przygotowana ########################################################################################')


#pngResizerq(kraje, catDir, 'baner2_check', 2, 2)