#!/usr/bin/python
# -*- coding: utf-8 -*-

from interfaz import  Interfaz
import wx

class Inicio(wx.Frame):
  
    def __init__(self, parent, title):
        super(Inicio, self).__init__(parent, title=title, size=(300, 200))
        self.mensaje=wx.StaticText(self,id=-1,label="Ingrese el numero de vertices ",pos=(20, 30))
        self.texto=wx.TextCtrl(self,id=-1,value="",pos=(20, 50),size=(100,20))
        self.boton = wx.Button(self,-1,label="aceptar",pos=(20, 70))
        self.Bind(wx.EVT_BUTTON, self.aceptarc, self.boton)
        self.Move((800, 250))
        self.Show()
    def aceptarc(self,a):
        self.a=int(self.texto.GetValue())
        app = wx.App()
        Interfaz(None, title='Tabla del Algoritmo de Kruskal',n=self.a)
        app.MainLoop()

if __name__ == '__main__':
  
    app = wx.App()
    Inicio(None, title='Algoritmo de Kruskal')
    app.MainLoop()