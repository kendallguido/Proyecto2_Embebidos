from tkinter import *

window = Tk()

window.title("Proyecto")

lbl = Label(window, text="Sistema de Televigilancia Remota", font=("Arial Bold", 30)) #Título de ventana

lbl.grid(column=0, row=0)

window.geometry('850x850') #Tamaño de ventana

#Botones

#Definir funciones back.end
def click():

    lbl.configure(text="Click realizado")

#def leer_archivo():
	#archivo = open("register.txt", “r”)

#Definir botones
#Botón 1
btn1 = Button(window, text="Empezar tranmisión", bg="black", fg="white", command=click)

btn1.grid(column=0, row=10)

#Botón 2
btn2 = Button(window, text="Ver tranmisión", bg="black", fg="white", command=click)

btn2.grid(column=0, row=15)

#Botón 3
btn3 = Button(window, text="Terminar tranmisión", bg="black", fg="white", command=click)

btn3.grid(column=0, row=20)

#Botón 4
btn4 = Button(window, text="Activar detección", bg="black", fg="white", command=click)

btn4.grid(column=0, row=25)

#Botón 5
btn5 = Button(window, text="Importar registro", bg="black", fg="white", command=click)

btn5.grid(column=0, row=30)

#Botón 6
btn6 = Button(window, text="Ver registro", bg="black", fg="white", command=click)

btn6.grid(column=0, row=35)

#Botón 7
btn7 = Button(window, text="Salir", bg="black", fg="white", command=click)

btn7.grid(column=0, row=40)


window.mainloop()
