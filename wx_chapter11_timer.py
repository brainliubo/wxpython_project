class TimerTaskBase(object):
    """Defines interface for long running task
    state machine.
    """
    TASK_STATE_PENDING, \
    TASK_STATE_RUNNING, \
    TASK_STATE_COMPLETE = range(3)
    def __init__(self):
        super(TimerTaskBase, self).__init__()
        # Attributes
        self._state = TimerTaskBase.TASK_STATE_PENDING
        #---- Interface ----#
    def ProcessNext(self):
        """Do next iteration of task
        @note: must be implemented by subclass
        """
        raise NotImplementedError

    def InitTask(self):
        """Optional override called before task
        processing begins
        """

        self.SetState(TimerTaskBase.TASK_STATE_RUNNING)

    # ---- Implementation ----#
    def GetState(self):
        return self._state

    def SetState(self, state):
        self._state = state

class TimerTaskMixin(object):
    """Mixin class for a wxWindow object to use timers
    for running long task. Must be used as a mixin with
    a wxWindow derived class!
    """
    def __init__(self):
        super(TimerTaskMixin, self).__init__()
        # Attributes
        self._task = None
        self._timer = wx.Timer(self)
        # Event Handlers
        self.Bind(wx.EVT_TIMER, self.OnTimer, self._timer)

    def __del__(self):
        # Make sure timer is stopped
        self.StopProcessing()

    def OnTimer(self, event):
        if self._task is not None:
            self._task.ProcessNext()

        state = self._task.GetState()
        if state == self._task.TASK_STATE_COMPLETE:
            self._timer.Stop()

    def StartTask(self, taskobj):
        assert not self._timer.IsRunning(), \
            "Task already busy!"

        assert isinstance(taskobj, TimerTaskBase)
        self._task = taskobj
        self._task.InitTask()
        self._timer.Start(100)

    def StopProcessing(self):
        if self._timer.IsRunning():
            self._timer.Stop()