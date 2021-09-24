import wx
import wx.xrc
from wxFormBuilder.main import Main


class head(Main):
    def __init__(self,parent):
        super().__init__(parent)
        self.Timer = self.m_timer1.Start(60)
        
        
app = wx.App(False)
frame = head(None)
frame.Show()
app.MainLoop()