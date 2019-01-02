import wx
import threading

#定义线程
class FibThread(threading.Thread):
    def __init__(self, window, n):
        super(FibThread, self).__init__()
        # Attributes
        self.window = window
        self.n = n
     #定义线程的run 函数，在线程的start()中会调用run 函数
    def run(self):
        val = SlowFib(self.n)
        #等跑完之后，还是要输出值，并且stopbusy
        #call after 的第一个参数是处理函数，后面是*arg,**kw
        wx.CallAfter(self.window.output.SetValue, str(val))
        wx.CallAfter(self.window.StopBusy)  #在这里将stopbusy 调用

#计算fibonacci数组的函数
def SlowFib(n):
    """Calculate Fibonacci numbers
    using slow recursive method to demonstrate
    blocking the UI.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return SlowFib(n-1) + SlowFib(n-2)


####
class BlockingApp(wx.App):
    def OnInit(self):
        self.frame = BlockingFrame(None,
        title="Non-Blocking Gui")
        self.frame.Show()
        return True

class BlockingFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(BlockingFrame, self).__init__(*args, **kwargs)
        # Attributes
        self.panel = BlockingPanel(self)
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class BlockingPanel(wx.Panel):
    def __init__(self, parent):
        super(BlockingPanel, self).__init__(parent)
        # Attributes
        self.timer = wx.Timer(self)
        #spinctrl将textctrl和spinbutton结合在一起，设置了初始值为35，最小的值为1
        # 设置了max = 40之后，即使设置了超出40的值，也按照40来计算
        self.input = wx.SpinCtrl(self, value="35", min=1,max = 40)
        #输出的text框
        self.output = wx.TextCtrl(self)
        #定义2个button
        self.block = wx.Button(self, label="Blocking")
        self.noblock = wx.Button(self, label="Non-Blocking")
        #定义一个进度条
        self.prog = wx.Gauge(self)
        # Layout
        self.__DoLayout()
        # Event Handlers
        #（event,handler,source）三个参数
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        #wx.timer会发出wx.EVT_TIMER? 没有找到这个EVENT，处理函数是onPulse
        self.Bind(wx.EVT_TIMER, self.OnPulse, self.timer)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        gridsz = wx.GridSizer(2, 2, 5, 5)
        # Layout controls
        #将self.prog 放在vszier上面
        vsizer.Add(self.prog, 0, wx.EXPAND)
        #布局输入和输出
        gridsz.Add(wx.StaticText(self, label="fib(n):"))
        gridsz.Add(self.input, 0, wx.EXPAND)
        gridsz.Add(wx.StaticText(self, label="result:"))
        gridsz.Add(self.output, 0, wx.EXPAND)
        #将上面布局好的输入输出放在prog下面,bolder = 10
        vsizer.Add(gridsz, 0, wx.EXPAND | wx.ALL, 10)
        #将两个button 横放
        hsizer.Add(self.block, 0, wx.ALL, 5)
        hsizer.Add(self.noblock, 0, wx.ALL, 5)
        #将两个button 组装好的放在vsizer下面
        vsizer.Add(hsizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(vsizer)

    def OnButton(self, event):
        input = self.input.GetValue() #从spinctrl中获取输入值
        self.output.SetValue("") # clear output
        self.StartBusy() # give busy feedback
        #如果被点击的是block
        if event.GetEventObject() == self.block:
            # Calculate value in blocking mode
            val = SlowFib(input) #使用slowfib 计算
            self.output.SetValue(str(val))
            self.StopBusy()
        else:
            # Non-Blocking mode
            task = FibThread(self, input) #但是这里有问题：1)初始化时,window 是BlockPannl
            task.start() # 在start()函数中，会触发run函数，

    def OnPulse(self, event):
        self.prog.Pulse() # Pulse busy feedback

    def StartBusy(self):
        self.timer.Start(100) # 100ms
        self.block.Disable()  #disable 两个button
        self.noblock.Disable()

    def StopBusy(self):  #停止timer,将prog清0，使能Button
        self.timer.Stop()
        self.prog.SetValue(0)
        self.block.Enable()
        self.noblock.Enable()


if __name__ == '__main__':
    app = BlockingApp(False)
    app.MainLoop()