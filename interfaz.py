#Interfaz para el proyecto #1- Relaciones

from tkinter import *
import time
import tkinter.messagebox  ##para la ventana de decision
from tkinter import simpledialog as sdg
from turtle import *
from propAntisimetrica import *
from propIrreflexiva import *
from propReflexiva import *
from propSimetrica import *
from propTransitiva import *
from validacionGeneral import *


"""Variables globales"""
elementosConjunto = []
conjunto=[]

def Fn(v):
    result = self._oldvalue
    self._oldvalue = v
    print(result)
	
	
	##Funcion Reloj
time1 =''
def reloj ():  ##Solo es un reloj de adorno
	global time1
	time2 = time.strftime ('%H:%M:%S')
	if time2 != time1:
		time1 = time2
		clock.configure (text=time2)
	clock.after(500,reloj)
	
	
##Funcion para el boton de salida
def salirPrograma():
	respuesta = tkinter.messagebox.askyesno("Saliendo del programa...","Esta seguro que desea salir del programa?")
	if(respuesta==True):
			ventanaPrincipal.quit()
			
			
def generarSpinBox(cantidad, ventana,  posX, posY): 
	global spinBox1, spinBox2,spinBox3,spinBox4,spinBox5,spinBox6

	if(cantidad == 1):
		e1= Label(ventana,text="Rel 1:", font=('Consolas', 9), bg="black", fg="white" ).place(x=3,y=posY+120)
		e1 = Spinbox(ventana,wrap=True,textvariable= spinBox1, width=2, from_=1,to=10).place(x=70, y= posY+120)
		
	elif(cantidad ==2):
		e1= Label(ventana,text="Rel 1:", font=('Consolas', 9), bg="black", fg="white" ).place(x=3,y=posY+120)
		e1 = Spinbox(ventana,wrap=True,textvariable= spinBox1, width=2, from_=1,to=10).place(x=70, y= posY+120)
		
		e2= Label(ventana,text="Rel 2:", font=('Consolas', 9), bg="black", fg="white" ).place(x=98,y=posY+120)
		e2 = Spinbox(ventana,wrap=True,textvariable= spinBox2, width=2, from_=1,to=10).place(x=156, y= posY+120)
		
	elif(cantidad ==3):
		e1= Label(ventana,text="Rel 1:", font=('Consolas', 9), bg="black", fg="white" ).place(x=3,y=posY+120)
		e1 = Spinbox(ventana,wrap=True,textvariable= spinBox1, width=2, from_=1,to=10).place(x=70, y= posY+120)
		
		e2= Label(ventana,text="Rel 2:", font=('Consolas', 9), bg="black", fg="white" ).place(x=98,y=posY+120)
		e2 = Spinbox(ventana,wrap=True,textvariable= spinBox2, width=2, from_=1,to=10).place(x=156, y= posY+120)
		
		e3= Label(ventana,text="Rel 3:", font=('Consolas', 9), bg="black", fg="white" ).place(x=189,y=posY+120)
		e3 = Spinbox(ventana,wrap=True,textvariable= spinBox3, width=2, from_=1,to=10).place(x=242, y= posY+120)
		
	elif(cantidad ==4):
		e1= Label(ventana,text="Rel 1:", font=('Consolas', 9), bg="black", fg="white" ).place(x=3,y=posY+120)
		e1 = Spinbox(ventana,wrap=True,textvariable= spinBox1, width=2, from_=1,to=10).place(x=70, y= posY+120)
		
		e2= Label(ventana,text="Rel 2:", font=('Consolas', 9), bg="black", fg="white" ).place(x=98,y=posY+120)
		e2 = Spinbox(ventana,wrap=True,textvariable= spinBox2, width=2, from_=1,to=10).place(x=156, y= posY+120)
		
		e3= Label(ventana,text="Rel 3:", font=('Consolas', 9), bg="black", fg="white" ).place(x=189,y=posY+120)
		e3 = Spinbox(ventana,wrap=True,textvariable= spinBox3, width=2, from_=1,to=10).place(x=242, y= posY+120)
		
		e4= Label(ventana,text="Rel 4:", font=('Consolas', 9), bg="black", fg="white" ).place(x=282,y=posY+120)
		e4 = Spinbox(ventana,wrap=True,textvariable= spinBox4, width=2, from_=1,to=10).place(x=329, y= posY+120)
	
	elif(cantidad ==5):
		e1= Label(ventana,text="Rel 1:", font=('Consolas', 9), bg="black", fg="white" ).place(x=3,y=posY+120)
		e1 = Spinbox(ventana,wrap=True,textvariable= spinBox1, width=2, from_=1,to=10).place(x=70, y= posY+120)
		
		e2= Label(ventana,text="Rel 2:", font=('Consolas', 9), bg="black", fg="white" ).place(x=98,y=posY+120)
		e2 = Spinbox(ventana,wrap=True,textvariable= spinBox2, width=2, from_=1,to=10).place(x=156, y= posY+120)
		
		e3= Label(ventana,text="Rel 3:", font=('Consolas', 9), bg="black", fg="white" ).place(x=189,y=posY+120)
		e3 = Spinbox(ventana,wrap=True,textvariable= spinBox3, width=2, from_=1,to=10).place(x=242, y= posY+120)
		
		e4= Label(ventana,text="Rel 4:", font=('Consolas', 9), bg="black", fg="white" ).place(x=282,y=posY+120)
		e4 = Spinbox(ventana,wrap=True,textvariable= spinBox4, width=2, from_=1,to=10).place(x=329, y= posY+120)
		
		e5= Label(ventana,text="Rel 5:", font=('Consolas', 9), bg="black", fg="white" ).place(x=369,y=posY+120)
		e5 = Spinbox(ventana,wrap=True,textvariable= spinBox5, width=2, from_=1,to=10).place(x=412, y= posY+120)		
	
	elif(cantidad ==6):
		e1= Label(ventana,text="Rel 1:", font=('Consolas', 9), bg="black", fg="white" ).place(x=3,y=posY+120)
		e1 = Spinbox(ventana,wrap=True,textvariable= spinBox1, width=2, from_=1,to=10).place(x=70, y= posY+120)
		
		e2= Label(ventana,text="Rel 2:", font=('Consolas', 9), bg="black", fg="white" ).place(x=98,y=posY+120)
		e2 = Spinbox(ventana,wrap=True,textvariable= spinBox2, width=2, from_=1,to=10).place(x=156, y= posY+120)
		
		e3= Label(ventana,text="Rel 3:", font=('Consolas', 9), bg="black", fg="white" ).place(x=189,y=posY+120)
		e3 = Spinbox(ventana,wrap=True,textvariable= spinBox3, width=2, from_=1,to=10).place(x=242, y= posY+120)
		
		e4= Label(ventana,text="Rel 4:", font=('Consolas', 9), bg="black", fg="white" ).place(x=282,y=posY+120)
		e4 = Spinbox(ventana,wrap=True,textvariable= spinBox4, width=2, from_=1,to=10).place(x=329, y= posY+120)
		
		e5= Label(ventana,text="Rel 5:", font=('Consolas', 9), bg="black", fg="white" ).place(x=369,y=posY+120)
		e5 = Spinbox(ventana,wrap=True,textvariable= spinBox5, width=2, from_=1,to=10).place(x=412, y= posY+120)
		
		e6= Label(ventana,text="Rel 6:", font=('Consolas', 9), bg="black", fg="white" ).place(x=457,y=posY+120)
		e6 = Spinbox(ventana,wrap=True,textvariable= spinBox6, width=2, from_=1,to=10).place(x=497, y= posY+120)
	
	

