import wx

class MyNotebook(wx.Notebook):
    def __init__(self, parent):
        super(MyNotebook, self).__init__(parent,style = wx.NB_BOTTOM) # NB_TOP
        # Attributes
        self.textctrl = wx.TextCtrl(self, value="edit me",
        style=wx.TE_MULTILINE)
        self.blue = wx.Panel(self)
        self.blue.SetBackgroundColour(wx.BLUE)
        #使用此类进行文件系统的选择
        self.fbrowser = wx.GenericDirCtrl(self,style = wx.DIRCTRL_3D_INTERNAL)
        # Setup
        self.AddPage(self.textctrl, "Text Editor")
        self.AddPage(self.blue, "Blue Panel")
        self.AddPage(self.fbrowser, "File Browser")




class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
        #在frame上可以直接使用notebook,而不仅仅是panel
        self.notebook = MyNotebook(self)
        self.CreateStatusBar()  #


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None)
    frame.Show()
    app.MainLoop()