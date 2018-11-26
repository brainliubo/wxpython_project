import wx

class Border(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size =(800,600))
        pane = wx.Panel(self, -1, size =(800,600))
        pane.SetBackgroundColour('yellow')
        boxsizer = wx.BoxSizer(wx.HORIZONTAL)

        btn1 = wx.Button(pane, -1, 'Botton1')
        btn2 = wx.Button(pane, -1, 'Botton2')
        btn3 = wx.Button(pane, -1, 'Botton3')

        boxsizer.Add(btn1, proportion=0, flag=wx.ALL, border=2)
        boxsizer.Add(btn2, proportion=1, flag=wx.ALL, border=2)
        boxsizer.Add(btn3, proportion=2, flag=wx.ALL, border=2)

        self.SetSizer(boxsizer)

        self.Centre()
        self.Show(True)

def main():
    app = wx.App()
    Border(None, -1, '')
    app.MainLoop()

if __name__ == '__main__':
    main()