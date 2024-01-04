import os
import shutil


# Sprawdza czy pliki nie mają w nazwie ciągu znaków "desktop" a jesli tak to je usówa aby pozbyć sie zbednego znaku "DE" w tym słowie
def nameCorrection(catDir,baner_check, b_number):
    for plik in baner_check:
        if "desktop" in plik:
            new = plik.replace("desktop", " ")
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{plik}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{new}")
        elif "Desktop" in plik:
            new = plik.replace("Desktop", " ")
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{plik}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{new}")
        elif "DESKTOP" in plik:
            new = plik.replace("DESKTOP", " ")
            os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{plik}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{new}")
    print(f"***** Sprawdzanie nazw banerów nr {b_number} zakończone *****")

# Sprawdza różne kombinacje  nazwy "DACH" a jeśli znajdzie to zmienia pierwszy plik na "CHDE" i robi z niego kopie dla "DE" oraz "AT"
def dach_checker(catDir, b_number, format):
    baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
    for plik in baner_check:
         baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
         if ("DACH" in plik ) or ("dach" in plik ) or (f"CH.{format}" in plik) or (f"ch.{format}" in plik) or (f"Ch.{format}" in plik):
             if plik.endswith(f".{format}"):
             
              os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{plik}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\chde.{format}")
              print(f'Utworzono plik chde.{format}')
              shutil.copy(f"{catDir}\\Banery\\Baner {b_number}\\Org\\chde.{format}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\de.{format}")
              print(f'Utworzono plik de.{format}')
              shutil.copy(f"{catDir}\\Banery\\Baner {b_number}\\Org\\chde.{format}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\at.{format}")
              print(f'Utworzono plik at.{format}')
    print(f"***** Sprawdzanie poprawności DACH'u banerów nr {b_number} zakończone *****")
            #  print(list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org")))
            #  print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
         
        
     

# Sprawdza czy w folderze znajduje sie "FR" i "CHFR" jeśli tak ustawia wartość "count = 2" na tej podstawie  funkcja "chfr_checker_jpg" decyduje czy szukać brakującego pliku i go stworzyć 
def checkFor_CH_FR(catDir, b_number):
     baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
     count = 0
     for plik in baner_check:
          if (("FR" in plik and (plik[(plik.find("FR") - 2):2] == "CH") or ("fr" in plik and (plik[(plik.find("fr") - 2):2] == "ch")))):
               count += 1
               #print(f"jest plik: {plik}")
          if (("FR" in plik and (plik[(plik.find("FR") - 2):2] != "CH") or ("fr" in plik and (plik[(plik.find("fr") - 2):2] != "ch")))): 
               count += 1
               #print(f"jest plik: {plik}")
     return count
     
        


# Jeśli "count != 2" to funkcja sprawdza którego pliku brakuje i tworzy go z kopii znalezionego pliku
def chfr_checker(catDir, b_number, format):
  if(checkFor_CH_FR(catDir, b_number) != 2):
    baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))
    for plik in baner_check:
        
        baner_check =list(os.listdir(f"{catDir}\\Banery\\Baner {b_number}\\Org"))     
        if( ("fr" in plik or "FR" in plik) and ("CHFR" not in plik) and ("chfr" not in plik) ):
                 if plik.endswith(f".{format}"):
                    os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{plik}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\fr.{format}")
                    shutil.copy(f"{catDir}\\Banery\\Baner {b_number}\\Org\\fr.{format}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\chfr.{format}")
                    print(f"Znaleziono plik  FR, utworzono plik chfr.{format}")
               
        if("CHFR" in plik or "chfr" in plik ):
             if (("FR" in plik and (plik[(plik.find("FR") - 2):2] == "CH") or ("fr" in plik and (plik[(plik.find("fr") - 2):2] == "ch")))):
                 if plik.endswith(f".{format}"):
                    os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{plik}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\chfr.{format}")
                    shutil.copy(f"{catDir}\\Banery\\Baner {b_number}\\Org\\chfr.{format}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\fr.{format}")
                    print(f"Znaleziono plik  CHFR, utworzono plik fr.{format}")
  print(f"***** Sprawdzanie poprawności banerów nr {b_number} CH/FR zakończone *****")
                 
             

         



# catDir = "C:\\Users\\User\\Desktop\\Python\\PyWyP\\Testowe pliki\\Banery"
# #baner1_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 1\\Org"))
# dach_checker_jpg(catDir, 1, "jpg")
# chfr_checker_jpg(catDir, 1, "jpg")
