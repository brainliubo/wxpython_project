import wx

class MyApp(wx.App):
    def OnInit(self):  #OnInit 函数需要返回true
        #app 上添加frame
        self.frame = MouseFrame(None,title="key event")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MouseFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MouseFrame, self).__init__(parent,
        *args,
        **kwargs)
        # Attributes
        self.panel = wx.Panel(self)
        self.btn = wx.Button(self.panel) #parent = panel
        # Event Handlers
        self.panel.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        self.panel.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.panel.Bind(wx.EVT_MOTION,self.motion)
        self.bar = self.CreateStatusBar()
    def motion(self,event):
        print(type(event))
        position = event.GetPosition()
        print(type(position))
        print(position[0])
        self.PushStatusText("position = %d,%d" % (position[0],position[1]))

    def OnEnter(self, event):
        """Called when the mouse enters the panel"""
        self.panel.SetBackgroundColour(wx.RED)
        self.btn.SetForegroundColour(wx.BLACK)
        self.btn.SetLabel("EVT_ENTER_WINDOW")
        self.btn.SetInitialSize()


    def OnLeave(self, event):
        """Called when the mouse leaves the panel"""

        self.btn.SetLabel("EVT_LEAVE_WINDOW")
        self.btn.SetForegroundColour(wx.RED)

    def OnLeftDown(self, event):
        """Called for left down clicks on the Panel"""
        self.panel.Refresh()
        self.btn.SetLabel("EVT_LEFT_DOWN")

    def OnLeftUp(self, event):
        """Called for left clicks on the Panel"""

        position = event.GetPosition()
        self.btn.SetLabel("EVT_LEFT_UP")
        # Move the button
        self.btn.SetPosition(position)

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()