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
        self._field1 = wx.TextCtrl(self)
        self._field2 = wx.TextCtrl(self)
        # Layout
        self._DoLayout()

    def _DoLayout(self):
        """Layout the controls"""
        vsizer = wx.BoxSizer(wx.VERTICAL)
        field1_sz = wx.BoxSizer(wx.HORIZONTAL)
        field2_sz = wx.BoxSizer(wx.HORIZONTAL)
        # Make the labels
        field1_lbl = wx.StaticText(self, label="Field 1:")
        field2_lbl = wx.StaticText(self, label="Field 2:")
        # Make the first row by adding the label and field
        # to the first horizontal sizer

        field1_sz.Add(field1_lbl,flag = wx.ALIGN_CENTER_VERTICAL | wx.RIGHT,border = 4)

        field1_sz.Add(self._field1,proportion = 1, flag = wx.ALIGN_CENTER_VERTICAL|wx.RIGHT,border = 4)


        # Do the same for the second row

        field2_sz.Add(field2_lbl,wx.ALIGN_CENTER_VERTICAL|wx.RIGHT,border = 4)

        field2_sz.Add(self._field2,proportion = 1, flag = wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM,border = 4)

        # Now finish the layout by adding the two sizers
        # to the main vertical sizer.
        #vsizer.AddStretchSpacer()
        vsizer.Add(field1_sz,proportion = 0,flag = wx.ALL,border = 5)

        vsizer.Add(field2_sz,proportion = 0,flag = wx.ALL,border = 5)

        #vsizer.AddStretchSpacer()

        # Finally assign the main outer sizer to the panel
        self.SetSizer(vsizer)


if __name__ == '__main__':
    app = wx.App()
    frame = BoxSizerFrame(parent=None)
    frame.Show()
    app.MainLoop()