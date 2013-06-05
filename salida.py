#!/usr/bin/python
# -*- coding: utf-8 -*-

# move.py

import wx #importando la libreria Wxpython (Manejo de interfaz grafica)
from PosicionP import PosicionP #Importando la clase PosicionP (Guarda posiciones X y Y)
class InterfazSalida(wx.Frame): #iniciando la clase del formulario
    #constructor recibe como parametros el titulo de la ventana, la cantidad de elementos y el vector resultante
    def __init__(self, parent, title, n,vectorMostrar):
        #calculamos el tamaño de la ventana
    	self.zx=200+n*100
    	self.zy=600+n*30
    	self.n=n
        self.vector=vectorMostrar
        #llamamos al constructor de la clase padre
        super(InterfazSalida, self).__init__(parent, title=title, size=(self.zx,self.zy))
        #creacion de variables auxialiates para el manejo de los labels
        self.cajasDeTexto= []
        self.mensajex=[]
        self.mensajey=[]
        self.posix=60
        self.posiy=60
        self.caja=[]
        for x in xrange(0, n):
        	self.caja=[]
        	self.mensajex.append(wx.StaticText(self,id=-1,label="x:"+str(x),pos=(self.posix+x*75+30, 40)))
        	for y in xrange(0,n):
        		self.mensajey.append(wx.StaticText(self,id=-1,label="y: "+str(y),pos=(35, self.posiy+y*20+5)))
        	   	self.caja.append(wx.StaticText(self,id=-1,label=str(vectorMostrar[x][y]),pos=(self.posix+x*75, self.posiy+y*20)))
        	self.cajasDeTexto.append(self.caja)
        self.caja=wx.StaticText(self,id=-1,label="ALgoritmo de Kruskal",pos=(self.zx/2, 20))
        self.caja0=wx.StaticText(self,id=-1,label="Grafica del algoritmo de Kruskal",pos=(self.zx/4, self.zy-500))
        pesoint=self.calcularPeso()
        peso="El peso del grafo es de: "+str(pesoint)
        self.caja1=wx.StaticText(self,id=-1,label=peso,pos=(self.zx/4, self.posiy+n*21))
        #######################################################################################
        ##################################Dibujar Circulos###################################3333
        self.Bind(wx.EVT_PAINT, self.pintar) #evento para dibujar
        self.Move((800, 250)) #posicion de la ventana en el escritorio
        self.Show() #mostrar la ventana
    #funcion para calcular peso
    def calcularPeso(self):
        #r = peso o costo
        r=0
        #ciclo para deter el peso 
        for x in xrange(0, self.n):
            for y in xrange(0, self.n):
                if self.vector[x][y] != 0:
                    if x < y:
                        r=r+int(self.vector[x][y])
        return r
    #dibujando los grafos 
    def pintar(self, a):
        #variables auxiliares
        auxX = []
        aux = []
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.BeginDrawing()      
        for x in xrange(0, self.n):
            if x == 0:
                px = 50
                py = self.zy-300
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x), px+5, py-10)
                aux.append(PosicionP(x, px, py))
            elif x == 7:
                px = 400
                py = self.zy-300
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x),px+5,py-10)
                aux.append(PosicionP(x, px, py))
            elif x == 1:
                px = 50+(80*x)+(10*x)
                py = self.zy-350
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x), px+5, py-10)
                aux.append(PosicionP(x, px, py))
            elif (x % 2) == 0:
                px = 50+(40*x)+(10*x)
                py = self.zy-250
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x),px+5,py-10)
                aux.append(PosicionP(x, px, py))
            elif (x % 2) == 1:
                px = 50+(40*x)+(20*x)
                py = self.zy-350
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x), px+5, py-10)
                aux.append(PosicionP(x, px, py))
        #dibujo de lineas
        x1 = None
        x2 = None
        y1 = None
        y2 = None
        pen=wx.Pen("BLUE",3,wx.SOLID)
        dc.SetPen(pen)
        for x in xrange(0, self.n):
            for y in xrange(0, self.n):
                if self.vector[x][y] != 0:
                    if x < y:
                        for z in aux:
                            if z.n == x:
                                x1 = z.x
                                y1 = z.y
                            if z.n == y:
                                x2 = z.x
                                y2 = z.y
                        dc.DrawLine(x1+27, y1+15, x2-30, y2)
                        #dibujo de texto
                        dc.DrawText(str(self.vector[x][y]),x1+((x2-x1)/2)+5,y1+((y2-y1)/2))0