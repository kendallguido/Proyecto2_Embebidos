from tkinter import *

#Configuracion de ventana
window = Tk()
window.title("Proyecto")
window.geometry('800x700') #Tamaño de ventana (x, y)
window.resizable(0,0)
window.configure(bg='white')

#Imagen en ventana
path_imagen = '/home/gaby/Descargas/Proyecto2_Embebidos/camera1.png'
img = PhotoImage(file = path_imagen)

#Etiqueta de ventana
lbl = Label(window, text="Sistema de Televigilancia Remota", font=("Arial Bold", 25), bg='white') #etiqueta
lbl.pack() #posicion de etiqueta

imagen1 = Label(window, image=img, bg='white')
imagen1.pack(padx= 150, pady= 150)
#imagen1.grid(row=3, column=1)



#Botones

#Definir funciones back.end
def iniciar_transmision():
	print("Iniciar")

def terminar_tranmision():
	print("Terminar")

def ver_transmision():
	print("Ver")

def activar_deteccion():
	print("Activar")

def ver_registro(): #funcion para leer archivo
	print("Ver")
	path_archivo = '/home/gaby/Descargas/Proyecto2_Embebidos/register.txt'
	#archivo = open("register.txt", “r”)
	#archivo = open(file=path_archivo)

def importar_registro(): #funcion para leer archivo
	print("Importar")

def salir(): #funcion para cerrar app
	exit()

#Definir botones
#Botón 1
btn1 = Button(window, text="Iniciar tranmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=iniciar_transmision)
btn1.place(x=60, y=100)

#Botón 2
btn2 = Button(window, text="Terminar tranmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=terminar_tranmision)
btn2.place(x=580, y=100)

#Botón 3
btn3 = Button(window, text="Ver tranmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=ver_transmision)
btn3.place(x=60, y=300)

#Botón 4
btn4 = Button(window, text="Activar detección", font=20, padx=10, pady=15, bg="white", fg="black", command=activar_deteccion)
btn4.place(x=580, y=300)

#Botón 5
btn5 = Button(window, text="Ver registro", font=20, padx=10, pady=15, bg="white", fg="black", command=ver_registro)
btn5.place(x=60, y=500)

#Botón 6
btn6 = Button(window, text="Importar registro", font=20, padx=10, pady=15, bg="white", fg="black", command=importar_registro)
btn6.place(x=580, y=500)

#Botón 7
btn7 = Button(window, text="Salir", font=30, padx=10, pady=15, bg="white", fg="black", command=salir)
btn7.place(x=360, y=600)

window.mainloop()
