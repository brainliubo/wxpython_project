import wx
import time
class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize,
             style=wx.DEFAULT_FRAME_STYLE, name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)
        msg = "progress dialog "
        self.progdialog = wx.ProgressDialog("test progress",
                                            msg,
                                            maximum=1000,
                                            parent=self
                                            )
        for i in range(1000):
            time.sleep(0.01)
            self.progdialog.Update(i)

        if ( False  == self.progdialog.WasCancelled()):
            self.progdialog.Destroy()









if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None)
    frame.Show()
    app.MainLoop()