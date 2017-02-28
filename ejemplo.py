__author__ = "Mac"


from flask import Flask, request, Response
app = Flask("EDD_codigo_ejemplo")

class ListaSimple:
	 def __init__(self):
	 	self.cabeza=None

	 def insertar(self, palabra):
		 nuevo= Nodo(palabra)
		 if self.cabeza is None:
		 	self.setCabeza(nuevo)
		 else:
		 	auxiliar=self.getCabeza()
		 	while(auxiliar.getSiguiente()!=None):
		 		auxiliar=auxiliar.getSiguiente()
		 	auxiliar.setSiguiente(nuevo)

	 def imprimir(self):
		auxiliar=self.getCabeza()
		while auxiliar:
			print(str(auxiliar.getPalabra()))
			auxiliar=auxiliar.getSiguiente()
	 def eliminar(self, indice):
	 	auxiliar=self.getCabeza()
	 	if indice==0:
	 		self.setCabeza(auxiliar.getSiguiente())
	 	else:
	 		for i in range(indice-1):
	 			auxiliar=auxiliar.getSiguiente()
	 		auxiliar.setSiguiente(auxiliar.getSiguiente().getSiguiente())
	 def buscar(self, palabra):
	 	auxiliar=self.getCabeza()
	 	i=0
	 	while auxiliar:
	 		if auxiliar.getPalabra()==palabra:
	 			return str("EL DATO SE ENCUENTRA EN EL INDICE "+str(i))
	 		auxiliar=auxiliar.getSiguiente()
	 		i=i+1
	 	return str("NO SE ENCONTRO EL DATO")
	 		

	 def setCabeza(self, cabeza):
	 	self.cabeza=cabeza
	 def getCabeza(self):
	 	return self.cabeza
class Nodo:
	 def __init__(self,palabra):
		self.palabra=palabra
		self.siguiente=None
	 def getSiguiente(self):
		return self.siguiente
	 def setSiguiente(self,siguiente):
		self.siguiente=siguiente
	 def getPalabra(self):
		return str(self.palabra)
	 def setPalabra(self,palabra):
		self.palabra=str(palabra)

class NodoCola:
	def __init__(self):
		self.palabra=None
		self.siguiente=None
class Cola:
	def __init__(self):
		self.cabeza=None
		self.fondo=None
	def add(self, palabra):
		actual=NodoCola()
		actual.palabra=palabra
		if self.colavacia()==True:
			self.cabeza=actual
			self.fondo=actual
		else:
			self.fondo.siguiente=actual
			self.fondo=actual
	def sacar(self):
		if self.colavacia()==False:
			palabra=self.cabeza.palabra
			if self.cabeza==self.fondo:
				self.cabeza=None
				self.fondo=None
			else:
				self.cabeza=self.cabeza.siguiente
			return palabra
		else:
			return ""

	def mostrar(self):			
		reco=self.cabeza
		print("Listado de los elementos")
		while reco:
			print str(reco.palabra)+"-",
			reco=reco.siguiente

	def colavacia(self):
		if self.cabeza==None:
			return True
		else:
			return False
class NodoPila:
	def __init__(self):
		self.info=None
		self.siguiente=None
class Pila:
	def __init__(self):
		self.cabeza=None
	def push(self, dato):
		nuevo=NodoPila()
		nuevo.info=dato
		if self.cabeza==None:
			nuevo.siguiente=None
			self.cabeza=nuevo
		else:
			nuevo.siguiente=self.cabeza
			self.cabeza=nuevo
	def pop(self):
		if self.cabeza!=None:
			informacion=self.cabeza.info
			self.cabeza=self.cabeza.siguiente
			return informacion
		else:
			return " "
	def imprimir(self):
		reco=self.cabeza
		print("LISSTADO DE TODOS LOS ELEMENTOS DE LA PILA")
		while reco:
			print str(reco.info)+"-",
			reco=reco.siguiente		
