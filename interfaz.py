from tkinter import *
import subprocess
import threading
import os

reconocedor = 'python3 Reconocedor.py -c 0.8 --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel'
#Configuracion de ventana
window = Tk()
window.title("Proyecto")
window.geometry('800x700') #Tamaño de ventana (x, y)
window.resizable(0,0)
window.configure(bg='white')

#Imagen en ventana
path_imagen = 'camera1.png'
img = PhotoImage(file = path_imagen)

#Etiqueta de ventana
lbl = Label(window, text="Sistema de Televigilancia Remota", font=("Arial Bold", 25), bg='white') #etiqueta
lbl.pack() #posicion de etiqueta

imagen1 = Label(window, image=img, bg='white')
imagen1.pack(padx= 150, pady= 150)

#Botones
#Definir funciones back.end
global abrir_camara
abrir_camara = '1'
#Funcion boton 1
def iniciar_transmision():
	print("Iniciar transmisión")
	abrir_camara = 'gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,width=640,height=480 ! autovideosink'
	#camara = subprocess.Popen(abrir_camara.split())

deteccion = None
#Funcion boton 2	
def terminar_tranmision():
	global deteccion
	print("Terminar transmisión")
	if deteccion is not None: 
		deteccion.kill()
	if abrir_camara == '0':
		os.kill(abrir_camara)

#Funcion boton 3
def activar_deteccion():
	print("Activar detección")
	global deteccion
	#deteccion = subprocess.Popen(['python', 'Reconocedor.py', '-c', '0.8', '--prototxt', 'MobileNetSSD_deploy.prototxt.txt', '--model', 'MobileNetSSD_deploy.caffemodel'])
	deteccion = subprocess.Popen(reconocedor.split()) 
#Funcion boton 4
def ver_registro():
	file = os.path.isfile('register.txt')
	if file:
	
		print("Ver registro")
		archivo = "gedit"
		#this_dir = os.path.dirname(os.path.abspath(__file__))
		#path_archivo = this_dir + os.sep + 'register.txt'
		#print(path_archivo)
		#archivo = Label(window, open(file=path_archivo))
		subprocess.Popen([archivo,'register.txt'])
	else:
		window2 = Tk()
		window2.geometry('200x200')
		no_registro = Label(window2, text="No existe el archivo", font=("Arial Bold", 12), bg='white') #etiqueta
		no_registro.place(relx = 0.5, rely = 0.5, anchor = 'center') #posicion de Etiqueta
		boton_no_registro = Button(window2, text="Salir", font=20, padx=10, pady=15, bg="white", fg="black", command= lambda: window2.destroy())
		boton_no_registro.place(relx = 0.5, rely = 0.75, anchor = 'center')
		window2.mainloop()
		#print("El archivo no existe")
	#archivo = open("register.txt", “r”)
	#archivo = open(file=path_archivo)

#Funcion boton 5
def salir():
	if deteccion is not None:
		deteccion.kill()
	exit()

window.protocol("WM_DELETE_WINDOW", salir)
#Definir botones
#Botón 1
btn1 = Button(window, text="Iniciar transmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=iniciar_transmision)
btn1.place(x=60, y=150)
btn1.config(state=NORMAL)

#Botón 2
btn2 = Button(window, text="Terminar transmisión", font=20, padx=10, pady=15, bg="white", fg="black", command=terminar_tranmision)
btn2.place(x=580, y=150)

#Botón 3
btn3 = Button(window, text="Activar detección", font=20, padx=10, pady=15, bg="white", fg="black", command = lambda : threading.Thread(target = activar_deteccion).start())
btn3.place(x=60, y=400)

#Botón 4
btn4 = Button(window, text="Ver registro", font=20, padx=10, pady=15, bg="white", fg="black", command= lambda : threading.Thread(target = ver_registro).start())
btn4.place(x=580, y=400)

#Botón 5
btn5 = Button(window, text="Salir", font=30, padx=10, pady=15, bg="white", fg="black", command= salir)
btn5.place(x=360, y=600)

window.mainloop()