##Funcion para  las ventanas
def ejecutar(f): 
	try:
		ventana.after(200,ejecutar)
	except ventana:
		print("Abrio ventana")

##Funcion para  las ventanas
def mostrarVentana(ventana):
	try:
		ventana.deiconify()
		
	except ventana:
		ventana.deiconify()
		print("Abrio ventana")


		
##Funcion para  las ventanas	
def ocultarVentana(ventana):
	try:
		ventana.withdraw()
	except ventana:
		print("Oculto ventana")
		
#Variables para los spinBox


##########################################################--------------------CONFIG. PANTALLA PRINCIPAL--------------------------------##########################################################
##Configuracion pantalla
ventanaPrincipal=Tk()
ventanaPrincipal.title("PROYECTO #1. Relaciones")
ventanaPrincipal.attributes("-alpha", 0.91) #Esto sirve para transparentar ventanas
ventanaPrincipal.geometry("800x500+200+200")  ##Tamanio y la posicion donde va aparecer
ventanaPrincipal.config(bg='black')
#asas=Image.open("asas.png")
"""imagenFondo = PhotoImage(file= "asas.png")"""
"""labelFondo = Label(ventanaPrincipal, image = imagenFondo).place(x=-1,y=-50)"""
ventanaPrincipal.maxsize(height=1400, width=800)
encabezado1 = Label(ventanaPrincipal, text = "PROYECTO #1. Relaciones", font=('Consolas', 23), bg="black",  fg="yellow").place(x=50,y=400)
botonInformacion=Button(ventanaPrincipal, text="Informacion", bg = "black", fg="white",height=4, width=15, command = lambda: mostrarVentana(ventanaInformacion)).place(x=600,y=120)
botonRelaciones=Button(ventanaPrincipal, text="Verificar \n Relaciones", bg = "black", fg="white",height=4, width=15, command = lambda:mostrarVentana(ventanaMenu)).place(x=600,y=221)
botonSalir=Button(ventanaPrincipal, text="Salir de \n la aplicacion", bg = "blue", fg="white", command=lambda: salirPrograma())
botonSalir.grid(row=1,column=9)
	

	