class NodoDisperso:
	def __init__(self, info):
		self.info=info
		self.derecha=None
		self.izquierda=None
		self.arriba=None
		self.abajo=None
		self.profundidabajo=None
		self.profundidadarriba=None
	def getInfo(self):
		return str(self.info)
	def setInfo(self, info):
		self.info=str(info)
	def getDerecha(self):
		return self.derecha
	def setDerecha(self, derecha):
		self.derecha=derecha
	def getIzquierda(self):
		return self.izquierda
	def setIzquierda(self, izquierda):
		self.izquierda=izquierda
	def getArriba(self):
		return self.arriba
	def setArriba(self, arriba):
		self.arriba=arriba
	def getAbajo(self):
		return self.abajo
	def setAbajo(self, abajo):
		self.abajo=abajo
	def getProfundidabajo(self):
		return self.profundidabajo
	def setProfundidabajo(self, profundidabajo):
		self.profundidabajo=profundidabajo
	def getProfundidadarriba(self):
		return self.profundidadarriba
	def setProfundidadarriba(self, profundidadarriba):
		self.profundidadarriba=profundidadarriba

class MatrizDispersa:
	def __init__(self):
		nuevo=NodoDisperso("Cabeza")
		self.cabeza=nuevo
	def filas(self, auxiliar, letra):
		while auxiliar:
			if auxiliar.getAbajo()!=None:
				if auxiliar.getAbajo().getInfo()>letra:
					return auxiliar
				else:
					auxiliar=auxiliar.getAbajo()
			else:
				return auxiliar
	def columnas(self, auxiliar, letra):
		while auxiliar:
			if auxiliar.getDerecha()!=None:
				if auxiliar.getDerecha().getInfo()>letra:
					return auxiliar
				else:
					auxiliar=auxiliar.getDerecha()
			else:
				return auxiliar
	def compararfila(self, letra):
		auxiliar=self.cabeza.getAbajo()
		while auxiliar:
			if auxiliar.getInfo()==letra:
				return True
			auxiliar=auxiliar.getAbajo()
		return False
	def compararcolumna(self, letra):
		auxiliar=self.cabeza.getDerecha()
		while auxiliar:
			if auxiliar.getInfo()==letra:
				return True
			auxiliar=auxiliar.getDerecha()
		return False
	def imprimir(self):
		auxiliar=self.cabeza
		while auxiliar:
			print str(auxiliar.getInfo()+" "),
			auxiliar=auxiliar.getDerecha()
		print "\n"
		auxiliar=self.cabeza.getAbajo()
		while auxiliar:
			print str(auxiliar.getInfo()+" ") 
			auxiliar=auxiliar.getAbajo()
	def buscarletra(self, letra):
		respuesta=""
		auxiliar=self.cabeza.getAbajo()
		fila=None
		while auxiliar:
			if auxiliar.getInfo()==letra:
				fila=auxiliar
				auxiliar=None
			else:
				auxiliar=auxiliar.getAbajo()
		while fila:
			respuesta=respuesta+fila.getInfo()+"-"
			if fila.getProfundidabajo()!=None:
				auxiliar2=fila.getProfundidabajo()
				while auxiliar2!=None:
					respuesta=respuesta+auxiliar2.getInfo()+"-"
					auxiliar2=auxiliar2.getProfundidabajo()
			fila=fila.getDerecha()
		return respuesta
	def buscarCorreo(self, correo):
		respuesta=""
		auxiliar=self.cabeza.getDerecha()
		columna=None
		while auxiliar:
			if auxiliar.getInfo()==correo:
				columna=auxiliar
				auxiliar=None
			else:
				auxiliar=auxiliar.getDerecha()
		while columna:
			respuesta=respuesta+columna.getInfo()+"-"
			if columna.getProfundidabajo()!=None:
				auxiliar2=columna.getProfundidabajo()
				while auxiliar2!=None:
					respuesta=respuesta+auxiliar2.getInfo()+"-"
					auxiliar2=auxiliar2.getProfundidabajo()
			columna=columna.getAbajo()
		return respuesta
		
	def insertar(self, dato, dato2):
		letra=str(dato[0])
		fila=self.cabeza
		columna=self.cabeza
		nuevo=NodoDisperso(dato)
		if self.cabeza.getDerecha()==None:
			fila=NodoDisperso(letra)
			columna=NodoDisperso(dato2)
			self.cabeza.setDerecha(columna)
			columna.setIzquierda(self.cabeza)
			self.cabeza.setAbajo(fila)
			fila.setArriba(self.cabeza)
			nuevo.setIzquierda(fila)
			fila.setDerecha(nuevo)
			nuevo.setArriba(columna)
			columna.setAbajo(nuevo)
		else:
			existefila=self.compararfila(letra)
			existecolumna=self.compararcolumna(dato2)
			if existecolumna==False and existefila==False:
				auxiliar=self.cabeza
				#PARA VER EN QUE FILA DEBE DE IR
				fila=self.filas(auxiliar,letra)
				#PARA VER EN QUE COLUMNA DEBE DE IR
				columna=self.columnas(auxiliar,dato2)
				#SE CREAN LOS ENCABEZADOS DE LA FILA Y COLUMNA
				auxiliarfila=NodoDisperso(letra)
				auxiliarcolumna=NodoDisperso(dato2)
				#ENLACES DE LAS FILAS
				if fila.getAbajo()!=None:
					auxiliarfila.setAbajo(fila.getAbajo())
					fila.getAbajo().setArriba(auxiliarfila)
				fila.setAbajo(auxiliarfila)
				auxiliarfila.setArriba(fila)
				#ENLACES DE LAS COLUMNAS
				if columna.getDerecha()!=None:
					auxiliarcolumna.setDerecha(columna.getDerecha())
					columna.getDerecha().setIzquierda(auxiliarcolumna)
				columna.setDerecha(auxiliarcolumna)
				auxiliarcolumna.setIzquierda(columna)
				#ENLACES AL NODO NUEVO
				auxiliarfila.setDerecha(nuevo)
				nuevo.setIzquierda(auxiliarfila)
				auxiliarcolumna.setAbajo(nuevo)
				nuevo.setArriba(auxiliarcolumna)
			if existefila==True and existecolumna==False:
				columna=self.columnas(self.cabeza,dato2)
				#METEMOS EL INDICE DE LA COLUMNA
				auxiliarcolumna=NodoDisperso(dato2)
				auxiliarcolumna.setDerecha(columna.getDerecha())
				if columna.getDerecha()!=None:
					columna.getDerecha().setIzquierda(auxiliarcolumna)
				auxiliarcolumna.setIzquierda(columna)
				columna.setDerecha(auxiliarcolumna)
				#METEMOS EL DATO EN LA MATRIZ
				auxiliar=self.cabeza.getAbajo()
				while not(auxiliar.getInfo()==letra):
					auxiliar=auxiliar.getAbajo()
				
				fila=auxiliar
				prueba=auxiliar
				while prueba.getDerecha()!=None:
					prueba=prueba.getDerecha()
					auxiliar2=prueba
					while auxiliar2.getArriba()!=None:
						auxiliar2=auxiliar2.getArriba()
					if auxiliar2.getInfo()<dato2:
						fila=prueba
					auxiliar=auxiliar.getDerecha()
				
				nuevo.setArriba(auxiliarcolumna)
				auxiliarcolumna.setAbajo(nuevo)
				nuevo.setDerecha(fila.getDerecha())
				if fila.getDerecha()!=None:
					fila.getDerecha().setIzquierda(nuevo)
				fila.setDerecha(nuevo)
				nuevo.setIzquierda(fila)
			if existefila==False and existecolumna==True:
				fila=self.filas(self.cabeza,letra)
				#METEMOS EL NUEVO INDICE DE LA FIAL
				auxiliarfila=NodoDisperso(letra)
				auxiliarfila.setAbajo(fila.getAbajo())
				if fila.getAbajo()!=None:
					fila.getAbajo().setArriba(auxiliarfila)
				fila.setAbajo(auxiliarfila)
				auxiliarfila.setArriba(fila)
				#METEMOS EL DATO EN LA MATRIZ
				auxiliar=self.cabeza.getDerecha()
				while not(auxiliar.getInfo()==dato2):
					auxiliar=auxiliar.getDerecha()
				columna=self.filas(auxiliar,letra)
				nuevo.setAbajo(columna.getAbajo())
				if columna.getAbajo()!=None:
					columna.getAbajo().setArriba(nuevo)
				columna.setAbajo(nuevo)
				nuevo.setArriba(columna)
				nuevo.setIzquierda(auxiliarfila)
				auxiliarfila.setDerecha(nuevo)
			if existefila==True and existecolumna==True:
				auxiliar=self.cabeza.getDerecha()
				while not(auxiliar.getInfo()==dato2):
					auxiliar=auxiliar.getDerecha()
				columna=self.filas(auxiliar,letra)
				if columna.getAbajo()!=None:
						#fdsafasfasfsadfasfasf
					if columna.getAbajo().getInfo()[0]==letra[0]:
						actual=columna.getAbajo()
						while actual.getProfundidabajo():
							actual=actual.getProfundidabajo()
						actual.setProfundidabajo(nuevo)
						nuevo.setProfundidadarriba(actual)
				else:
					auxiliar=self.cabeza.getAbajo()
					while not(auxiliar.getInfo()==letra):
						auxiliar=auxiliar.getAbajo()
					prueba=auxiliar
					fila=auxiliar
					while prueba.getDerecha():
						prueba=prueba.getDerecha()
						auxiliar2=prueba
						while auxiliar2.getArriba():
							auxiliar2=auxiliar2.getArriba()
						if auxiliar2.getInfo()<dato2:
							fila=prueba
						auxiliar=auxiliar.getDerecha()
					nuevo.setDerecha(fila.getDerecha())
					if fila.getDerecha()!=None:
						fila.getDerecha().setIzquierda(nuevo)
					fila.setDerecha(nuevo)
					nuevo.setIzquierda(fila)
					nuevo.setAbajo(columna.getAbajo())
					if columna.getAbajo()!=None:
						columna.getAbajo.setArriba(nuevo)
					nuevo.setArriba(columna)
					columna.setAbajo(nuevo)
	def buscarNodo(self, correo):
		letra=str(correo[0])
		auxiliar=self.cabeza.getAbajo()
		fila=None
		while auxiliar:
			if auxiliar.getInfo()==letra:
				fila=auxiliar
				auxiliar=None
			else:
				auxiliar=auxiliar.getAbajo()
		while fila:
			if fila.getInfo()==correo:
				return fila
			if fila.getProfundidabajo()!=None:
				auxiliar=fila.getProfundidabajo()
				while auxiliar:
					if auxiliar.getInfo()==correo:
						return auxiliar
					auxiliar=auxiliar.getProfundidabajo()
			fila=fila.getDerecha()
		print("NO envia nada")
		return None
	def eliminar(self, correo):
		auxiliar=self.buscarNodo(correo)
		if auxiliar.getAbajo()==None and auxiliar.getDerecha()==None and (auxiliar.getProfundidadarriba()==None and auxiliar.getProfundidabajo()==None):
			if auxiliar.getArriba().getArriba()==None and auxiliar.getIzquierda().getIzquierda()==None:
				arriba=auxiliar.getArriba()
				arriba.getIzquierda().setDerecha(arriba.getDerecha())
				if arriba.getDerecha()!=None:
					arriba.getDerecha().setIzquierda(arriba.getIzquierda())
				izquierda=auxiliar.getIzquierda()
				izquierda.getArriba().setAbajo(izquierda.getAbajo())
				if izquierda.getAbajo()!=None:
					izquierda.getAbajo().setArriba(izquierda.getArriba())
			else:
				auxiliar.getArriba().setAbajo(None)
				auxiliar.getIzquierda().setDerecha(None)
				if auxiliar.getIzquierda().getIzquierda()==None and auxiliar.getDerecha()==None:
					actual=auxiliar.getIzquierda()
					actual.getArriba().setAbajo(actual.getAbajo())
					if actual.getAbajo()!=None:
						actual.getAbajo().setArriba(actual.getArriba())
				if auxiliar.getArriba().getArriba()==None and auxiliar.getAbajo()==None:
					actual=auxiliar.getArriba()
					actual.getIzquierda().setDerecha(actual.getDerecha())
					if actual.getDerecha()!=None:
						actual.getDerecha().setIzquierda(actual.getIzquierda())
		else:
			if auxiliar.getProfundidadarriba()!=None:
				auxiliar.getProfundidadarriba().setProfundidabajo(auxiliar.getProfundidabajo())
				if auxiliar.getProfundidabajo()!=None:
					auxiliar.getProfundidabajo().setProfundidadarriba(auxiliar.getProfundidadarriba())
				else:
					auxiliar.getProfundidadarriba().setProfundidabajo(None)
			elif auxiliar.getProfundidabajo()!=None and auxiliar.getProfundidadarriba()==None:
				abajo=auxiliar.getProfundidabajo()
				if auxiliar.getAbajo()!=None:
					auxiliar.getAbajo().setArriba(abajo)
				if auxiliar.getDerecha()!=None:
					auxiliar.getDerecha().setIzquierda(abajo)
				auxiliar.getIzquierda().setDerecha(abajo)
				auxiliar.getArriba().setAbajo(abajo)
				abajo.setIzquierda(auxiliar.getIzquierda())
				abajo.setArriba(auxiliar.getArriba())
				abajo.setAbajo(auxiliar.getAbajo())
				abajo.setDerecha(auxiliar.getDerecha())
				abajo.setProfundidadarriba(None)
			elif auxiliar.getDerecha()!=None:
				auxiliar.getIzquierda().setDerecha(auxiliar.getDerecha())
				auxiliar.getDerecha().setIzquierda(auxiliar.getIzquierda())
				auxiliar.getArriba().setAbajo(auxiliar.getAbajo())
				if auxiliar.getAbajo()!=None:
					auxiliar.getAbajo().setArriba(auxiliar.getArriba())
				if auxiliar.getArriba().getArriba()==None and auxiliar.getAbajo()==None:
					actual=auxiliar.getArriba()
					actual.getIzquierda().setDerecha(actual.getDerecha())
					if actual.getDerecha()!=None:
						actual.getDerecha().setIzquierda(actual.getIzquierda())
			elif auxiliar.getAbajo()!=None:
				auxiliar.getArriba().setAbajo(auxiliar.getAbajo())
				auxiliar.getAbajo().setArriba(auxiliar.getArriba())
				auxiliar.getIzquierda().setDerecha(auxiliar.getDerecha())
				if auxiliar.getDerecha()!=None:
					auxiliar.getDerecha().setIzquierda(auxiliar.getIzquierda())
				if auxiliar.getIzquierda().getIzquierda()==None and auxiliar.getDerecha()==None:
					actual=auxiliar.getIzquierda()
					actual.getArriba().setAbajo(actual.getAbajo())
					if actual.getAbajo()!=None:
						actual.getAbajo().setArriba(actual.getArriba())

