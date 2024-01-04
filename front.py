import tkinter as tk
import core
import mp4FileChecker

def bigWindow():
    window = tk.Tk()
    v = tk.IntVar()
    window.geometry("400x250")
    label1 = tk.Label(text='Podaj lokalizację docelową katalogu: ')
    llinkForCatalog_ = tk.Entry()
    label2 = tk.Label(text='Podaj date kampani DD/MM/YY: ')
    dateforCatalog_ = tk.Entry()
    

    def licz():
        kraje = ['chde','chfr','at', 'de', 'fr', 'uk', 'pl', 'nl', 'es', 'it', 'pt', 'fi', 'hu', 'dk', 'cz', 'no', 'sk', 'se']
        catalogLocalization_ = llinkForCatalog_.get()
        data_ = dateforCatalog_.get()
        
        core.makeStructure(catalogLocalization_)
        weryfikacja  = input("Czy banery zostały dodane we właściwych folderach? Y/N ")
        if weryfikacja.upper() == "Y":
            core.cNC.nameCorrection(catalogLocalization_,core.banerList(1, catalogLocalization_), 1)
            core.chooseRightFormat(kraje, catalogLocalization_, core.banerList(1, catalogLocalization_), 1, data_)
            # core.cNC.dach_checker_jpg(catalogLocalization_, 1, "jpg")
            # core.cNC.chfr_checker_jpg(catalogLocalization_, 1, "jpg")
           
            core.cNC.nameCorrection(catalogLocalization_,core.banerList(2, catalogLocalization_), 2)
            core.chooseRightFormat(kraje, catalogLocalization_, core.banerList(2, catalogLocalization_), 2, data_)

            # core.cNC.dach_checker_jpg(catalogLocalization_, 2, "jpg")
            # core.cNC.chfr_checker_jpg(catalogLocalization_, 2, "jpg")
            
            
            


    def close():
        window.destroy()


    

    button_1 = tk.Button(text = 'Make a Banner', 
                         width=20,
                        # height=2,
                        bg="green",
                        fg="yellow",
                        command = licz,)
    
    button_2 = tk.Button(window, text='Exit',
                        width=20,
                        bg="red",
                        fg="yellow", 
                        command= close)
    


    
    label1.grid(row=1, column=0)
    llinkForCatalog_.grid(row=1, column=1)
    label2.grid(row=3, column=0)
    dateforCatalog_.grid(row=3, column=1)
    
    button_2.grid(row=7, column=0)
    button_1.grid(row=7, column=1)



    window.mainloop()






























