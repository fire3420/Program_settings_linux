# Enter script code
import os
winClass = window.get_active_class()

if 'doublecmd.Double Commander' in winClass:
    os.system("xvkbd -no-jump-pointer -xsendevent -text '\C\[Prior]'")
elif 'gnome-terminal-server.Gnome-terminal' in winClass:
    keyboard.send_keys('cd ..')
    keyboard.send_keys('<enter>')
    keyboard.send_keys('la')
    keyboard.send_keys('<enter>')
else:
    keyboard.send_keys('<alt>+<up>')