def creartxtlista():
	 archi=open('lista.txt','w')
	 archi.close
	 crearlista()	

def crearlista():
    archi=open('lista.txt','a')
    archi.write("digraph G {")
    auxiliar=lista.getCabeza()
    i=0
    while auxiliar:
    	archi.write("A"+str(i)+"[label="+auxiliar.getPalabra()+"] ")
    	auxiliar=auxiliar.getSiguiente()
    	i=i+1	
    for j in range(i-1):
    	archi.write("A"+str(j)+"->A"+str(j+1)+" ");
    archi.write("}")
    archi.close()
    ejecutar("lista")
def creartxtcola():
	 archi=open('cola.txt','w')
	 archi.close
	 crearcola()
def crearcola():
    archi=open('cola.txt','a')
    archi.write("digraph G {")
    auxiliar=cola.cabeza
    i=0
    while auxiliar:
    	archi.write("A"+str(i)+"[label="+auxiliar.palabra+"] ")
    	auxiliar=auxiliar.siguiente
    	i=i+1	
    for j in range(i-1):
    	archi.write("A"+str(j)+"->A"+str(j+1)+" ");
    archi.write("}")
    archi.close()
    ejecutar("cola")	
def creartxtpila():
	 archi=open('pila.txt','w')
	 archi.close
	 crearpila()
