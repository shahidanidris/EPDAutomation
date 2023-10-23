def getLongTextNoti(notiNum):
    import pyautogui
    import pyperclip
    import time
    import os
    import subprocess

    def copy_clipboard():
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
        return pyperclip.paste()

    path = 'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'

    os.system('start "" "' + path+ '"')
    time.sleep(8)
    # pyautogui.moveTo(841, 848)
    pyautogui.moveTo(322, 766)
    # pyautogui.doubleClick(841, 848)
    pyautogui.doubleClick(322, 766)

    time.sleep(8)
    pyautogui.moveTo(158, 78)
    pyautogui.click(158, 78)
    pyautogui.write('iw23', interval=0)
    pyautogui.press('enter')

    pyautogui.moveTo(470, 304)
    pyautogui.click(470, 304)
    pyautogui.write(str(notiNum), interval=0)
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.moveTo(509, 685)
    pyautogui.click(509, 685)
    pyautogui.hotkey('ctrl', 'a')
    var = copy_clipboard()
    subprocess.call(["taskkill","/F","/IM",'saplogon.exe'], stdout=subprocess.DEVNULL)
    
    return str(var.encode("utf-8"))

def getLongTextWO(WO):
    import pyautogui
    import pyperclip
    import time
    import os
    import subprocess

    def copy_clipboard():
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
        return pyperclip.paste()

    path = 'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'

    os.system('start "" "' + path+ '"')
    time.sleep(8)
    # pyautogui.moveTo(841, 848)
    pyautogui.moveTo(322, 766)
    # pyautogui.doubleClick(841, 848)
    pyautogui.doubleClick(322, 766)

    time.sleep(8)
    pyautogui.moveTo(158, 78)
    pyautogui.click(158, 78)
    pyautogui.write('iw33', interval=0)
    pyautogui.press('enter')

    pyautogui.moveTo(466, 304)
    pyautogui.click(466, 304)
    pyautogui.write(str(WO), interval=0)
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.moveTo(644, 316)
    pyautogui.click(644, 316)
    pyautogui.hotkey('ctrl', 'a')
    var = copy_clipboard()
    subprocess.call(["taskkill","/F","/IM",'saplogon.exe'], stdout=subprocess.DEVNULL)
    
    return str(var.encode("utf-8"))