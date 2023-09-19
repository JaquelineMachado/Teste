import tkinter
import sqlite3

def emp_screen():
    rootE = tkinter.Tk()
    rootE.title("Profissional")
    rootE.geometry("700x700")
    rootE.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')

    var = tkinter.StringVar(master = rootE)

    C = tkinter.Label(rootE,text="Profissional", fg="purple", font="arial 16 bold italic")
    C.place(x=20,y=20)

    l1 = tkinter.Label(rootE,justify='left',highlightthickness=1,anchor="nw",text="ID Profissional", fg="purple", font="arial 12 bold")
    l1.place(x=20,y=50)

    t1 = tkinter.Entry(rootE)
    t1.place(x=50,y=80)

    l2 = tkinter.Label(rootE,justify='left',highlightthickness=1,anchor="nw",text="Nome Profissional", fg="purple", font="arial 12 bold")
    l2.place(x=20,y=110)

    t2 = tkinter.Entry(rootE,width=40)
    t2.place(x=50,y=140)

    l3 = tkinter.Label(rootE,justify='left',highlightthickness=1,anchor="nw",text="Telefone", fg="purple", font="arial 12 bold")
    l3.place(x=20,y=170)

    t3 = tkinter.Entry(rootE)
    t3.place(x=50,y=200)

    l4 = tkinter.Label(rootE,justify='left',highlightthickness=1,anchor="nw",text="E-mail", fg="purple", font="arial 12 bold")
    l4.place(x=20,y=230)

    t4 = tkinter.Entry(rootE,width=40)
    t4.place(x=50,y=260)

    l5 = tkinter.Label(rootE,justify='left',highlightthickness=1,anchor="nw",text="Senha", fg="purple", font="arial 12 bold")
    l5.place(x=20,y=290)

    t5 = tkinter.Entry(rootE)
    t5.place(x=50,y=320)

    l6 = tkinter.Label(rootE,justify='left',highlightthickness=1,anchor="nw",text="Grupo Profissional", fg="purple", font="arial 12 bold")
    l6.place(x=20,y=350)

    scrollbar = tkinter.Scrollbar(rootE)
    scrollbar.place(x=20,y=380)

    lb = tkinter.Listbox(rootE,selectmode= 'SINGLE',exportselection= 0,height= 4,width= 15)
    lb.insert(tkinter.END,"Administração")
    lb.insert(tkinter.END,"Prof Saúde")
    lb.insert(tkinter.END,"Recepção")
    lb.place(x=20,y=380)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)

    l7 = tkinter.Label(rootE,justify='center',text="Último Acesso(YYYY:MM:DD)(HH:MM:SS)", fg="purple", font="arial 12 bold")
    l7.place(x=20,y=500)

    t7 = tkinter.Entry(rootE)
    t7.place(x=140,y=550)


    Cad = tkinter.Button(rootE,justify='center',text="Cadastrar",fg='purple', width=10,font='Times 12 bold')
    Cad.place(x=315,y=590)

    rootE.mainloop()
