import wx
class BoxSizerFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(BoxSizerFrame, self).__init__(*args, **kwargs)
        # Attributes
        self.panel = BoxSizerPanel(parent=self)
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        #self.SetInitialSize()   # 这个函数在库中没有
        self.Show()


class BoxSizerPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(BoxSizerPanel, self).__init__(*args, **kwargs)
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
        field1_sz.AddSpacer(50)
        field1_sz.Add(field1_lbl)
        field1_sz.AddSpacer(5)  # put 5px of space between
        field1_sz.Add(self._field1)
        field1_sz.AddSpacer(50)
        # Do the same for the second row
        field2_sz.AddSpacer(50)
        field2_sz.Add(field2_lbl)
        field2_sz.AddSpacer(5)
        field2_sz.Add(self._field2)
        field2_sz.AddSpacer(50)
        # Now finish the layout by adding the two sizers
        # to the main vertical sizer.
        vsizer.AddSpacer(50)
        vsizer.Add(field1_sz)
        vsizer.AddSpacer(15)
        vsizer.Add(field2_sz)
        vsizer.AddSpacer(50)
        # Finally assign the main outer sizer to the panel
        self.SetSizer(vsizer)


if __name__ == "__main__":
    app = wx.App()
    frame = BoxSizerFrame(parent=None)
    frame.Show()
    app.MainLoop()