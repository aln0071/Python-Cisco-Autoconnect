import pyautogui as gui
import time

def locate(path):
    while(1):
        try:
            x,y = gui.locateCenterOnScreen(path)
        except:
            print('waiting...')
            time.sleep(0.5)
        else:
            break
    return x,y

def openAndClickCisco(mode):
    gui.hotkey('winleft', 'r')
    time.sleep(0.5)
    gui.typewrite('C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\\vpnui.exe')
    gui.press('return')
    a,b = locate('.\cisco.png')
    try:
        gui.locateCenterOnScreen(".\connected.png")
    except:
        if(mode=='1'):
            gui.click(a,b)
            gui.click(a-50, b-70)
    else:
        if(mode=='0'):
            gui.click(a,b)
            gui.click(a-50, b-70)

def toggleInternetOptions(mode):
    gui.hotkey('winleft', 'r')
    gui.typewrite('inetcpl.cpl')
    gui.hotkey('return')
    x,y = locate('.\connections.png')
    gui.click(x,y)
    gui.hotkey('shift', 'l')
    x,y = locate('internetoptions.png')
    try:
        gui.locateCenterOnScreen(".\proxydisabled.png")
    except:
        if(mode == '1'):
            gui.click(x-165,y+145)
    else:
        if(mode == '0'):
            gui.click(x-165,y+145)
    gui.click(x+50,y+250)
    time.sleep(0.25)
    gui.typewrite(['esc'])

secs = 1;
mode = input("0: disconnect\n1: connect\n");
toggleInternetOptions(mode)
if(mode == '0'):
    openAndClickCisco(mode);
    gui.hotkey('alt', 'f4')
    exit(0)
f = open("rsa.txt", "r")
password = f.read()
f.close()
gui.hotkey('winleft', 'r')
gui.typewrite('C:\Program Files (x86)\RSA SecurID Software Token\SecurID.exe')
gui.hotkey('return')
x,y = locate('.\pin.png')
gui.click(x+200, y)
gui.typewrite(password)
gui.press('return')
x,y = locate('.\copy.png')
gui.click(x,y)
openAndClickCisco(mode)
time.sleep(3)
x,y = locate('password.png')
gui.click(x,y)
gui.click(x+100,y+80)
gui.hotkey('ctrl', 'v')
gui.hotkey('return')
time.sleep(1)
x,y = locate('.\\accept.png')
gui.click(x,y)
