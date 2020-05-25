try:
    import wx
    import wx.adv
except ImportError:
    wx = None

try:
    import win32gui, win32con
except ImportError:
    win32gui = None
    win32con = None

# TRAY_TOOLTIP = 'WarframeDB'
# TRAY_ICON = 'icon.png'

if wx is not None and win32gui is not None:
    class SysTrayConsole(wx.adv.TaskBarIcon):
        def __init__(self, tray_tooltip, tray_icon, console_window_hwnd=None):
            app = wx.App()

            # todo: get status instead of keeping in memory
            self.shown = True

            if console_window_hwnd is None:
                self.console_window_hwnd = win32gui.GetForegroundWindow()
            else:
                self.console_window_hwnd = console_window_hwnd

            super(SysTrayConsole, self).__init__()
            self.set_icon(tray_icon, tray_tooltip)
            self.menu = wx.Menu()
            self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
            self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.on_left_double)

            app.MainLoop()

        def CreatePopupMenu(self):
            self.create_menu_item('Show console', self.console_show)
            self.create_menu_item('Hide console', self.console_hide)
            self.menu.AppendSeparator()
            self.create_menu_item('Exit', self.on_exit)
            return self.menu

        def set_icon(self, icon_path, tooltip):
            icon = wx.Icon(wx.Bitmap(icon_path))
            self.SetIcon(icon, tooltip)

        def on_left_down(self, event):
            # print('Tray icon was left-clicked.')
            pass

        def on_left_double(self, event):
            self.console_toggle_hidden()
            # print('Tray icon was double-clicked.'
            pass

        def on_exit(self, event):
            wx.CallAfter(self.Destroy)

        def create_menu_item(self, label, func):
            item = wx.MenuItem(self.menu, -1, label)
            self.menu.Bind(wx.EVT_MENU, func, id=item.GetId())
            self.menu.Append(item)
            return item

        def console_hide(self):
            self.console_toggle_hidden(hide=True)

        def console_show(self):
            self.console_toggle_hidden(hide=False)

        def console_toggle_hidden(self, hide=None):
            if hide is None:
                hide = not self.shown
            if hide:
                win32gui.ShowWindow(self.console_window_hwnd, win32con.SW_HIDE)
                self.shown = False
            else:
                win32gui.ShowWindow(self.console_window_hwnd, win32con.SW_SHOW)
                self.shown = True
else:
    class SysTrayConsole:
        def __init__(self):
            if wx is None:
                raise Exception("Cannot use SysTrayConsole: wxPython is not present.")

            if win32gui is None:
                raise Exception("Cannot use SysTrayConsole: pywin32 is not present.")

    if __name__ == '__main__':
        print('This is just a library. Not a runnable script.')