def crearpila():
    archi=open('pila.txt','a')
    archi.write("digraph G {")
    auxiliar=pila.cabeza
    i=0
    while auxiliar:
    	archi.write("A"+str(i)+"[label="+auxiliar.info+"] ")
    	auxiliar=auxiliar.siguiente
    	i=i+1	
    for j in range(i-1):
    	archi.write("A"+str(j)+"->A"+str(j+1)+" ");
    archi.write("}")
    archi.close()
    ejecutar("pila")
def creartxtmatriz():
	 archi=open('matriz.txt','w')
	 archi.close
	 crearmatriz()
def crearmatriz():
    archi=open('matriz.txt','a')
    archi.write("digraph G {")
    auxiliar=matriz.cabeza
    print(auxiliar.getInfo())
    auxiliar2=auxiliar
    while auxiliar2:
    	auxiliar=auxiliar2
    	while auxiliar:
    		if auxiliar.getDerecha()!=None:
    			archi.write('"'+auxiliar.getInfo()+'"->"'+auxiliar.getDerecha().getInfo()+'" ')
    		if auxiliar.getIzquierda()!=None:
    			archi.write('"'+auxiliar.getInfo()+'"->"'+auxiliar.getIzquierda().getInfo()+'" ')
    		if auxiliar.getArriba()!=None:
    			archi.write('"'+auxiliar.getInfo()+'"->"'+auxiliar.getArriba().getInfo()+'" ')
    		if auxiliar.getAbajo()!=None:
    			archi.write('"'+auxiliar.getInfo()+'"->"'+auxiliar.getAbajo().getInfo()+'" ')
    		if auxiliar.getProfundidabajo()!=None:
    			auxiliar3=auxiliar
    			while auxiliar3.getProfundidabajo():
    				archi.write('"'+auxiliar3.getInfo()+'"->"'+auxiliar3.getProfundidabajo().getInfo()+'" ')
    				archi.write('"'+auxiliar3.getProfundidabajo().getInfo()+'"->"'+auxiliar3.getInfo()+'" ')
    				auxiliar3=auxiliar3.getProfundidabajo()
    				
    		auxiliar=auxiliar.getDerecha()
    	auxiliar2=auxiliar2.getAbajo()
    archi.write("}")
    archi.close()
    ejecutar("matriz")	