##Creando ventanas para los botones
#Instanciando ventanas
ventanaInformacion = Toplevel(ventanaPrincipal)
ventanaInformacion.withdraw()
ventanaMenu = Toplevel(ventanaPrincipal)
ventanaMenu.withdraw()
ventanaRelaciones = Toplevel(ventanaMenu)
ventanaRelaciones.withdraw()
ventanaResultados = Toplevel(ventanaMenu)
ventanaResultados.withdraw()


	##Reloj
clock = Label(ventanaPrincipal, font=('Consolas', 18), bg="Black", fg="yellow")
#clock.pack()
clock.place (x=640, y=450)
reloj ()



##########################################################--------------------VENTANA "INFORMACION DEL PROGRAMA"--------------------------------##########################################################
ventanaInformacion.geometry("400x220+380+350")
ventanaInformacion.config(bg="black")
ventanaInformacion.maxsize(height=420, width=400)
ventanaInformacion.attributes("-alpha", 0.78) #Esto sirve para transparentar ventanas
#l1 = Label(ventanaInformacion, image = imagenFondo).place(x=-15,y=-20)
version = Label(ventanaInformacion,text="Version del programa: 1.4.0").place(x=130,y=155)

	#Nombres de nosotros
unamLabel = Label(ventanaInformacion,text="Universidad Nacional Autonoma de Mexico", font=('Consolas', 14), bg="black", fg="yellow").place(x=0,y=-4)
fiLabel =   Label(ventanaInformacion,text="       Facultad de Ingenieria  ", font=('Consolas', 14), bg="black", fg="yellow").place(x=0,y=21)
fiLabel = Label(ventanaInformacion,text="*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-", font=('Consolas', 14), bg="black", fg="blue").place(x=0,y=50)
nombre1 = Label(ventanaInformacion,text="Desarrolladores:" , font=('Consolas', 14), bg="Black", fg="white").place(x=30,y=80)
nombre1 = Label(ventanaInformacion,text="***Lemuz Fuentes Omar Alejandro", font=('Consolas', 11), bg="Black", fg="white").place(x=30,y=100)
nombre2 = Label(ventanaInformacion,text="***Ramirez Castillo Miguel Angel", font=('Consolas', 11), bg="Black", fg="white").place(x=30,y=120)
		
		

		
##########################################################--------------------VENTANA MENU "Relaciones"--------------------------------##########################################################
ventanaMenu.title("MENU RELACIONES")
ventanaMenu.attributes("-alpha", 0.91) #Esto sirve para transparentar ventanas
ventanaMenu.geometry("300x200+300+300")  ##Tamanio y la posicion donde va aparecer
ventanaMenu.config(bg='black')
ventanaMenu.maxsize(height=300, width=200)
"""imFondo = PhotoImage(file= "max.png")"""
"""labelFondo = Label(ventanaMenu, image = imFondo).place(x=-55,y=-120)"""
encabezado1 = Label(ventanaMenu, text = "Menu del programa", font=('Consolas', 15), bg="black",  fg="yellow").grid(row=0,column=0)
lblInstrucciones = Label(ventanaMenu, text = "Ejecute secuencialmente \ncada uno de los botones \nde este menu", font=('Consolas', 10), bg="black",  fg="white").grid(row=1,column=0)
btnInsertarConjunto=Button(ventanaMenu, text="Insertar elementos \ndel conjunto", bg = "black", fg="white", command=lambda: anadirElementosConjunto()).grid(row=2,column=0)
btnInsertarRelaciones=Button(ventanaMenu, text="Insertar relaciones", bg = "black", fg="white", command=lambda: mostrarVentana(ventanaRelaciones)).grid(row=3,column=0)
btnVerTabla=Button(ventanaMenu, text="Ver resultados", bg = "black", fg="white", command=lambda: mostrarVentana(ventanaResultados)).grid(row=4,column=0)


