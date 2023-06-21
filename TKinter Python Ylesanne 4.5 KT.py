from tkinter import *
# vaheta ened commentid ja selle koodi lugemine ara, muutujad peaksid OK olema
# akna algus, also ma kirjutasin siia sitaks
aken = Tk()
aken.title('ulesanne 4.5 kt')
aken.geometry('128x125')
aken.maxsize(width=200, height=200)

# textbox lol
laabel = Label(aken,text='mis on faili nimi (.txt)')
laabel.grid(row=0,column=1, padx=2)

# siin lisad 'entry' modulega kirjakasti, kuhu kasutaja kirjutab failinime
entri = Entry(aken)
entri.grid(row=1,column=1,columnspan=2,padx=1,pady=2)

# see on 'laabel2', tekstikast mille str vaartust me muudame 'git' funktsioonis
laabel2 = Label(aken,text='koik myndid:')
laabel2.grid(row=3,column=1)

# sama ka 'laabel3'-ga
laabel3 = Label(aken,text='myndivaartus porsas:')
laabel3.grid(row=4,column=1)


# pm main funktsioon mida kood kasutab
def git():
    # teeb 'summa' muutuja funktsioonile ligipaasetavaks        
    summa = 0
    kogusumma = 0
    intlist = []
    # 'gitentri' votab 'entri' aka kirjakastist failinime
    gitentri = entri.get()
    # with avab 'gitentri'st saadud failinimega filei, paneb listi ka
    with open (gitentri) as offen:
        muna = [i for i in offen.read().split('\n')]
    # loop et vahetada 'str' list 'int' listiks...muidu ei saa arvutada
    for i in muna: 
        inttra = int(i)
        intlist.append(inttra)
    # siin hakkab loop pihta mis kaib ridade labi intlistist
    for i in intlist:
        kogusumma += i  
        # vahetab 'laabel3' teksti '.config' moduleiga ara
        # naide: 'koik myndid:(siia tulevad koik myndid listina)'
        laabel2.config(text=f'koik myndid:{kogusumma}')
        if i <= 5:
            summa += i
        # naide: '25 myntivaartust on seal porsas'
        laabel3.config(text=f'myndivaartus porsas:{summa}')

# see nupp paneb 'git' functioni toole
buton = Button(aken, text='tee see arvutus', command=git)
buton.grid(row=2,column=1)

aken.mainloop()