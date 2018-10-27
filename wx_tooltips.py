import wx

class ToolTipTestPanel(wx.Panel):
    def __init__(self, parent):
        super(ToolTipTestPanel, self).__init__(parent)
        # 添加一个button
        self.button = wx.Button(self, label="Go")
        # Setup
        self.button.SetToolTipString("Launch the shuttle")
        
        self.timer = wx.Timer(self)
        self.count = 11
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button, 0, wx.ALIGN_CENTER)
        msizer = wx.BoxSizer(wx.HORIZONTAL)
        msizer.Add(sizer, 1, wx.ALIGN_CENTER)
        self.SetSizer(msizer)
        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnGo, self.button)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
    def OnGo(self, event):
        self.button.Disable()
        print(self.timer.Start(1000))
        tlw = self.GetTopLevelParent()
        tlw.PushStatusText("Launch initiated...")
    def OnTimer(self, event):
        tlw = self.GetTopLevelParent()
        self.count -= 1
        tlw.PushStatusText("%d" % self.count)
        if self.count == 0:
            self.timer.Stop()
            wx.MessageBox("Shuttle Launched!")

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
        self.panel = ToolTipTestPanel(self)
        self.CreateStatusBar()  #

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None)
    frame.Show()
    app.MainLoop()