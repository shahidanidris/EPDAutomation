import PySimpleGUI as sg
from epdInput import epdCreator
from functions import detailedData, listOutTags, separateFiles
import shutil

selector = 0

# GUI Menu
sg.theme("DarkTeal2")
layout = [  [sg.Button("List Out Tags with Data")],
            [sg.Button("Create separate data files/folders from IW69")],
            [sg.Button("Show Detailed Data by Tag Number")],
            [sg.Button("Create EPD Files from IW69")],
            ]
window = sg.Window('My File Browser', layout, size=(600,150))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "List Out Tags with Data":
        selector = 1
        break
    elif event == "Create separate data files/folders from IW69":
        selector = 2
        break
    elif event == "Show Detailed Data by Tag Number":
        selector = 3
        break
    elif event == "Create EPD Files from IW69":
        selector = 4
        break
window.close()

if selector == 1:
    listOutTags()
elif selector == 2:
    separateFiles()
elif selector == 3:
    detailedData()
elif selector == 4:
    epdCreator()

shutil.rmtree('__pycache__')