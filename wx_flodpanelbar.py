import wx
import wx.lib.agw.foldpanelbar as fpb

class MyFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, -1, "FoldPanelBar Demo")

        text_ctrl = wx.TextCtrl(self, -1, size=(400, 100), style=wx.TE_MULTILINE)

        panel_bar = fpb.FoldPanelBar(self, -1, agwStyle=fpb.FPB_VERTICAL)

        fold_panel = panel_bar.AddFoldPanel("Thing")
        thing = wx.TextCtrl(fold_panel, -1, size=(400, -1), style=wx.TE_MULTILINE)

        panel_bar.AddFoldPanelWindow(fold_panel, thing)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(text_ctrl, 1, wx.EXPAND)
        main_sizer.Add(panel_bar, 1, wx.EXPAND)
        self.SetSizer(main_sizer)


# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()
