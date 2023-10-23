import pandas as pd
import PySimpleGUI as sg
from mouseReader import getLongTextNoti, getLongTextWO
import re
import time
import datetime
import os

tagNumList = []
longTextList = []

# GUI Menu
sg.theme("DarkTeal2")
layout = [  [sg.Text("IW69 Excel File: "), sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), key="-IN-")],
            [sg.Text("WO Excel File: "), sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), key="-IN1-")],
            [sg.Button("Submit")]
            ]
window = sg.Window('My File Browser', layout, size=(600,150))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        sourceFile = values["-IN-"]
        woExcel = values["-IN1-"]
        break
window.close()

start_time = time.time()

iw69df = pd.read_excel(sourceFile)
wodf = pd.read_excel(woExcel)

iw69df = iw69df[['Functional Loc.', 'Notification', 'Order', 'Description.1']]
wodf = wodf[['Order', 'Description']]

new_df = iw69df.merge(wodf, left_on='Order', right_on='Order', how='inner')
new_df = new_df.astype({'Order': 'int'})
new_df = new_df.loc[(new_df['Functional Loc.'].str.endswith('TX')) | (new_df['Functional Loc.'].str.endswith('CV')) | (new_df['Functional Loc.'].str.endswith('VX')) | (new_df['Functional Loc.'].str.endswith('SV'))]

print("Total Notifications to Process: " + str(len(new_df)))

count = 1
indexCounter = 0
for index, row in new_df.iterrows():
    if os.path.exists('dataframe.csv'):
        final_df = pd.read_csv('dataframe.csv', index_col = [0])
    else:
        final_df = pd.DataFrame(columns=['tagNum', 'text'])
        final_df.to_csv('dataframe.csv')
    if indexCounter in final_df.index:
        print("Completed: " + str(count) + '/' + str(len(new_df)))
        indexCounter = indexCounter + 1
        count = count + 1
        continue
    s = getLongTextNoti(row['Notification'])
    s = s.replace(r"\r\n", " ")
    result = re.search("b'(.*)'", s)
    if result is None:
        result = re.search('b"(.*)"', s)
    s_wo = getLongTextWO(int(row['Order']))
    s_wo = s_wo.replace(r"\r\n", " ")
    result_wo = re.search("b'(.*)'", s_wo)
    if result_wo is None:
        result_wo = re.search(r'"(.+?)"', s_wo)
    newDataDict = {
        'tagNum' : row['Functional Loc.'],
        'text' : str(row['Description.1']) + ' ' + result.group(1) + ' ' + str(row['Description']) + ' ' + result_wo.group(1)
    }
    final_df = final_df.append(newDataDict, ignore_index=True)
    final_df.to_csv('dataframe.csv')
    print("Completed: " + str(count) + '/' + str(len(new_df)))
    count = count + 1
    indexCounter = indexCounter + 1

programExecutionTime = time.time() - start_time
print("Total code runtime:", str(datetime.timedelta(seconds=programExecutionTime)))