##########################################################--------------------VENTANA ANIADIR CONJUNTO--------------------------------##########################################################
"""La funcion de esta ventana es para que al obtener los elementos del conjunto en una lista, estos puedan compararse con los que se inserten en las relaciones y pertenezcan al conjunto"""
def anadirElementosConjunto():
	global elementosConjunto
	global conjunto
	conjunto=[]
	elementosConjunto =  sdg.askstring('Elementos del conjunto', 'Escriba los elementos del conjunto  separados por coma [MAXIMO 6] \n En caso de que se inserten mas de 6, el sistema tomara los SEIS primeros: ')
	elementosConjunto = elementosConjunto.split(',')
	if len(elementosConjunto)==1:
		if not elementosConjunto[0]:
			print("lista vacia")
			elementosConjunto.pop(0)
			tkinter.messagebox.showinfo(title= "ADVERTENCIA!", message= "No insertó ningún elemento al conjunto! INGRÉSELOS!")
		else:
			conjunto.append(int(elementosConjunto[0]))
		print("3. ", conjunto)

	elif len(elementosConjunto) >6:
		tkinter.messagebox.showinfo(title= "ADVERTENCIA!", message= "Usted insertaron mas de 6 elementos, SE TOMARAN UNICAMENTE LOS 6 PRIMEROS.")
		for i in range(0, len(elementosConjunto)):
			conjunto.append(int(elementosConjunto[i]))
		conjunto = conjunto[0:6]
		print("2. ", conjunto)

	else:
		for i in range(0, len(elementosConjunto)):
			conjunto.append(int(elementosConjunto[i]))
		print("1. ", conjunto)
	


"""Variables para RadioButton"""
radioButNumRelaciones = IntVar() 
spinBox1 = IntVar()
spinBox2 = IntVar()
spinBox3 = IntVar()
spinBox4 = IntVar()
spinBox5 = IntVar()
spinBox6 = IntVar()

###FUNCION PARA OBTENER VALORES DE SPINBOX###
def getval():
	global txtb1, txtb2, txtb3, txtb4, txtb5, txtb6
	global a,b,c,d,e,f
	a=int(spinBox1.get())
	b=int(spinBox2.get())
	c=int(spinBox3.get())
	d=int(spinBox4.get())
	e=int(spinBox5.get())
	f=int(spinBox6.get())
	print("Elementos para relaciones: ", a,b,c,d,e,f)
	adlab=Label(ventanaRelaciones, text="Ingrese los conjuntos ordenados entre paréntesis y separados por una coma dentro y u por un espacio fuera de estos... (x,y) (y,x)", font=('Consolas', 10), bg="black", fg="white").place(x=0,y=220)
	adlab2=Label(ventanaRelaciones, text="En caso de que introduzca mas conjuntos de los ya seleccionados arriba solo se tomaran los primeros x conjuntos", font=('Consolas', 10), bg="black", fg="white").place(x=0,y=240)
	if a!=0:
		lbl1=Label(ventanaRelaciones, text="Relacion 1:", font=('Consolas', 13), bg="black", fg="white").place(x=0,y=270)
		txtb1=Entry(ventanaRelaciones,width=40)
		txtb1.place(x=110,y=273)
		boton2=Button(ventanaRelaciones, text="Cargar relaciones", bg = "black", fg="white", command=lambda: getrel()).place(x=30,y=460)
		
		if b!=0:
			lbl2=Label(ventanaRelaciones, text="Relacion 2:", font=('Consolas', 13), bg="black", fg="white").place(x=0,y=300)
			txtb2=Entry(ventanaRelaciones,width=40)
			txtb2.place(x=110,y=303)
			if c!=0:
				lbl3=Label(ventanaRelaciones, text="Relacion 3:", font=('Consolas', 13), bg="black", fg="white").place(x=0,y=330)
				txtb3=Entry(ventanaRelaciones,width=40)
				txtb3.place(x=110,y=333)
				if d!=0:
					lbl4=Label(ventanaRelaciones, text="Relacion 4:", font=('Consolas', 13), bg="black", fg="white").place(x=0,y=360)
					txtb4=Entry(ventanaRelaciones,width=40)
					txtb4.place(x=110,y=363)
					if e!=0:
						lbl5=Label(ventanaRelaciones, text="Relacion 5:", font=('Consolas', 13), bg="black", fg="white").place(x=0,y=390)
						txtb5=Entry(ventanaRelaciones,width=40)
						txtb5.place(x=110,y=393)
						if f!=0:
							lbl6=Label(ventanaRelaciones, text="Relacion 6:", font=('Consolas', 13), bg="black", fg="white").place(x=0,y=420)
							txtb6=Entry(ventanaRelaciones,width=40)
							txtb6.place(x=110,y=423)

