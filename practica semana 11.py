# Melvin Josué Pereira Amaya SMIS010221
# Melvin Adiel Vasquez Mejia SMIS001021

from tkinter import GROOVE, Label,Button, Tk,filedialog,messagebox
from PIL import Image,ImageTk,ImageFilter


class cargar():
   
    def __init__(self):
        self.archivo = ""
        self.size = (300,300)

    def cargarmetodo(self):
        self.archivo = filedialog.askopenfilename(title="Seleccione una imagen",filetypes=(("jpg file","*.jpg"),("png files","*.png"),("all files","*.*")))
        try:
            imagen2 = Image.open(self.archivo)
            imagen2resiz = imagen2.resize(self.size,Image.Resampling.LANCZOS)
            render2 = ImageTk.PhotoImage(imagen2resiz)
            imagen.configure(image=render2)
            imagen.image = render2
        except:
            messagebox.showerror("Procesar imagen","Debe seleccionar una imagen jpg.")

        

    def blancoNegro(self):
        if self.archivo !="":
            imagen4 = Image.open(self.archivo)
            imagenbn = imagen4.convert("L")
            imagenbnresiz = imagenbn.resize(self.size,Image.Resampling.LANCZOS)
            render4 = ImageTk.PhotoImage(imagenbnresiz)
            imagen.configure(image=render4)
            imagen.image = render4
            imagenbn.save("Imagen en blanco y negro.jpg")
            messagebox.showinfo("Procesar imagen","Se aplico el Efecto Blanco y negro.")
        else:
            messagebox.showerror("Procesar imagen","Se necesita cargar una imagen.")

    def Resaltar(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            filtro1 = imagen3.filter(ImageFilter.EMBOSS)
            image3resiz = filtro1.resize(self.size,Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(image3resiz)
            imagen.configure(image=render3)
            imagen.image = render3
            filtro1.save("Imagen Resaltada.jpg")
            messagebox.showinfo("Procesar imagen","Se resalto la imagen.")
        else:
            messagebox.showerror("Procesar imagen","Se necesita cargar una imagen.")

    def desenfoque(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            filtro2 = imagen3.filter(ImageFilter.BLUR)
            image3resiz = filtro2.resize(self.size,Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(image3resiz)
            imagen.configure(image=render3)
            imagen.image = render3
            filtro2.save("Imagen con desenfoque.jpg")
            messagebox.showinfo("Procesar imagen","Se aplico el desenfoque.")
        else:
            messagebox.showerror("Procesar imagen","Se necesita cargar una imagen.")

    def contorno(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            filtro3 = imagen3.filter(ImageFilter.CONTOUR)
            image3resiz = filtro3.resize(self.size,Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(image3resiz)
            imagen.configure(image=render3)
            imagen.image = render3
            filtro3.save("Imagen con contorno.jpg")
            messagebox.showinfo("Procesar imagen","Se aplico el contorno a la imagen.")
        else:
            messagebox.showerror("Procesar imagen","Se necesita cargar una imagen.")

ventana = Tk()
clase1 = cargar()
ancho_ventana = 550
alto_ventana = 500

x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
#ventana.geometry("550x500")
ventana.title("Procesar imagen")
ventana.configure(background='dark turquoise')
ventana.resizable(0,0)
txt0 = Label(ventana,text="Procesar imagenes ",bg='dark turquoise',font='Helvetica 16 bold')
txt0.pack()
imagen = Label(ventana,image="",bg='dark turquoise',relief=GROOVE,border=10)
imagen.place(x = 40,y = 40,width=300,height=300)
btnCargar = Button(ventana,command=clase1.cargarmetodo,text="Cargar Imagen")
btnCargar.place(x = 370,y = 150,width = 150,height = 40)
btnblancoNegro = Button(ventana,command=clase1.blancoNegro,text="Blanco/Negro")
btnblancoNegro.place(x = 40,y = 400,width = 100,height = 40)
btnDesenfoque = Button(ventana,command=clase1.desenfoque,text="Desenfoque")
btnDesenfoque.place(x = 150,y = 400,width = 100,height = 40)
btnContorno = Button(ventana,command=clase1.contorno,text="Contorno")
btnContorno.place(x = 260,y = 400,width = 100,height = 40)
btnResaltar = Button(ventana,command=clase1.Resaltar,text="Resaltar")
btnResaltar.place(x = 370,y = 400,width = 100,height = 40)
ventana.mainloop()