def ejecutar(nombre):
	import os
	dotPath = "C:\\Graphviz2.30\\bin\\dot.exe"
	fileInputPath = "C:\\Estructuras\\"+nombre+".txt"
	fileOutputPath = "C:\\Estructuras\\"+nombre+".jpg"
	tParam = " -Tjpg "
	tOParam = " -o "
	tuple = (dotPath +tParam+ fileInputPath+tOParam+fileOutputPath)
	os.system(tuple)



lista=ListaSimple()
cola =Cola()
pila=Pila()
matriz=MatrizDispersa()

@app.route('/metodoWeb',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	return "Hola " + str(parametro) + "!"+str(dato2)

@app.route('/insertarLista',methods=['POST']) 
def helloa():
	parametro = str(request.form['dato'])
	lista.insertar(parametro)
	creartxtlista()
	return "AGREGADO"

@app.route('/buscarLista',methods=['POST']) 
def hellob():
	parametro = str(request.form['dato'])
	return str(lista.buscar(parametro))

@app.route('/eliminarLista',methods=['POST']) 
def helloc():
	parametro = int(request.form['dato'])
	lista.eliminar(parametro)
	creartxtlista()
	return "ELIMINADO"

@app.route('/agregarCola',methods=['POST']) 
def hellod():
	parametro = str(request.form['dato'])	
	cola.add(parametro)
	creartxtcola()
	return "AGREGADO"

@app.route('/sacarCola',methods=['POST']) 
def helloe():
	parametro = str(request.form['dato'])
	resultado=str(cola.sacar())
	creartxtcola()
	return resultado

@app.route('/agregarPila',methods=['POST']) 
def hellog():
	parametro = str(request.form['dato'])	
	pila.push(parametro)
	creartxtpila()
	return "AGREGADO"

@app.route('/sacarPila',methods=['POST']) 
def helloh():
	parametro = str(request.form['dato'])
	resultado=pila.pop()
	creartxtpila()
	return resultado

@app.route('/agregarMatriz',methods=['POST']) 
def helloi():
	parametro = str(request.form['dato'])
	parametro2=str(request.form['dato2'])
	matriz.insertar(parametro,parametro2)
	creartxtmatriz()
	return "AGREGADO"

@app.route('/eliminarMatriz',methods=['POST']) 
def helloj():
	parametro = str(request.form['dato'])
	matriz.eliminar(parametro)
	creartxtmatriz()
	return "FUE ELIMINADO"

@app.route('/letraMatriz',methods=['POST']) 
def hellok():
	parametro = str(request.form['dato'])
	return matriz.buscarletra(parametro)
@app.route('/dominioMatriz',methods=['POST']) 
def hellol():
	parametro = str(request.form['dato'])
	return matriz.buscarCorreo(parametro)

@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
  
  
