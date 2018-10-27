import wx

class MyListCtrl(wx.ListCtrl):
    def __init__(self, parent):
        super(MyListCtrl, self).__init__(parent,style=wx.LC_REPORT)
        # Add three columns to the list
        self.InsertColumn(0, "Column 1")
        self.InsertColumn(1, "Column 2")
        self.InsertColumn(2, "Column 3")

    def PopulateList(self, data):
        """Populate the list with the set of data. Data
        should be a list of tuples that have a value for each
        column in the list.
        [('hello', 'list', 'control'),]
        """
        for item in data:
            self.Append(item)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        # Attributes
        self.lst = MyListCtrl(self)
        # Setup
        data = [ ("row %d" % x,
        "value %d" % x,
        "data %d" % x) for x in range(100) ]
        self.lst.PopulateList(data)
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lst, 1, wx.EXPAND)
        self.SetSizer(sizer)
        # Event Handlers
        self.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnItemSelected)

    def OnItemSelected(self, event):
        selected_row = event.GetIndex()
        val = list()
        for column in range(3):
            item = self.lst.GetItem(selected_row, column)
            val.append(item.GetText())
        # Show what was selected in the frames status bar
        frame = self.GetTopLevelParent()
        frame.PushStatusText(",".join(val))


class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
        self.panel = MyPanel(self)
        self.CreateStatusBar()  #




if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None)
    frame.Show()
    app.MainLoop()




