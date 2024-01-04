import cv2
import os
import jpgFiltrChecker as jpgFiltr
import core
# kraje = ['chde','at', 'de', 'fr', 'uk', 'pl', 'nl', 'es', 'it', 'pt', 'fi', 'hu', 'dk', 'cz', 'no', 'sk', 'se','chfr']
# catDir = 'C:\\Users\\User\\Desktop\\PyWyP\\Testowe pliki\\mp4Test'
# baner1_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 1\\Org"))
# baner2_check =  list(os.listdir(f"{catDir}\\Banery\\Baner 2\\Org"))
#sprawdzenie  czy baner jest w rozszerzeniu mp4, jesli tak to zmienia nazwe na kraj i konwertuje do jpg


def mp4Conwerter(kraje, catDir, baner_check, b_number,data):

  
  
 if baner_check[0].endswith(".mp4") or baner_check[1].endswith(".mp4"):
  for e in kraje:
    for d in baner_check:
      if e  in d:
        print('jest ' + e + ' w ' + d)
        os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.mp4")
        cam = cv2.VideoCapture(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.mp4")
            
        ret,frame = cam.read()
        if ret:

          name = f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e.upper()}.jpg"
          print ('Creating...' + name)

        cv2.imwrite(name, frame)
      elif e.upper()  in d:
        print('jest ' + e)
        os.rename(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{d}", f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.mp4")
        cam = cv2.VideoCapture(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e}.mp4")
            
        ret,frame = cam.read()
        if ret:

          name = f"{catDir}\\Banery\\Baner {b_number}\\Org\\{e.upper()}.jpg"
          print ('Creating...' + name)

        cv2.imwrite(name, frame)
      
  cv2.destroyAllWindows()
  print("mp4 sie wykonał teraz konwert na jpg")
 jpgFiltr.jpgResizer(kraje, catDir, core.banerList(b_number, catDir),b_number, data)




#mp4Conwerter(kraje, catDir, baner2_check, 2)

