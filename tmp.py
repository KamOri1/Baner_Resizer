import photoshop.api as ps
import os
def psBannerResizer(catDir, baner_check, b_number):
    app = ps.Application()

    for banner_name in baner_check:
            print(banner_name)

            #Load the image file into Photoshop and assign it to the 'a' variable
            banner_file = app.load(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{banner_name}")
            print('załadowano kraj')
            # Resize and save the image
            banner_file.resizeImage(width=610, height=242, resolution=72, automatic=8)
            jpg = f"{catDir}\\Banery\\Baner {b_number}\\New\\{banner_name}"
            options = ps.JPEGSaveOptions(quality=5)
            banner_file.saveAs(jpg, options, asCopy=True)
            banner_file.close()










kraje = ['chde','at', 'de', 'fr', 'uk', 'pl', 'nl', 'es', 'it', 'pt', 'fi', 'hu', 'dk', 'cz', 'no', 'sk', 'se','chfr']
catDir = 'C:\\Users\\User\\Desktop\\Praca\\2024'
baner_check = os.listdir("C:\\Users\\User\\Desktop\\Praca\\2024\\Banery\\Baner 1\\Org")
data = '12'
b_number = 1
psBannerResizer(catDir, baner_check, 1)

print(baner_check)
# for banner_name in baner_check:
#
#     print(banner_name)
#     app = ps.Application()
#     banner_file = app.load(f"{catDir}\\Banery\\Baner {b_number}\\Org\\{banner_name}")
