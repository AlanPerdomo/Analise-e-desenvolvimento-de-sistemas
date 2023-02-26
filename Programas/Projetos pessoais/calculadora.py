# https://www.youtube.com/watch?v=NhNORVxdOsc

from tkinter import *

root = Tk()
root.title('Sua Calculadora')
root.geometry('1920x1080')
root.minsize(450,450)

root.configure(background='#282828')
e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',bg='#a7a28f', font= ('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row= 0,
    column= 0,
    columnspan= 4,
    pady=2
)
#funçoes para operação
def div_buttom():
    return
def click_buttom():
    return


divide = Button(
    root,
    text='/',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
multiplica = Button(
    root,
    text='x',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
soma = Button(
    root,
    text='+',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
subtrai = Button(
    root,
    text='-',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
zero = Button(
    root,
    text='0',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
um = Button(
    root,
    text='1',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
dois = Button(
    root,
    text='2',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
tres = Button(
    root,
    text='3',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
quatro = Button(
    root,
    text='4',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
cinco = Button(
    root,
    text='5',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
seis = Button(
    root,
    text='6',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
sete = Button(
    root,
    text='7',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
oito = Button(
    root,
    text='8',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)
nove = Button(
    root,
    text='9',
    padx=40,
    pady=20,
    command= div_buttom,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura',12, 'bold')
)

divide.grid(row=0, column=4)
multiplica.grid(row=1, column=4)
subtrai.grid(row=2, column=4)
soma.grid(row=3, column=4)
um.grid(row=1, column=0)
dois.grid(row=1, column=1)
tres.grid(row=1, column=2)
quatro.grid(row=2, column=0)
cinco.grid(row=2, column=1)
seis.grid(row=2, column=2)
sete.grid(row=3, column=0)
oito.grid(row=3, column=1)
nove.grid(row=3, column=2)
zero.grid(row=4, column=0)



root.mainloop()