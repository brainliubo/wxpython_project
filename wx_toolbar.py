import wx

#创建一个字典，进行ID的转化
ART_MAP = { wx.ID_CUT : wx.ART_CUT,
wx.ID_COPY : wx.ART_COPY,
wx.ID_PASTE : wx.ART_PASTE }

'''
创建一个class
'''
class EasyToolBar(wx.ToolBar):
    def AddEasyTool(self, id, shortHelp="", longHelp=""):
        """Simplifies adding a tool to the toolbar
        @param id: Stock ID
        """
        assert id in ART_MAP, "Unknown Stock ID"
        art_id = ART_MAP.get(id)
        bmp = wx.ArtProvider.GetBitmap(art_id, wx.ART_TOOLBAR)
        self.AddSimpleTool(id, bmp, shortHelp, longHelp)

class ToolBarFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ToolBarFrame, self).__init__(*args, **kwargs)
        # Setup the ToolBar
        toolb = EasyToolBar(self)
        toolb.AddEasyTool(wx.ID_CUT)
        toolb.AddEasyTool(wx.ID_COPY)
        toolb.AddEasyTool(wx.ID_PASTE)
        toolb.Realize()
        self.SetToolBar(toolb)
        # Event Handlers
        self.Bind(wx.EVT_TOOL, self.OnToolBar)

    def OnToolBar(self, event):
        print ("ToolBarItem Clicked {}".format( event.GetId()))

if __name__ == "__main__":
    app = wx.App()
    frame = ToolBarFrame(parent=None)
    frame.Show()
    app.MainLoop()