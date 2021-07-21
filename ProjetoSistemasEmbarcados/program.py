from tkinter import *

# pip install pillow
from PIL import Image, ImageTk



class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("sentimento.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        

        botao1 = Button(self, text="Dor",command=self.dor, bg='#24FF00')
        botao1.place(x=30, y=13)

        botao2 = Button(self, text="Falta de ar",command=self.ar, bg='#00FFF0')
        botao2.place(x=108, y=11)

        botao3 = Button(self, text="Nausea",command=self.nausea, bg='#FF6B00')
        botao3.place(x=218, y=13)

        botao4 = Button(self, text="Frio",command=self.frio, bg='#ffffff')
        botao4.place(x=127, y=110)

        botao5 = Button(self, text="Medo",command=self.medo,bg='#FFD600')
        botao5.place(x=225, y=110)

        botao6 = Button(self, text="Bem",command=self.bem,bg='#FF00C7')
        botao6.place(x=21, y=210)

        botao7 = Button(self, text="Cansado",command=self.cansado,bg='#848484')
        botao7.place(x=114, y=210)
        
        botao8 = Button(self, text="Coceira",command=self.coceira,bg='#7E71CD')
        botao8.place(x=217, y=210)
        
        botao9 = Button(self, text= "Calor",command=self.calor, bg='#FF0000')
        botao9.place(x=20, y=110) 
    
    def clickExitButton(self):
        load = Image.open("sentimento.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        

        botao1 = Button(self, text="Dor",command=self.dor, bg='#24FF00')
        botao1.place(x=30, y=13)

        botao2 = Button(self, text="Falta de ar",command=self.ar, bg='#00FFF0')
        botao2.place(x=108, y=11)

        botao3 = Button(self, text="Nausea",command=self.nausea, bg='#FF6B00')
        botao3.place(x=218, y=13)

        botao4 = Button(self, text="Frio",command=self.frio, bg='#ffffff')
        botao4.place(x=127, y=110)

        botao5 = Button(self, text="Medo",command=self.medo,bg='#FFD600')
        botao5.place(x=225, y=110)

        botao6 = Button(self, text="Bem",command=self.bem,bg='#FF00C7')
        botao6.place(x=21, y=210)

        botao7 = Button(self, text="Cansado",command=self.cansado,bg='#848484')
        botao7.place(x=114, y=210)
        
        botao8 = Button(self, text="Coceira",command=self.coceira,bg='#7E71CD')
        botao8.place(x=217, y=210)
        
        botao9 = Button(self, text= "Calor",command=self.calor, bg='#FF0000')
        botao9.place(x=20, y=110) 

    def dor(self):
        load = Image.open("dor.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)
    
    def ar(self):
        load = Image.open("ar.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)
    
    def nausea(self):
        load = Image.open("nausea.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)      

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)

    def calor(self):
        load = Image.open("calor.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)  
        
        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)

    def frio(self):
        load = Image.open("frio.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)

    def medo(self):
        load = Image.open("medo.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)

    def bem(self):
        load = Image.open("bem.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)

    def cansado(self):
        load = Image.open("cansado.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)

    def coceira(self):
        load = Image.open("coceira.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        exitButton = Button(self, text="Voltar", command=self.clickExitButton)
        exitButton.place(x=120, y=200)
    
########################################################################################

root = Tk()
app = Window(root)
root.wm_title("Sentimentos")
root.geometry("300x300")
root.mainloop()

