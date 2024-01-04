import os
import cv2
from PIL import Image
#import serverConnection
import mp4FileChecker as mp4Filtr
import jpgFiltrChecker as jpgFiltr
import pngFiltrChecker as pngFiltr
import countryNameCorrection as cNC
#cataDir = 'C:\\Users\\Kaspi\\Desktop\\Nowy folder'
# kraje = ['chde','at', 'de', 'fr', 'uk', 'pl', 'nl', 'es', 'it', 'pt', 'fi', 'hu', 'dk', 'cz', 'no', 'sk', 'se','chfr']
# catDir = 'C:\\Users\\User\\Desktop\\PyWyP\\Testowe pliki\\mp4Test'
def banerList(baner_check, catDir):
    if baner_check == 1:
        baner_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 1\\Org"))
        return baner_check
    elif baner_check == 2:
        baner_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 2\\Org"))
        return baner_check
def makeStructure(linkForCatalog):
    
    catDir = linkForCatalog
    
    if os.path.exists(f"{catDir}\\Banery") == False:
        os.makedirs(f"{catDir}\\Banery")
        os.makedirs(f"{catDir}\\Banery\\Baner 1")
        os.makedirs(f"{catDir}\\Banery\\Baner 1\\Org")
        os.makedirs(f"{catDir}\\Banery\\Baner 1\\New")
        os.makedirs(f"{catDir}\\Banery\\Baner 2")
        os.makedirs(f"{catDir}\\Banery\\Baner 2\\Org")
        os.makedirs(f"{catDir}\\Banery\\Baner 2\\New")
        os.startfile(f"{catDir}\\Banery\\Baner 1\\Org")
        os.startfile(f"{catDir}\\Banery\\Baner 2\\Org")
    else: 
        os.startfile(f"{catDir}\\Banery\\Baner 1\\Org")
        os.startfile(f"{catDir}\\Banery\\Baner 2\\Org")

def chooseRightFormat(kraje, catDir, baner_check, b_number, data):
    
    
        #cNC.nameCorrection(catDir,baner_check, b_number)
        #cNC.dach_chfr_checker_jpg(catDir,baner_check, b_number, "jpg")
       
        
        if baner_check[0].endswith(".mp4") or baner_check[1].endswith(".mp4"):
            cNC.dach_checker(catDir, b_number, ".mp4")
            cNC.chfr_checker(catDir, b_number, ".mp4")
            # Pobranie zaktualizowanej zawartości folderów aby filtr mógł je wszystkie przeskalować "baner_check"
            baner_check = baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
            mp4Filtr.mp4Conwerter(kraje, catDir, baner_check, b_number, data)

        elif baner_check[0].endswith(".jpg") or baner_check[1].endswith(".jpg"): 
            cNC.dach_checker(catDir, b_number, "jpg")
            cNC.chfr_checker(catDir, b_number, "jpg")
            # Pobranie zaktualizowanej zawartości folderów aby filtr mógł je wszystkie przeskalować "baner_check"
            baner_check = baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
            jpgFiltr.jpgResizer(kraje, catDir, baner_check,b_number,data)

        elif baner_check[0].endswith(".png") or baner_check[1].endswith(".png"): 
            cNC.dach_checker(catDir, b_number, "png")
            cNC.chfr_checker(catDir, b_number, "png")
            # Pobranie zaktualizowanej zawartości folderów aby filtr mógł je wszystkie przeskalować "baner_check"
            baner_check = baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
            pngFiltr.pngResizerq(kraje, catDir, baner_check, b_number)
   # else: print("uzupełnij foldery banerów")   
    



#chooseRightFormat(kraje, catDir, baner2_check, 2)






















 
# def weryfikacja(linkForCatalog, kraje): 
     
#      catDir = linkForCatalog
#      weryfikacjaBaneru  = input("Czy banery zostały dodane we właściwych folderach? Y/N ")
#      while weryfikacjaBaneru:
#         wweryfikacja = weryfikacjaBaneru.upper()
#         if wweryfikacja == 'Y':
#           baner1_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 1\\Org"))
#           baner2_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 2\\Org"))
#           if baner1_check[0].find('.mp4'):
#               mp4FileChecker.mp4Conwerter(kraje, catDir, 1, baner1_check)
#           break
            
#         else: 
#             print('Dodaj pliki banerów do właściwych folderów')
#             weryfikacja(catDir)
         



















    