def getrel():
	global u, v, w, x, y, z, conjunto
	listaComprobatoria = []  #Esta lista booleana tiene como objetivo guardar 1 si se anadieron las relaciones y 0 si no (y tenian que anadirse pares ordenados)
	if(len(conjunto)!= 0):
		if a!=0:
			u=txtb1.get()
			u=u.replace(")", "")
			u=u.replace("(", "")
			u=u.split()
			u=u[0:a]
			u=cast(u)
			pertenenciaa = pertenenciaAlConjunto(conjunto, u)
			if pertenenciaa == 1:
				if(len(u)!= 0):
					listaComprobatoria.append(1)
					u1=propiedadReflexiva(conjunto, u)
					u2=propiedadSimetrica(conjunto, u)
					u3=propiedadTransitiva(conjunto, u)
					u4=propiedadAntisimetrica(conjunto, u)
					u5=propiedadIrreflexiva(conjunto, u)
					print("Relacion 1:", u1, u2, u3, u4, u5)
				
					lblru = Label(ventanaResultados, text=str(u1), font=('Consolas', 10), bg="black", fg="white").grid(row=3,column=3)
					lblsu = Label(ventanaResultados, text=str(u2), font=('Consolas', 10), bg="black", fg="white").grid(row=3,column=5)
					lbltu = Label(ventanaResultados, text=str(u3), font=('Consolas', 10), bg="black", fg="white").grid(row=3,column=7)
					lblau = Label(ventanaResultados, text=str(u4), font=('Consolas', 10), bg="black", fg="white").grid(row=3,column=9)
					lbliu = Label(ventanaResultados, text=str(u5), font=('Consolas', 10), bg="black", fg="white").grid(row=3,column=11)
				else:
					
					tkinter.messagebox.showinfo(title= "ALERTA!", message= "No se anadio ninguna pareja ordenada en la RELACION 1")
			else:
				listaComprobatoria.append(0)
				tkinter.messagebox.showinfo(title= "ANULANDO OPERACION!", message= "AlGUNO DE LOS PARES ORDENADOS DE LA REL. 1 NO PERTENECE AL CONJUNTO!")
			
			if b!=0:
				v=txtb2.get()
				v=v.replace(")", "")
				v=v.replace("(", "")
				v=v.split()
				v=v[0:b]
				v=cast(v)
				pertenenciab = pertenenciaAlConjunto(conjunto, v)
				if pertenenciab == 1:
					if(len(v)!= 0):
						listaComprobatoria.append(1)
						v1=propiedadReflexiva(conjunto, v)
						v2=propiedadSimetrica(conjunto, v)
						v3=propiedadTransitiva(conjunto, v)
						v4=propiedadAntisimetrica(conjunto, v)
						v5=propiedadIrreflexiva(conjunto, v)
						print("Relacion 2: ", v1, v2, v3, v4, v5)
						
						lblrv = Label(ventanaResultados, text=str(v1), font=('Consolas', 10), bg="black", fg="white").grid(row=5,column=3)
						lblsv = Label(ventanaResultados, text=str(v2), font=('Consolas', 10), bg="black", fg="white").grid(row=5,column=5)
						lbltv = Label(ventanaResultados, text=str(v3), font=('Consolas', 10), bg="black", fg="white").grid(row=5,column=7)
						lblav = Label(ventanaResultados, text=str(v4), font=('Consolas', 10), bg="black", fg="white").grid(row=5,column=9)
						lbliv = Label(ventanaResultados, text=str(v5), font=('Consolas', 10), bg="black", fg="white").grid(row=5,column=11)
					else:
						
						tkinter.messagebox.showinfo(title= "ALERTA!", message= "No se anadio ninguna pareja ordenada en la RELACION 2")
				else:
					listaComprobatoria.append(0)
					tkinter.messagebox.showinfo(title= "ERROR GRAVE!", message= "AlGUNO DE LOS PARES ORDENADOS DE LA REL. 2 NO PERTENECE AL CONJUNTO!")
			
				if c!=0:
					w=txtb3.get()
					w=w.replace(")", "")
					w=w.replace("(", "")
					w=w.split()
					w=w[0:c]
					w=cast(w)
					pertenenciac = pertenenciaAlConjunto(conjunto, w)
					if pertenenciac == 1:
						if(len(w)!= 0):
							listaComprobatoria.append(1)
							w1=propiedadReflexiva(conjunto, w)
							w2=propiedadSimetrica(conjunto, w)
							w3=propiedadTransitiva(conjunto, w)
							w4=propiedadAntisimetrica(conjunto, w)
							w5=propiedadIrreflexiva(conjunto, w)
							print("Relacion 3: ", w1, w2, w3, w4, w5)
							
							lblrw = Label(ventanaResultados, text=str(w1), font=('Consolas', 10), bg="black", fg="white").grid(row=7,column=3)
							lblsw = Label(ventanaResultados, text=str(w2), font=('Consolas', 10), bg="black", fg="white").grid(row=7,column=5)
							lbltw = Label(ventanaResultados, text=str(w3), font=('Consolas', 10), bg="black", fg="white").grid(row=7,column=7)
							lblaw = Label(ventanaResultados, text=str(w4), font=('Consolas', 10), bg="black", fg="white").grid(row=7,column=9)
							lbliw = Label(ventanaResultados, text=str(w5), font=('Consolas', 10), bg="black", fg="white").grid(row=7,column=11)
						else:
							
							tkinter.messagebox.showinfo(title= "ALERTA!", message= "No se anadio ninguna pareja ordenada en la RELACION 3")
					else:
						listaComprobatoria.append(0)
						tkinter.messagebox.showinfo(title= "ERROR GRAVE!", message= "AlGUNO DE LOS PARES ORDENADOS DE LA REL. 3 NO PERTENECE AL CONJUNTO!")
					
					if d!=0:
						x=txtb4.get()
						x=x.replace(")", "")
						x=x.replace("(", "")
						x=x.split()
						x=x[0:d]
						x=cast(x)
						pertenenciad = pertenenciaAlConjunto(conjunto, x)
						if pertenenciad == 1:
							if(len(x)!= 0):
								listaComprobatoria.append(1)
								x1=propiedadReflexiva(conjunto, x)
								x2=propiedadSimetrica(conjunto, x)
								x3=propiedadTransitiva(conjunto, x)
								x4=propiedadAntisimetrica(conjunto, x)
								x5=propiedadIrreflexiva(conjunto, x)
								print("Relacion4: ", x1, x2, x3, x4, x5)
								
								lblrx = Label(ventanaResultados, text=str(x1), font=('Consolas', 10), bg="black", fg="white").grid(row=9,column=3)
								lblsx = Label(ventanaResultados, text=str(x2), font=('Consolas', 10), bg="black", fg="white").grid(row=9,column=5)
								lbltx = Label(ventanaResultados, text=str(x3), font=('Consolas', 10), bg="black", fg="white").grid(row=9,column=7)
								lblax = Label(ventanaResultados, text=str(x4), font=('Consolas', 10), bg="black", fg="white").grid(row=9,column=9)
								lblix = Label(ventanaResultados, text=str(x5), font=('Consolas', 10), bg="black", fg="white").grid(row=9,column=11)
							else:
								
								tkinter.messagebox.showinfo(title= "ALERTA!", message= "No se anadio ninguna pareja ordenada en la RELACION 4")
						else:
							listaComprobatoria.append(0)
							tkinter.messagebox.showinfo(title= "ERROR GRAVE!", message= "AlGUNO DE LOS PARES ORDENADOS DE LA REL.4 NO PERTENECE AL CONJUNTO!")
						
						
						if e!=0:
							y=txtb5.get()
							y=y.replace(")", "")
							y=y.replace("(", "")
							y=y.split()
							y=y[0:e]
							y=cast(y)
							pertenenciae = pertenenciaAlConjunto(conjunto, y)
							if pertenenciae == 1:
								if(len(y)!= 0):
									listaComprobatoria.append(1)
									y1=propiedadReflexiva(conjunto, y)
									y2=propiedadSimetrica(conjunto, y)
									y3=propiedadTransitiva(conjunto, y)
									y4=propiedadAntisimetrica(conjunto, y)
									y5=propiedadIrreflexiva(conjunto, y)
									print("Relacion 5", y1, y2, y3, y4, y5)
									
									lblry = Label(ventanaResultados, text=str(y1), font=('Consolas', 10), bg="black", fg="white").grid(row=11,column=3)
									lblsy = Label(ventanaResultados, text=str(y2), font=('Consolas', 10), bg="black", fg="white").grid(row=11,column=5)
									lblty = Label(ventanaResultados, text=str(y3), font=('Consolas', 10), bg="black", fg="white").grid(row=11,column=7)
									lblay = Label(ventanaResultados, text=str(y4), font=('Consolas', 10), bg="black", fg="white").grid(row=11,column=9)
									lbliy = Label(ventanaResultados, text=str(y5), font=('Consolas', 10), bg="black", fg="white").grid(row=11,column=11)
								else:
									
									tkinter.messagebox.showinfo(title= "ALERTA!", message= "No se anadio ninguna pareja ordenada en la RELACION 5")
							else:
								listaComprobatoria.append(0)
								tkinter.messagebox.showinfo(title= "ERROR GRAVE!", message= "AlGUNO DE LOS PARES ORDENADOS DE LA REL. 5 NO PERTENECE AL CONJUNTO!")
								
								
							if f!=0:
								z=txtb6.get()
								z=z.replace(")", "")
								z=z.replace("(", "")
								z=z.split()
								z=z[0:f]
								z=cast(z)
								pertenenciaf = pertenenciaAlConjunto(conjunto, z)
								if pertenenciaf == 1:
									if(len(z)!= 0):
										listaComprobatoria.append(1)
										z1=propiedadReflexiva(conjunto, z)
										z2=propiedadSimetrica(conjunto, z)
										z3=propiedadTransitiva(conjunto, z)
										z4=propiedadAntisimetrica(conjunto, z)
										z5=propiedadIrreflexiva(conjunto, z)
										print("Relacion 6: ", z1, z2, z3, z4, z5)
										
										lblrz = Label(ventanaResultados, text=str(z1), font=('Consolas', 10), bg="black", fg="white").grid(row=13,column=3)
										lblsz = Label(ventanaResultados, text=str(z2), font=('Consolas', 10), bg="black", fg="white").grid(row=13,column=5)
										lbltz = Label(ventanaResultados, text=str(z3), font=('Consolas', 10), bg="black", fg="white").grid(row=13,column=7)
										lblaz = Label(ventanaResultados, text=str(z4), font=('Consolas', 10), bg="black", fg="white").grid(row=13,column=9)
										lbliz = Label(ventanaResultados, text=str(z5), font=('Consolas', 10), bg="black", fg="white").grid(row=13,column=11)
										
									else:
										
										tkinter.messagebox.showinfo(title= "ALERTA!", message= "No se anadio ninguna pareja ordenada en la RELACION 6")
								else:
									listaComprobatoria.append(0)
									tkinter.messagebox.showinfo(title= "ERROR GRAVE!", message= "AlGUNO DE LOS PARES ORDENADOS DE LA REL. 6 NO PERTENECE AL CONJUNTO!")
		print("Lista comparatoria: ", listaComprobatoria)						
		
		if (0 not in listaComprobatoria and len(listaComprobatoria)!= 0):
			tkinter.messagebox.showinfo(title= "RELACIONES CARGADAS AL SISTEMA!", message= "Sus relaciones se cargaron con exito! \nRegrese al menu y seleccione @VerResultados")
	else:
		tkinter.messagebox.showinfo(title= "Anada elementos al conjunto!", message= "No hay elementos en el conjunto! \n Insertelos en @Insertar elementos del conjunto")
			
			
