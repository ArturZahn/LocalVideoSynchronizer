import wx.adv
import wx
TRAY_TOOLTIP = 'Name' 
TRAY_ICON = 'icon.png' 


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    print("1")
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    print("2")
    def __init__(self, frame):
        print("3")
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        print("4")
        menu = wx.Menu()
        create_menu_item(menu, 'Hello', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        print("5")
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):      
        print("6")
        print ('Tray icon was left-clicked.')

    def on_hello(self, event):
        print("7")
        print ('Hello, world!')

    def on_exit(self, event):
        print("8")
        wx.CallAfter(self.Destroy)
        self.frame.Close()

class App(wx.App):
    def OnInit(self):
        print("9")
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    print("10")
    app = App(False)
    app.MainLoop()


if __name__ == '__main__':
    print("11")
    main()