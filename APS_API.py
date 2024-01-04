import photoshop.api as ps

app = ps.Application()

# Load the image file into Photoshop and assign it to the 'a' variable
a = app.load("C:\\Users\\User\Desktop\\Baner_Resizer\\Baner_Code\\Baner_resizer_version\\10_new_function\\PS_Project\\NO.jpg")

# Resize and save the image
a.resizeImage(width=610, height=242, resolution=72, automatic=8)
jpg = 'C:\\Users\\User\Desktop\\Baner_Resizer\\Baner_Code\\Baner_resizer_version\\10_new_function\\PS_Project\\no05012334sss.jpg'
options = ps.JPEGSaveOptions(quality=5)
a.saveAs(jpg, options, asCopy=True)
a.close()

# zamyka program photoshop
ps.Application().quit()
print('zakończono')