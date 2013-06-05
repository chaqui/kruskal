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
        self.tamano=int(self.texto.GetValue())
        if self.tamano <9 and self.tamano >0:
            app = wx.App()
            Interfaz(None, title='Tabla del Algoritmo de Kruskal',n=self.tamano)
            app.MainLoop()
        else:
            dlg = wx.MessageDialog(self, "Debe de ser menor a 9", "error de <ingreso></ingreso>", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == '__main__':
  
    app = wx.App()
    Inicio(None, title='Algoritmo de Kruskal')
    app.MainLoop()