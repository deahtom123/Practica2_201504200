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

lista=ListaSimple()
cola =Cola()
pila=Pila()

@app.route('/metodoWeb',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	return "Hola " + str(parametro) + "!"+str(dato2)

@app.route('/insertarLista',methods=['POST']) 
def helloa():
	parametro = str(request.form['dato'])
	lista.insertar(parametro)
	return ""

@app.route('/buscarLista',methods=['POST']) 
def hellob():
	parametro = str(request.form['dato'])
	return str(lista.buscar(parametro))

@app.route('/eliminarLista',methods=['POST']) 
def helloc():
	parametro = int(request.form['dato'])
	lista.eliminar(parametro)
	return ""

@app.route('/agregarCola',methods=['POST']) 
def hellod():
	parametro = str(request.form['dato'])	
	cola.add(parametro)
	return ""

@app.route('/sacarCola',methods=['POST']) 
def helloe():
	parametro = str(request.form['dato'])
	return cola.sacar()

@app.route('/agregarPila',methods=['POST']) 
def hellog():
	parametro = str(request.form['dato'])	
	pila.push(parametro)
	return ""

@app.route('/sacarPila',methods=['POST']) 
def helloh():
	parametro = str(request.form['dato'])
	return pila.pop()

@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
  
  
