from tkinter import *
from tkinter.ttk import *
import sqlite3
import tkinter
import customtkinter as ctk
'''from PIL import Image'''


'''img = ctk.CTkImage(light_image=Image.open(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\lupa.png'), dark_image=Image.open(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\lupa.png'), size=(20,20))'''

janela = ctk.CTk()

janela.geometry("900x600")
janela.title("Sistema Clínica")
janela.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
       
agenda = tkinter.Label(janela,justify='left',highlightthickness=1,anchor="nw",text="Agenda",font="arial 16 bold italic",fg='purple')
agenda.place(x=20,y=10)

tabview = ctk.CTkTabview(janela, width=850, height=550,fg_color="white",segmented_button_fg_color="MediumPurple1",segmented_button_selected_hover_color="MediumPurple3",segmented_button_unselected_hover_color="MediumPurple1",segmented_button_unselected_color="MediumPurple1")
tabview.place(x=20,y=40)
tabview.add("Calendário")
tabview.add("Venda")
tabview.add("Profissional")
tabview.add("Histórico")
tabview.tab("Venda").grid_columnconfigure(40,weight=40)
tabview.tab("Profissional").grid_columnconfigure(40,weight=40)
tabview.tab("Calendário").grid_columnconfigure(40,weight=40)
tabview.tab("Histórico").grid_columnconfigure(40,weight=40,)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=190,placeholder_text="Cliente...")
entry.place(x=5,y=20)


imag= tkinter.PhotoImage(file =r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\Pessoa.png')
imag=imag.subsample(55,60)
Cad = tkinter.Button(tabview.tab("Calendário"), width=25, imag= imag)
labelimge=tkinter.Label(imag=imag)
Cad.place(x=196,y=20)

image= tkinter.PhotoImage(file =r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\lupa.png')
image=image.subsample(60,55)
pq = tkinter.Button(tabview.tab("Calendário"), width=25, image= image)
labelimg=tkinter.Label(image=image)
pq.place(x=229,y=20)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='center',placeholder_text="(  )_____-____")
entry.place(x=5,y=60)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='center',placeholder_text="Nascimento")
entry.place(x=136,y=60)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=190,placeholder_text="Serviço...")
entry.place(x=5,y=100)

Cadt = tkinter.Button(tabview.tab("Calendário"), width=3,text="+", fg="purple", font="arial 10 bold")
Cadt.place(x=196,y=100)

magee= tkinter.PhotoImage(file =r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\lp.png')
magee=magee.subsample(60,55)
pps = tkinter.Button(tabview.tab("Calendário"), width=25, image=magee)
labelimagee=tkinter.Label(image=magee)
pps.place(x=229,y=100)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='left',placeholder_text="__/__/____")
entry.place(x=5,y=140)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='left',placeholder_text="  :  ")
entry.place(x=136,y=140)

duracao = ctk.CTkOptionMenu(tabview.tab("Calendário"),width=255,values=["Duração...","30 minutos","40 minutos","50 minutos","1 hora","1 hora e 30 minutos","1 hora e 40 minutos","1 hora e 50 minutos","2 horas"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
duracao.place(x=5,y=180)

prof = ctk.CTkOptionMenu(tabview.tab("Calendário"),width=255,values=["Profissional...","Jaqueline Machado"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
prof.place(x=5,y=220)

entry = ctk.CTkEntry(tabview.tab("Calendário"),width=255,justify='left',placeholder_text="Observação...")
entry.place(x=5,y=260)

stat = ctk.CTkOptionMenu(tabview.tab("Calendário"),width=255,values=["Selecione Status...","Agendado","Atendendo","Atendido","Atrasado","Cancelado","Confirmado","Faltou"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
stat.place(x=5,y=300)

sms = tkinter.Label(tabview.tab("Calendário"),justify='left',text="Enviar SMS", fg="purple", font="arial 10")
sms.place(x=110,y=350)

sim = tkinter.Button(tabview.tab("Calendário"),justify='left',text="SIM", fg="purple", font="arial 10")
sim.place(x=184,y=350)

nao = tkinter.Button(tabview.tab("Calendário"), justify='left',text="NÃO", fg="purple", font="arial 10")
nao.place(x=218,y=350)

salvar = tkinter.Button(tabview.tab("Calendário"),text="Salvar",fg='purple', width=10,font='Times 12 bold')
salvar.place(x=5,y=450)

'''vendac = ctk.CTkTabview(tabview.tab("Venda"),width=250, height=200,fg_color="white",border_width=2,border_color="Purple")
vendac.place(x=20,y=5)

vendac1 = tkinter.Label(vendac,text="Cliente",fg='purple',font='Times 16 bold')
vendac1.place(x=5,y=20)

entry = ctk.CTkEntry(vendac,tabview.tab("Venda"),width=200,placeholder_text="Cliente...")
entry.place(x=25,y=80)

pqvc = tkinter.Button(vendac,tabview.tab("Venda"), width=3)
pqvc.place(x=225,y=80)

entry = ctk.CTkEntry(vendac,tabview.tab("Venda"), width=124,justify='center',placeholder_text="Nascimento")
entry.place(x=25,y=130)

prodserv = ctk.CTkTabview(tabview.tab("Venda"), width=250, height=200,fg_color="white",border_width=2,border_color="Purple")
prodserv.place(x=20,y=300)

pdsv = tkinter.Label(prodserv,text="Produtos / Serviços",fg='purple',font='Times 16 bold')
pdsv.place(x=5,y=20)

entry = ctk.CTkEntry(prodserv,tabview.tab("Venda"), width=200,placeholder_text="Informe Produtos / Serviços...")
entry.place(x=25,y=80)

pqps = tkinter.Button(prodserv,tabview.tab("Venda"), width=3)
pqps.place(x=225,y=80)

profps = ctk.CTkOptionMenu(prodserv,tabview.tab("Venda"),width=255,values=["Profissional...","Jaqueline Machado"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
profps.place(x=5,y=110)'''




janela.mainloop()