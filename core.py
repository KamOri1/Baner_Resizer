import os
import cv2
from PIL import Image
#import serverConnection
import mp4FileChecker as mp4Filtr
#import jpgFiltrChecker as jpgFiltr
import pngFiltrChecker as pngFiltr
import bannerFileChecker as banFiltr
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

        if baner_check[0].endswith(".mp4") or baner_check[1].endswith(".mp4"):
            cNC.dach_checker(catDir, b_number, ".mp4")
            cNC.chfr_checker(catDir, b_number, ".mp4")
            # Pobranie zaktualizowanej zawartości folderów aby filtr mógł je wszystkie przeskalować "baner_check"
            baner_check = list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
            mp4Filtr.mp4Conwerter(kraje, catDir, baner_check, b_number, data)


        elif baner_check[0].endswith(".jpg") or baner_check[1].endswith(".jpg"): 
            cNC.dach_checker(catDir, b_number, "jpg")
            cNC.chfr_checker(catDir, b_number, "jpg")
            # Pobranie zaktualizowanej zawartości folderów aby filtr mógł je wszystkie przeskalować "baner_check"
            baner_check = list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
            banFiltr.bannerFileResizer(kraje, catDir, baner_check,b_number,data, "jpg")

        elif baner_check[0].endswith(".png") or baner_check[1].endswith(".png"): 
            cNC.dach_checker(catDir, b_number, "png")
            cNC.chfr_checker(catDir, b_number, "png")
            # Pobranie zaktualizowanej zawartości folderów aby filtr mógł je wszystkie przeskalować "baner_check"
            baner_check = list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
            banFiltr.bannerFileResizer(kraje, catDir, baner_check, b_number, data, "png")


