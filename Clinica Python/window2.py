import tkinter
import sqlite3
import tkinter.messagebox as tkMassageBox
from empreg import emp_screen
from clint import cli
from caixa import cxx
import customtkinter
from agendamento import janela
#from login import EXIT

def menu():
 global root1,button1,button2,button3,button4,button5,button6,button7

 root1 = tkinter.Tk()
 root1.geometry("200x500")
 root1.title("Sistema Clínica")
 root1.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
 m=tkinter.Label(root1, text="Menu",font='Times 16 bold italic',fg='purple')
     
 button1 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Agendamento",command=AGENDA, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button2 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Clientes", command=CLI, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button3 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Caixa",command=CAIXA, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button4 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Profissional",command=PROF, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button5 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw",text="Produtos e Serviços", bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button6 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Configurações", bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button7 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Sair",command=EXIT, bg='MediumPurple1', fg='purple', width=15,font='Times 12')
 
 m.place(x=20,y=-2)

 button1.pack(side=tkinter.TOP)
 button1.place(x=20,y=25)
    
 button2.pack(side=tkinter.TOP)
 button2.place(x=20,y=55)
    
 button3.pack(side=tkinter.TOP)
 button3.place(x=20,y=85)
    
 button4.pack(side=tkinter.TOP)
 button4.place(x=20,y=115)
    
 button5.pack(side=tkinter.TOP)
 button5.place(x=20,y=145)
    
 button6.pack(side=tkinter.TOP)
 button6.place(x=20,y=175)
    
 button7.pack(side=tkinter.TOP)
 button7.place(x=20,y=205)

 root1.mainloop()

 back = None
 SEARCH = None
 DELETE = None
 UPDATE = None
 NOVO = None
'''
 def CLI():
    root1.destroy()
    global cli_ID,cli_name,cli_sex,cli_dob,cli_cpf,cli_rg,cli_contact,cli_contactout,cli_email,cli_addr,cli_pro
    global rootc,regfrom,id,name,sex,dob,cpf,rg,c1,c2,email,addr,pro,filemenu,back,SUBMIT,menubar,SEARCH,DELETE,UPDATE

    menubar = tkinter.Menu(rootc)
    filemenu = tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="Novo",command=CLI)
    filemenu.add_separator()
    filemenu.add_command(label="Sair")

    rootc = tkinter.Tk()
    rootc.configure(background="darksalmon")
    rootc.title("Cadastro Clientes")

    regfrom = tkinter.Label(rootc,text="Cadastro Clientes",font="arial 16 bold",fg='purple')

    id = tkinter.Label(rootc,text="ID Cliente:",font="arial 8 bold",fg='purple')
    cli_ID = tkinter.Entry(rootc,width=12)

    name = tkinter.Label(rootc,text="Nome Cliente:",font="arial 8 bold",fg='purple')
    cli_name = tkinter.Entry(rootc,width=50)

    sex = tkinter.Label(rootc,text="Sexo:",font="arial 8 bold",fg='purple')
    cli_sex = tkinter.Entry(rootc,width=12)

    dob = tkinter.Label(rootc,text="Data Nascimento: (YYYY-MM-DD)",font="arial 8 bold",fg='purple')
    cli_dob = tkinter.Entry(rootc,width=12)

    cpf = tkinter.Label(rootc,text="CPF:",font="arial 8 bold",fg='purple')
    cli_cpf = tkinter.Entry(rootc,width=12)

    rg = tkinter.Label(rootc,text="RG:",font="arial 8 bold",fg='purple')
    cli_rg = tkinter.Entry(rootc,width=12)

    c1 = tkinter.Label(rootc,text="Telefone Celular:",font="arial 8 bold",fg='purple')
    cli_contact = tkinter.Entry(rootc,width=26)

    c2 = tkinter.Label(rootc,text="Telefone Outros:",font="arial 8 bold",fg='purple')
    cli_contactout = tkinter.Entry(rootc,width=26)

    email = tkinter.Label(rootc,text="E-mail:",font="arial 8 bold",fg='purple')
    cli_email = tkinter.Entry(rootc,width=50)

    addr = tkinter.Label(rootc,text="Endereço:",font="arial 8 bold",fg='purple')
    cli_addr = tkinter.Entry(rootc,width=50)

    pro = tkinter.Label(rootc,text="Profissional:",font="arial 8 bold",fg='purple')
    cli_pro = tkinter.Entry(rootc,width=30)

    back= tkinter.Button(rootc,text="< Voltar",font="arial 8 bold",fg='purple')
    SEARCH = tkinter.Button(rootc,text="Pesquisar",font="arial 8 bold",fg='purple')
    DELETE = tkinter.Button(rootc,text="Deletar",font="arial 8 bold",fg='purple')
    UPDATE = tkinter.Button(rootc,text="Atualizar",font="arial 8 bold",fg='purple')
    SUBMIT = tkinter.Button(rootc,text="Cadastrar",font="arial 8 bold",fg='purple')

    root1.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
    regfrom.pack()
    id.pack()
    cli_ID.pack()
    name.pack()
    cli_name.pack()
    sex.pack()
    cli_sex.pack()
    dob.pack()
    cli_dob.pack()
    cpf.pack()
    cli_cpf.pack()
    rg.pack()
    cli_rg.pack()
    c1.pack()
    cli_contact.pack()
    c2.pack()
    cli_contactout.pack()
    email.pack()
    cli_email.pack()
    addr.pack()
    cli_addr.pack()
    pro.pack()
    cli_pro.pack()

   
    SUBMIT.pack()
    SEARCH.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    UPDATE.pack(side=tkinter.LEFT)
    back.pack(side=tkinter.LEFT)

    
    rootc.mainloop()
'''
def EXIT():
 result = tkMassageBox.askquestion('Sistema Clínica','Deseja sair?')
 if result == 'Sim':
   menu.destroy()
   exit()

def PROF():
  if button4 == button4:
    emp_screen()
def CLI():
  if button2 == button2:
    cli()
def CAIXA():
  if button3 == button3:
    cxx()
def AGENDA():
  if button1 == button1:
    janela
   




    




