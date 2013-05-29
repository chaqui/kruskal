from Posicion import  Posicion

class Kruskal(object):
	"""docstring for Algoritmo"""
	"""Algoritmo de Dikstra desarrollado en python"""
	#constructor de la clase
	def __init__(self, vector,c ):
		#c es el numero de elementos que contiene el vector
		self.a=c
		#vector contiene todos los elementos de la tabla de aristas
		self.vectorEntrada= vector
		#se crea el vector de salida
		self.vectorSalida=[]
		#se llama a la funcion rellenar para colocar puros 0s en el verctor de salida
		self.rellenar(c)

	def solucionar(self):
		print"iniciar"
		i=0
		for x in xrange(0,self.a):
			self.vectorEntrada[x][x]=0
		#hacer la busqueda mientras no tiene la cantidad de aristas necesarias
		while (i<self.a-1):
			b=self.menor()
			if b!=None:
				#se  envia la informacuon 
				self.t=self.buscar(b.y)
				if self.t!=False:
					self.vectorSalida[b.x][b.y]=self.vectorEntrada[b.x][b.y]
					self.vectorSalida[b.y][b.x]=self.vectorEntrada[b.x][b.y]
					i=i+1
				self.vectorEntrada[b.x][b.y]=0
				self.vectorEntrada[b.y][b.x]=0
						

	def rellenar(self,b):
		self.aux=[]	
		#funcion para rellenar 0s
		for x in xrange(0,b):
			self.aux=[]
			for y in xrange(0,b):	
				self.aux.append(0)
			self.vectorSalida.append(self.aux)
	def menor(self):
		#aca se busca el numero menor
		m=0
		posiciones=None
		for x in xrange(0,self.a):
			for y in xrange(0,self.a):
				print str(x)+" "+str(y)+": "+str(self.vectorEntrada[x][y])
				if m==0:
					if self.vectorEntrada[x][y]!=0:
						m=self.vectorEntrada[x][y]
						posiciones = Posicion(x,y)
				else:
					if self.vectorEntrada[x][y]!=0:
						if self.vectorEntrada[x][y]<m:
							m=self.vectorEntrada[x][y]
							posiciones = Posicion(x,y)
		return posiciones
	def buscar(self,z):

		#se busca si el elemento ya esta en el conjunto solucion
		t=True
		for x in xrange(0,self.a):
			if self.vectorSalida[x][z]!=0:
				t= False
		return t


















