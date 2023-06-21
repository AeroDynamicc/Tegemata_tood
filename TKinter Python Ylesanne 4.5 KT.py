from tkinter import *
# Daniil Meijel
# 21.06
aken = Tk()
aken.title('Ulesanne 4.5 KT')
aken.geometry('128x125')
aken.maxsize(width=200, height=200)

#textbox
laabel = Label(aken,text='mis on faili nimi (.txt)')
laabel.grid(row=0,column=1, padx=2)

# 'Entry' moodul on siis selleks, et kasutaja kirjutaks faili sinna kirjakasti.
entri = Entry(aken)
entri.grid(row=1,column=1,columnspan=2,padx=1,pady=2)

# 'Laabel2' on tekstikast, et saaks 'git' funktsioonis muuta str vaartust.
laabel2 = Label(aken,text='koik myndid:')
laabel2.grid(row=3,column=1)

# 'Laabel3' juures on sama asi.
laabel3 = Label(aken,text='myndivaartus:')
laabel3.grid(row=4,column=1)


# Tahtsaim funktsioon
def git():
    # teeb 'summa' muutuja funktsioonile ligipaasetavaks. Teeb muutujat 'summa' ligipaasetavaks funktsioonile.        
    summa = 0
    kogusumma = 0
    intlist = []
    # Votab kirjakastist failinime
    gitentri = entri.get()
    # Paneb kirja 'gitentr'-ist saadud failinimega faili
    with open (gitentri) as offen:
        muna = [i for i in offen.read().split('\n')]
    # loop
    for i in muna: 
        inttra = int(i)
        intlist.append(inttra)
    # loop'i algus
    for i in intlist:
        kogusumma += i  
        laabel2.config(text=f'koik myndid:{kogusumma}')
        if i <= 5:
            summa += i
        laabel3.config(text=f'Myndivaartus porsas:{summa}')

# See funktsioon paneb 'git' nupu toole.
buton = Button(aken, text='tee see arvutus', command=git)
buton.grid(row=2,column=1)

aken.mainloop()