def cast(cadena):
	lista=[]
	lista2=[]
	lista3=[]	

	lista1=" ".join(cadena)
	lista1=lista1.replace(" ", ",")
		
	for i in range(0, len(lista1), 2):
		lista.append(int(lista1[i]))
		
		lista2=[[p] for p in lista]
		
	for j in range(0, len(lista2)//2):
		q=lista2[0]+lista2[1]
		lista2=lista2[2:]
		lista3.append(q)

	print("LISTAfin: ", lista3)

	return lista3
	


##########################################################--------------------VENTANA RELACIONES--------------------------------##########################################################

ventanaRelaciones.title("MENU RELACIONES")
ventanaRelaciones.attributes("-alpha", 0.91) #Esto sirve para transparentar ventanas
ventanaRelaciones.geometry("3600x2500+300+200")  ##Tamanio y la posicion donde va aparecer
ventanaRelaciones.config(bg='black')
ventanaRelaciones.maxsize(height=700, width=950)
#imFondo = PhotoImage(file= "max.png")
"""labelFondo = Label(ventanaRelaciones, image = imFondo).place(x=-55,y=-120)"""
encabezado1 = Label(ventanaRelaciones, text = "\t\t\tRELACIONES", font=('Consolas', 15), bg="black",  fg="yellow").grid(row=0,column=0)

lblInstrucciones1 = Label(ventanaRelaciones,text="Elija el numero de relaciones que desea analizar:  ", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=0)
rB1= Radiobutton(ventanaRelaciones, text = "1", value = 1, variable = radioButNumRelaciones, font=('Consolas', 9), bg="black", fg="yellow", command =lambda: generarSpinBox(radioButNumRelaciones.get(),ventanaRelaciones, 0,0)).place(x=28,y=55)
rB2= Radiobutton(ventanaRelaciones, text = "2", value = 2, variable = radioButNumRelaciones, font=('Consolas', 9), bg="black", fg="yellow", command =lambda: generarSpinBox(radioButNumRelaciones.get(),ventanaRelaciones, 0,0)).place(x=63,y=55)
rB3= Radiobutton(ventanaRelaciones, text = "3", value = 3, variable = radioButNumRelaciones, font=('Consolas', 9), bg="black", fg="yellow", command = lambda:generarSpinBox(radioButNumRelaciones.get(),ventanaRelaciones, 0,0)).place(x=98,y=55)
rB4= Radiobutton(ventanaRelaciones, text = "4", value = 4, variable = radioButNumRelaciones, font=('Consolas', 9), bg="black", fg="yellow", command = lambda:generarSpinBox(radioButNumRelaciones.get(),ventanaRelaciones, 0,0)).place(x=133,y=55)
rB5= Radiobutton(ventanaRelaciones, text = "5", value = 5, variable = radioButNumRelaciones, font=('Consolas', 9), bg="black", fg="yellow", command = lambda:generarSpinBox(radioButNumRelaciones.get(),ventanaRelaciones, 0,0)).place(x=168,y=55)
rB6= Radiobutton(ventanaRelaciones, text = "6", value = 6, variable = radioButNumRelaciones, font=('Consolas', 9), bg="black", fg="yellow", command = lambda:generarSpinBox(radioButNumRelaciones.get(),ventanaRelaciones, 0,0)).place(x=203,y=55)
lblInstrucciones2 = Label(ventanaRelaciones,text="Elija cuantos pares ordenados tendra cada relacion ", font=('Consolas', 10), bg="black", fg="white").place(x=3,y=85)
boton=Button(ventanaRelaciones, text="Concentrar datos", bg = "black", fg="white", command=lambda: getval()).place(x=30,y=180)


##########################################################--------------------VENTANA RESULTADOS--------------------------------##########################################################
ventanaResultados.title("RESULTADOS")
ventanaResultados.attributes("-alpha", 0.91) 
ventanaResultados.geometry("3600x2500+300+200") 
ventanaResultados.config(bg='black')
ventanaResultados.maxsize(height=275, width=620)
lbl11 = Label(ventanaResultados,text="   Reflexiva   ", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=3)
lbl12 = Label(ventanaResultados,text="Simetrica   ", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=5)
lbl13 = Label(ventanaResultados,text="Transitiva   ", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=7)
lbl14 = Label(ventanaResultados,text="Antisimetrica   ", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=9)
lbl15 = Label(ventanaResultados,text="Inflexiva", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=11)
lbl16 = Label(ventanaResultados,text="\n", font=('Consolas', 10), bg="black", fg="white").grid(row=1,column=12)
lbl1 = Label(ventanaResultados, text="R1\n ", font=('Consolas', 10), bg="black", fg="white").grid(row=3,column=0)
lbl2 = Label(ventanaResultados, text="R2\n ", font=('Consolas', 10), bg="black", fg="white").grid(row=5,column=0)
lbl3 = Label(ventanaResultados, text="R3\n ", font=('Consolas', 10), bg="black", fg="white").grid(row=7,column=0)
lbl4 = Label(ventanaResultados, text="R4\n ", font=('Consolas', 10), bg="black", fg="white").grid(row=9,column=0)
lbl5 = Label(ventanaResultados, text="R5\n ", font=('Consolas', 10), bg="black", fg="white").grid(row=11,column=0)
lbl6 = Label(ventanaResultados, text="R6\n ", font=('Consolas', 10), bg="black", fg="white").grid(row=13,column=0)
encRes = Label(ventanaResultados, text = "\t\t\tTABLA DE RESULTADOS :)", font=('Consolas', 13), bg="black",  fg="yellow").place(x=0,y=245)


                                        



 


ventanaPrincipal.mainloop() #proceso principal hacia la ventana
