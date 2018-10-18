import wx
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="The Main Frame")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
# Attributes
        self.panel = wx.Panel(parent = self)

        self.button = wx.Button(self.panel,wx.ID_CANCEL,pos = (50,50))# 使用系统默认的ID，就不用设置label了
        self.butid  = self.button.GetId()
        print(self.butid)
        self.Bind(wx.EVT_BUTTON,self.button_click, self.button)

        menu_bar = wx.MenuBar()
        edit_menu = wx.Menu()
        edit_menu.Append(wx.NewId(), item = "Test1",helpString = "test when click")
        edit_menu.Append(wx.ID_PREFERENCES) # 使用系统默认的ID，就不用设置item了
        menu_bar.Append(edit_menu, title = "Edit")
        self.SetMenuBar(menu_bar)

    def button_click(self,event): #定义相应函数，handler
        for children in self.GetChildren():
            print(children)
        button = self.panel.FindWindowById(self.butid) #找到Button
        print(type(button))
        button.SetLabel("标签改变")

        panel = button.GetParent() #找到parent
        print(type(panel))

        app = wx.GetApp()  #get app
        print(app)
        frame = app.GetTopWindow()
        print(frame)





if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()









