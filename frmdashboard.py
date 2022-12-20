import tkinter as tk
import tkinter.font as tkFont
from wRegistro import Registro
from wUserCRUD import Ucrud
from frmdescuentos import Dcrud

class Dashboard(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("Menu principal")
        #setting window size
        width=500
        height=300
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_723=tk.Button(self)
        GButton_723["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_723["font"] = ft
        GButton_723["fg"] = "#000000"
        GButton_723["justify"] = "center"
        GButton_723["text"] = "Reservas"
        GButton_723.place(x=20,y=20,width=200,height=30)
        GButton_723["command"] = self.abrir_reservas

        GButton_500=tk.Button(self)
        GButton_500["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_500["font"] = ft
        GButton_500["fg"] = "#000000"
        GButton_500["justify"] = "center"
        GButton_500["text"] = "Salas"
        GButton_500.place(x=250,y=20,width=200,height=30)
        GButton_500["command"] = self.abrir_salas

        GButton_596=tk.Button(self)
        GButton_596["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_596["font"] = ft
        GButton_596["fg"] = "#000000"
        GButton_596["justify"] = "center"
        GButton_596["text"] = "Descuentos"
        GButton_596.place(x=20,y=70,width=200,height=30)
        GButton_596["command"] = self.abrir_descuentos

        GButton_852=tk.Button(self)
        GButton_852["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_852["font"] = ft
        GButton_852["fg"] = "#000000"
        GButton_852["justify"] = "center"
        GButton_852["text"] = "Usuarios"
        GButton_852.place(x=250,y=70,width=200,height=30)
        GButton_852["command"] = self.abrir_usuarios
        
        
        GButton_940=tk.Button(self)
        GButton_940["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#000000"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Organizacion"
        GButton_940.place(x=150,y=120,width=200,height=30)
        GButton_940["command"] = self.abrir_Organizacion


        
    def abrir_reservas(self):
        print("RESERVAS")


    def abrir_salas(self):
        print("SALAS")


    #def abril_descuentos(self):
        #print("DESCUENTOS")
    
    def registro(self):
        Registro(self.master)

       
    def abrir_usuarios(self):
        Ucrud(self)
    
    def abrir_descuentos(self):
        Dcrud(self)
  
    def abrir_Organizacion(self):
        print("organizacion")

