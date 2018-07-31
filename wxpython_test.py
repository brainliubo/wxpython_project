
import wx
class MouseEventFrame(wx.Frame):
    def __init__(self, parent,id):
        wx.Frame.__init__(self, parent, id, "Frame With Button",size=(300, 300)) #加标题,设置size
        self.panel = wx.Panel(self) #设置一个覆盖frame的panel
        self.button = wx.Button(self.panel,label = "Not Over", pos=(100, 15))
        # eventhandler的三要素：事件， 处理Hander函数，窗口部件
        # 第三个参数是在当触发窗口的部件和处理事件的窗口部件不同时使用
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick,self.button) #1 绑定按钮事件
        self.button.Bind(wx.EVT_LEFT_DOWN,self.OnEnterWindow) #2 绑定鼠标位于其上事件
        #self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow) #3 绑定鼠标离开事件

        #self.Bind(wx.EVT_LEFT_DOWN, self.OnEnterWindow, self.button)  # 1 绑定按钮事件
        #self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow, self.button)  # 1 绑定按钮事件
    def OnButtonClick(self, event): # 这个onButtonClick 是self的函数，是frame的函数，不是button的函数
        self.panel.SetBackgroundColour("red")
        self.panel.Refresh()

    def OnEnterWindow(self, event):# 这个是frame的函数
        self.button.SetLabel("Over Me!")
        event.Skip() #当没有这句话时,发现点击鼠标之后,没有触发OnButtonClick 这个函数
    def OnLeaveWindow(self, event):
        self.button.SetLabel("Not Over")
        event.Skip()
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MouseEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()