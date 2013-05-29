import wx
class InterfazSalida(wx.Frame):
    def __init__(self, parent, title):
    	self.zx=800
    	self.zy=600
        super(InterfazSalida, self).__init__(parent, title=title, size=(self.zx,self.zy))
        #######################################################################################
        ##################################Dibujar Circulos###################################3333
        self.Bind(wx.EVT_PAINT, self._onPaint)
        print str(320+(10/2))
        print str(object)
        self.Move((800, 250))
        self.Show()
    def _onPaint(self,a):
        dc = wx.PaintDC(self)
        dc.DrawLine(0,0,100,100)
if __name__ == '__main__':
    app = wx.App()
    InterfazSalida(None, title='Algoritmo de Kruskal (Salida)')
    app.MainLoop()      
