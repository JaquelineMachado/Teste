import tkinter
import sqlite3


def cxx():
    rootcx = tkinter.Tk()
    rootcx.geometry("600x500")
    rootcx.title("Sistema Clínica")
    rootcx.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
    head = tkinter.Label(rootcx,text="Contas do Cliente Serviços & Produtos", font="arial 16 bold italic", fg='purple')
    head.place(x=110, y=10)

    id = tkinter.Label(rootcx,text="ID Cliente:",font="arial 10 bold", fg='purple')
    id.place(x=20, y=60)

    C_id = tkinter.Entry(rootcx)
    C_id.place(x=90, y=60)

    dd_l = tkinter.Label(rootcx,text="Data:",font="arial 10 bold", fg='purple')
    dd_l.place(x=20, y=100)

    dd = tkinter.Entry(rootcx)
    dd.place(x=90, y=100)

    ddc = tkinter.Button(rootcx,text="Atualizar Data",font="arial 10 bold", fg='purple')
    ddc.place(x=270, y=100)

    serv = tkinter.Label(rootcx, text="Serviços :",font="arial 10 bold", fg='purple')
    serv.place(x=20, y=140)

    '''serv = tkinter.Entry(rootcx)  # temos que fazer list box dos serviços
    serv.place(x=90, y=140)
    '''

    serv_q = tkinter.Label(rootcx, text="Quantidade :",font="arial 10 bold", fg='purple')
    serv_q.place(x=280, y=140)

    serv_q = tkinter.Entry(rootcx,width=5)
    serv_q.place(x=370,y=140)

    vlsl = tkinter.Label(rootcx, text="Valor Serviços:",font="arial 10 bold", fg='purple')
    vlsl.place(x=410, y=140)

    vls_t = tkinter.Entry(rootcx,width=10)
    vls_t.place(x=520,y=140)
    
    pdr = tkinter.Label(rootcx, text="Produtos :",font="arial 10 bold", fg='purple')
    pdr.place(x=20, y=180)

    # fazer lista

    pdr_q = tkinter.Label(rootcx, text="Quantidade :",font="arial 10 bold", fg='purple')
    pdr_q.place(x=280, y=180)

    pdr_q = tkinter.Entry(rootcx,width=5)
    pdr_q.place(x=370,y=180)
    
    vpdr_q = tkinter.Label(rootcx, text="Valor Produtos :",font="arial 10 bold", fg='purple')
    vpdr_q.place(x=410, y=180)

    vpdr_t = tkinter.Entry(rootcx,width=10)
    vpdr_t.place(x=520,y=180)


    rootcx.mainloop()


    

    

