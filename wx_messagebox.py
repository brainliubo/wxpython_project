import wx
'''
import wx.lib.agw.genericmessagedialog as GMD

# Our normal wxApp-derived class, as usual
app = wx.App(0)

main_message = "Hello world! I am the main message."

dlg = GMD.GenericMessageDialog(None, main_message, "A Nice Message Box",
                               agwStyle=wx.ICON_INFORMATION | wx.OK)

dlg.ShowModal()
dlg.Destroy()

app.MainLoop()
'''

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)
        # Layout
        self.CreateStatusBar()
        self.PushStatusText("Close this window")
        # Event Handlers
        self.Bind(wx.EVT_CLOSE, self.OnClose)
    def OnClose(self, event):
        result = wx.MessageBox("Are you sure you want to close this window?",
        style=wx.CENTER|\
        wx.ICON_QUESTION| \
              wx.ICON_INFORMATION |wx.YES_NO)
        if result == wx.NO:
            event.Veto()
        else:
            event.Skip()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None)
    frame.Show()
    app.MainLoop()