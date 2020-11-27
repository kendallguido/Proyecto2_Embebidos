from tkinter import *
import os

#Configuracion de ventana
window = Tk()
window.title("Proyecto")
window.geometry('800x700') #Tamaño de ventana (x, y)
window.resizable(0,0)
window.configure(bg='white')

#Imagen en ventana
path_imagen = '/home/gaby/Proyecto2_Embebidos/camera1.png'
img = PhotoImage(file = path_imagen)

#Etiqueta de ventana
lbl = Label(window, text="Sistema de Televigilancia Remota", font=("Arial Bold", 25), bg='white') #etiqueta
lbl.pack() #posicion de etiqueta

imagen1 = Label(window, image=img, bg='white')
imagen1.pack(padx= 150, pady= 150)

#Botones
#Definir funciones back.end

#Funcion boton 1
def iniciar_transmision():
	print("Iniciar transmisión")
	os.system('gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,width=640,height=480 ! autovideosink')

#Funcion boton 2	
def terminar_tranmision():
	print("Terminar transmisión")
	

#Funcion boton 3
def activar_deteccion():
	print("Activar detección")
	os.system('python3 Reconocedor.py -c 0.8 --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel')

#Funcion boton 4
def ver_registro():
	print("Ver registro")
	path_archivo = '/home/gaby/Descargas/Proyecto2_Embebidos/register.txt'
	archivo = Label(window, open(file=path_archivo))
	#archivo = open("register.txt", “r”)
	#archivo = open(file=path_archivo)

#Funcion boton 5
def salir():
	exit()

#Definir botones
#Botón 1
btn1 = Button(window, text="Iniciar tranmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=iniciar_transmision)
btn1.place(x=60, y=150)
btn1.config(state=NORMAL)

#Botón 2
btn2 = Button(window, text="Terminar tranmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=terminar_tranmision)
btn2.place(x=580, y=150)

#Botón 3
btn3 = Button(window, text="Activar detección", font=20, padx=10, pady=15, bg="white", fg="black", command=activar_deteccion)
btn3.place(x=60, y=400)

#Botón 4
btn4 = Button(window, text="Ver registro", font=20, padx=10, pady=15, bg="white", fg="black", command=ver_registro)
btn4.place(x=580, y=400)

#Botón 5
btn5 = Button(window, text="Salir", font=30, padx=10, pady=15, bg="white", fg="black", command=salir)
btn5.place(x=360, y=600)

window.mainloop()
