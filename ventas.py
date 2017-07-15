#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tkinter
import psycopg2
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
import tkinter as tk
from tkinter import messagebox
import locale


locale.setlocale(locale.LC_ALL, '')



#variable conexion
cadenaconexion="host='localhost' dbname='tienda' user='postgres' password='utp'"
#imprimir cadena conexion
#print ("MUY BIEN")#("cadena conexion al bd\n ->%s"%(cadenaconexion))
obj=psycopg2.connect(cadenaconexion)
objCursor=obj.cursor()
obj.commit()


#clase para mostrar los elementos que se consultan
class Consulta(tkinter.Frame):
    '''
    classdocs
    '''  
    def __init__(self, parent):
        '''
        Constructor
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.grid_rowconfigure(10,weight=200)
        self.parent.grid_columnconfigure(10,weight=200)
       
		
        # Define the different GUI widgets
       
        
        self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.insertarDatos)
        self.submit_button.grid(row = 2, column = 1, sticky = tkinter.W)
        #self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.parent.quit)
        #self.exit_button.grid(row = 0, column = 3)
        #self.botonDevuelta = tkinter.Button(self.parent, text = "Cambio", command = self.multi)
        #self.botonDevuelta.grid(row = 4, column = 3, sticky = tkinter.W)
        botonDevuelta = Button(pestaña1, text = "Cambio", command = self.calcularDevuelta)
        botonDevuelta.grid(row = 4, column = 3, sticky = tkinter.W) 
        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('Descripción', 'Cantidad','Valor unitario','Valor total'))
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Descripción')
        self.tree.heading('#2', text='Cantidad')
        self.tree.heading('#3', text='Valor unitario')
        self.tree.heading('#4', text='Valor total')
        self.tree.column('#1', stretch=tkinter.YES,width=250)
        self.tree.column('#2', stretch=tkinter.YES,width=100)
        self.tree.column('#3', stretch=tkinter.YES,width=100)
        self.tree.column('#4', stretch=tkinter.YES,width=100)
        self.tree.column('#0', stretch=tkinter.YES,width=40)
        self.tree.grid(row=10,rowspan=15,column=11, columnspan=13, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 1

     
    def calcularDevuelta(*args):
    	res = devuelta
    	cli = totalSuma
    	igual = devuelta.get()-totalSuma
    	mostrarCambio.insert(INSERT,igual)
    	mostrarCambio.configure(state=DISABLED)	    
    

    def insertarDatos(self):
        global totalSuma
        global mostrarCambio
        global devuelta
        devuelta = IntVar()
        lblConsultar = objCursor.execute("SELECT * FROM productos")
        rows = objCursor.fetchall()
        devueltaCliente = 0
        mostrarTotal = Text(pestaña1,width=10, height=1.5)
        mostrarCambio = Text(pestaña1,width=10, height=1.5)
        mostrarTotal.configure(state=NORMAL)
        dineroCliente = Entry(pestaña1,textvariable=devuelta,width=10).place(x=10,y=290)
       	for row in rows:
       		if entradaCodigo.get() == row[0] and len(entradaCodigo.get())!=0: #analiza si entradaCodigo esta vacia
       			multiplicarCantidad = row[4]*entradaCantidad.get()
       			
       			mostrarTotal.place(x=10,y=190)
       			mostrarCambio.place(x=10,y=415)
       			sumaTotal.append(multiplicarCantidad)
       			totalSuma=0
       			for i in sumaTotal:
       				totalSuma+=i
       			mostrarTotal.insert(INSERT,totalSuma)
       			
       			devueltaCliente = devuelta.get()-totalSuma
       			#mostrarCambio.insert(INSERT,devueltaCliente)
       			mostrarTotal.configure(state=DISABLED)
	       			#print(totalSuma)
       			
       			cantidadProductos = Entry(pestaña1,textvariable=entradaCantidad, width=35)
       			self.treeview.insert('', 'end',text=str(self.i),values=(str(row[1]),str(entradaCantidad.get()), str(row[4]),str(multiplicarCantidad)))
       			
       			#resultado.insert(4,multiplicarCantidad)
       			self.i = self.i + 1
       			entradaCodigo.set("")
       			entradaCantidad.set(value=1)
		        # Increment counter

	


    	
       
		        
				


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	
def mensaje():
	messagebox.showinfo("Mensaje", "Los datos fueron guardados satisfactoriamente")
	#messagebox.showwarnin("Mensaje", "Los datos fueron guardados satisfactoriamente")
	#messagebox.askquestion("pregunta 1", "Los datos fueron guardados satisfactoriamente")
	#messagebox.askokcancel("pregunta 1", "Los datos fueron guardados satisfactoriamente")
	#messagebox.askretrycancel("pregunta 1", "Los datos fueron guardados satisfactoriamente")



def guardar2():
	
	dato1 = entradaCodigo2.get()
	dato2 = entradaNombre2.get()
	dato3 = entradaCantidad2.get()
	dato4 = entradaPrecioM2.get()
	dato5 = entradaPrecioV2.get()
	lblGrabar2 = objCursor.execute("INSERT INTO productos values('%s','%s','%i','%i',%i)" % (dato1,dato2,dato3,dato4,dato5) ) 
	
	obj.commit()#Label(ventana,text='hola'+entrada.get(),font=("Arial",10)).place(x=456,y=559)	
	messagebox.showinfo("Guardado","Los datos fueron guardados satisfactoriamente")
	entradaCodigo2.set("")
	entradaNombre2.set("")
	entradaCantidad2.set("")
	entradaPrecioM2.set("")
	entradaPrecioV2.set("")




#pestaña inventario
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def pestaInventario():
	global entradaCodigo2
	global entradaNombre2
	global entradaCantidad2
	global entradaPrecioM2
	global entradaPrecioV2
	entradaCodigo2 = StringVar()
	entradaNombre2 = StringVar()
	entradaCantidad2 = IntVar()
	entradaPrecioM2 = IntVar()
	entradaPrecioV2 = IntVar()
	pestaña2 = ttk.Frame(notebook,style='My.TFrame')
	notebook.add(pestaña2,text='Inventario')
	btnGrabar2 = Button(pestaña2,text="Grabar",command=guardar2,font=("Arial",12)).place(x=15,y=5)

	codProducto = Label(pestaña2,text = "Código producto",font=("Arial",12)).place(x=15,y=60)
	Cod = Entry(pestaña2,textvariable=entradaCodigo2, width=25).place(x=15,y=85)

	
	nombreProducto = Label(pestaña2,text = "Nombre producto",font=("Arial",12)).place(x=200,y=60)
	nombre = Entry(pestaña2,textvariable=entradaNombre2, width=35).place(x=200,y=85)

	cantidadProducto = Label(pestaña2,text = "Cantidad",font=("Arial",12)).place(x=445,y=60)
	cantidad = Entry(pestaña2,textvariable=entradaCantidad2, width=7).place(x=450,y=85)

	precioPorMayor = Label(pestaña2,text = "Precio por mayor",font=("Arial",12)).place(x=550,y=60)
	precioMayor = Entry(pestaña2,textvariable=entradaPrecioM2, width=10).place(x=560,y=85)

	precioVenta = Label(pestaña2,text = "Precio venta",font=("Arial",12)).place(x=700,y=60)
	precioVen = Entry(pestaña2,textvariable=entradaPrecioV2, width=10).place(x=710,y=85)
	#pestaña2.mainloop()




#pestaña ventas
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def pestaVentas():
	global pestaña1
	global entradaCodigo
	global entradaNombre
	global entradaCantidad
	global entradaPrecioM
	global entradaPrecioV
	entradaCodigo = StringVar()
	entradaNombre = StringVar()
	entradaCantidad = IntVar(value=1)
	entradaPrecioM = IntVar()
	entradaPrecioV = IntVar()



	pestaña1 = ttk.Frame(notebook, style='My.TFrame')
	notebook.add(pestaña1,text='Venta')
	btnGrabar2 = Button(pestaña1,text="Grabar",command=guardar2,font=("Arial",12)).place(x=15,y=5)

	
	#botones inventario y venta
	#btnBuscar = tk.Button(pestaña1,text="Inventario",command=abrir,font=("Arial",12)).place(x=95,y=5)#para ubicar el boton.grid(row=0,column=1)
	#btnBuscar = Button(pestaña1,text="Vender", fg="blue",command=guardar,font=("Arial",12)).place(x=15,y=5)#.
	#Buscar = Button(pestaña1,text="consulta", fg="blue",command=consultar,font=("Arial",12)).place(x=120,y=5)#.

	codigoProducto = Label(pestaña1,text = "Código producto",fg=colorLetra,bg=colorFondo,font=("Arial",12)).place(x=10,y=60)
	Codigo = Entry(pestaña1,textvariable=entradaCodigo, width=25).place(x=15,y=85)
	cantidadProducto = Label(pestaña1,text = "Cantidad",font=("Arial",12)).place(x=200,y=60)
	cantidad = Entry(pestaña1,textvariable=entradaCantidad, width=10).place(x=205,y=85)
	#codigoVenta = Entry(pestaña1,textvariable=entradaCantidad, width=10).place(x=950,y=85)


	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	#campos de informacion total y cambio

	
	total = Label(pestaña1,text = "TOTAL",font=("Arial",12)).place(x=10,y=160)
	
	#nombre = Entry(pestaña1,textvariable=entradaNombre, width=35).place(x=900,y=85)
	dineroEntregado = Label(pestaña1,text = "DINERO ENTREGADO",font=("Arial",12)).place(x=15,y=260)

	dineroEntregado = Label(pestaña1,text = "CAMBIO",font=("Arial",12)).place(x=15,y=385)


	
#ventana principal    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


ventana = tk.Tk()

colorFondo = "#009"
colorLetra = "#FFF"
estilo = Style()

estilo.configure('My.TFrame',background=colorFondo, foreground=colorLetra)
#pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

pestaVentas()
pestaInventario()
#consultar()
#cons()

ventana.geometry("1200x600+100+70")
ventana.title("FACTURACION")

sumaTotal=[]


d=Consulta(pestaña1)

ventana.mainloop()
