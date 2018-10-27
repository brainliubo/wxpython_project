import wx
class FileEditorApp(wx.App):
    def OnInit(self):
        self.frame = FileEditorFrame(None,title="File Editor")  #
        self.frame.Show()
        return True


#定义一个class,为文件选择的frame
class FileEditorFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(FileEditorFrame, self).__init__(*args, **kwargs)
        # Attributes
        self.file = None
        #RICH2 表示的是文件的大小，可以超出64
        style=wx.TE_MULTILINE|wx.TE_RICH2
        #定义一个文本框
        self.txtctrl = wx.TextCtrl(self, style=style)
        # Setup
        self._SetupMenus()
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txtctrl, 1, wx.EXPAND)
        self.SetSizer(sizer)
        # Event Handlers
        #通过ID 来分辨来自不同的source的事件
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnExit)


    def _SetupMenus(self):
        """Make the frames menus"""

        menub = wx.MenuBar() #定义一个菜单栏
        fmenu = wx.Menu()    #定义一个菜单
        fmenu.Append(wx.ID_OPEN, "Open\tCtrl+O")  #加一个OPEN菜单
        fmenu.AppendSeparator()  # 加一个分割线
        fmenu.Append(wx.ID_SAVE, "Save\tCtrl+S")  #加SAVE和SAVE AS 菜单
        fmenu.Append(wx.ID_SAVEAS, "Save As\tCtrl+Shift+S")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_EXIT, "Exit\tCtrl+Q") #退出菜单
        menub.Append(fmenu, "File") #将菜单加入到菜单栏
        self.SetMenuBar(menub)  #将菜单栏加入到frame中

    def OnOpen(self, event):
        """Handle Open"""
        if event.GetId() == wx.ID_OPEN:
            self.DoOpen() #do open 函数
        else:
            event.Skip()

    def OnSave(self, event):
        """Handle Save/SaveAs"""
        evt_id = event.GetId()
        if evt_id in (wx.ID_SAVE,
                      wx.ID_SAVEAS):
            if self.file: #如果文件存在，则save
                self.Save(self.file)
            else:  #如果文件不存在，则save as
                self.DoSaveAs()
        else:
            event.Skip()


    def OnExit(self, event):
        """Handle window close event"""
        # Give warning about unsaved changes
        if self.txtctrl.IsModified():  #退出时，判断是否保存
            message = ("There are unsaved changes.\n\n"
                       "Would you like to save them?")
            style = wx.YES_NO | wx.ICON_WARNING | wx.CENTRE
            result = wx.MessageBox(message,
                                   "Save Changes?",
                                   style=style)
            if result == wx.YES: #如果需要保存，则判断文件是否存在，不存在，就SAVE AS
                if self.file is None:
                    self.DoSaveAs()
                else:
                    self.Save(self.file)
        else:
            print("no changes, close the window directly!")
        event.Skip()


    def DoOpen(self):
        """Show file open dialog and open file"""
        wildcard = "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self,
                        message="Open a File",
                        wildcard=wildcard,
                        style=wx.FD_OPEN)
        # Shows the dialog, returning ID_OK if the user pressed wx.OK, and ID_CANCEL otherwise
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath() #使用getpath得到选择的文件路径
            print(path)
            with open(path, "rb") as handle:
                text = handle.read()
                self.txtctrl.SetValue(text.decode("GBK")) #使用gbk进行解码
                self.file = path
        dlg.Destroy()  # 这个destoy好像没有什么用?

    def DoSaveAs(self):
        """Show SaveAs dialog"""

        wildcard = "Text Files (*.txt)|*.txt"
        # wx.FD_OVERWRITE_PROMPT: For save dialog only: prompt for a confirmation if a file will be overwritten
        # wx.FD_SAVE: This is a save dialog
        dlg = wx.FileDialog(self,
                            message="Save As",
                            wildcard = wildcard,
                            style = wx.FD_SAVE
                            | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.Save(path)
            self.file = path
        dlg.Destroy()

    #frame 的SAVE函数，指定路径文件写入，并将textctrl的SetModified 标志设置为false
    def Save(self, path):
        """Save the file"""
        self.txtctrl.SaveFile(path)  # 直接使用TextCtrl的SaveFile 进行保存
        ''' 
        with open(path, "wb") as handle:
            text = self.txtctrl.GetValue()  #这个GetValue在textctrl中是无效的，删除掉
            print(type(text))
            handle.write(text)
        '''
        self.txtctrl.SetModified(False)  #s




if __name__ == "__main__":
    app = FileEditorApp()

    app.MainLoop()