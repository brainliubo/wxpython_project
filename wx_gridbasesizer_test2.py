import wx
class BoxSizerFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        '''
          初始化时，要注意入口参数，这里参数有parent,但是在初始化时，没有使用parent,导致出错，但是Pycharm没有抱错。
        '''
        super(BoxSizerFrame, self).__init__(parent,*args, **kwargs)
        '''
        也可以采用下面这种方式进行初始化
       '''
        #wx.Frame.__init__(self,parent,*args,**kwargs)
        self.panel = BoxSizerPanel(parent=self)
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, proportion = 1 ,border = 2)
        self.SetSizer(sizer)




class BoxSizerPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(BoxSizerPanel, self).__init__(parent,*args, **kwargs)
        # Attributes

        # Layout
        self._DoLayout()

    def _DoLayout(self):
        """Layout the controls"""

        sizer = wx.GridBagSizer(vgap=8, hgap=8)
        txt_field1 =    wx.TextCtrl(self)
        txt_field2 =    wx.TextCtrl(self)
        field1_lbl = wx.StaticText(self, label="Field 1:")
        field2_lbl = wx.StaticText(self, label="Field 2:")

        sizer.Add(field1_lbl,(1,1))
        '''
        Add 方法的参数
        window (wx.Window) – 
        •pos (wx.GBPosition) – 
        •span (wx.GBSpan) – 
        •flag (int) – 
        •border (int) – 
        •userData (PyUserData) – 

        '''
        #必须加上wx.EXPAND,才能进行扩展。
        sizer.Add(txt_field1,(1,2),(1,10),flag = wx.EXPAND)

        sizer.Add(field2_lbl, (2, 1))
        sizer.Add(txt_field2, (2, 2), (2, 10),flag = wx.EXPAND)

        # 这里添加间隔，第一个括号里是size么？
        sizer.Add((80,80),(2,12))
        sizer.Add((80, 80), (4, 0))
        self.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App()
    frame = BoxSizerFrame(parent=None)
    frame.Show()
    app.MainLoop()