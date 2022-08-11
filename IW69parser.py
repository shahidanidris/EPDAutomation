# Import Libraries
import pandas as pd
import PySimpleGUI as sg
import time
import sys

# GUI Menu
sg.theme("DarkTeal2")
layout = [  [sg.T("")], 
            [sg.Text("IW69 Excel File: "), sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), key="-IN-")],
            [sg.Text("List Of Tag Numbers: "), sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), key="-IN2-")],
            [sg.Button("Submit")]
            ]
window = sg.Window('My File Browser', layout, size=(600,150))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        sourceFile = values["-IN-"]
        tagExcel = values["-IN2-"]
        break
window.close()

# Read IW69
sourceFile_df = pd.read_excel(sourceFile)

# Check columns to know if really IW69
correctColumns = ['Planning plant',
'Functional Loc.',
'Description',
'Equipment',
'Order',
'Notification',
'Description.1',
'ObjectPartCode',
'ObjPartCodeText',
'Damage Code',
'Prob. code text',
'Cause grp. text',
'Notif.date',
'Completn date',
'Malfunct. start',
'Malfunct.end',
'Notifictn type',
'Main WorkCtr',
'System status',
'Catalog profile',
'Code group',
'Obj.p. grp.txt.',
'Code group.1',
'Prob. grp. text',
'Code group.2',
'Cause code',
'Cause code text']

# Tags-To-Scan Excel reading
tagExcel_df = pd.read_excel(tagExcel)
tagsToScan = tagExcel_df['tags'].tolist()

print("Number of Tag Numbers to Scan:", len(tagsToScan))

print("Checking if Excel is IW69 generated...")
excelColumnCheck = True
for col in sourceFile_df.columns:
    if col not in correctColumns:
        excelColumnCheck = False

time.sleep(1)
if excelColumnCheck == True:
    print("Check PASSED! File is usable...")
else:
    print("Check FAILED! File is unusable...")

tagsWithData = []

for tags in tagsToScan:
# while True:
    # tagNum = input("Input Tag Number: ")
    tagNum = tags
    if tagNum.startswith("CUF-"):
        rewrittenTagNum = tagNum.replace("CUF-", "")
        filteredTag_df = sourceFile_df.loc[sourceFile_df['Functional Loc.'] == tagNum]
        filteredTag_df = filteredTag_df.append(sourceFile_df.loc[sourceFile_df['Functional Loc.'] == rewrittenTagNum], ignore_index=True)
    elif tagNum == 'done':
        sys.exit()
    else:
        rewrittenTagNum = "CUF-" + tagNum
        filteredTag_df = sourceFile_df.loc[sourceFile_df['Functional Loc.'] == tagNum]
        filteredTag_df = filteredTag_df.append(sourceFile_df.loc[sourceFile_df['Functional Loc.'] == rewrittenTagNum], ignore_index=True)

    # print()
    # print("Collecting and Sorting Data from 1st Observation to Last...")
    filteredTag_df.sort_values(by='Notif.date')
    filteredTag_df.reset_index(inplace=True)
    # print("\n=== FULL DATA OVERVIEW ===")
    # print("Number of Data Points:", len(filteredTag_df.index))
    # print("\n\n")

    if len(filteredTag_df.index) == 0:
        continue
    elif len(filteredTag_df.index) > 0:
        tagsWithData.append(str(filteredTag_df.at[0, "Functional Loc."]))

    # dataCount = 1
    # while dataCount <= len(filteredTag_df.index):
    #     rowNum = dataCount - 1
    #     print("DATA #" + str(dataCount))
    #     print("=====================")
    #     print("Tag Number: " + str(filteredTag_df.at[rowNum, "Functional Loc."]))
    #     print("Tag Description: " + str(filteredTag_df.at[rowNum, "Description"]))
    #     print("Notification Number: " + str(filteredTag_df.at[rowNum, "Notification"]))
    #     print("Notification Description: " + str(filteredTag_df.at[rowNum, "Description.1"]))
    #     print("Part Damage: " + str(filteredTag_df.at[rowNum, "ObjPartCodeText"]))
    #     print("Damage Description: " + str(filteredTag_df.at[rowNum, "Prob. code text"]))
    #     print("Cause Description: " + str(filteredTag_df.at[rowNum, "Cause code text"]))
        
    #     # Date selecting logic
    #     print(filteredTag_df.at[rowNum, "Notif.date"])
    #     print(type(filteredTag_df.at[rowNum, "Notif.date"]))
    #     # dateTargetColumn = None
    #     # print("Malfunction Start Date: " + str(filteredTag_df.at[rowNum, "Cause code text"]))
    #     # filteredTag_df.at[rowNum, "Notif.date"]
    #     # filteredTag_df.at[rowNum, "Malfunct. start"]
    #     dataCount = dataCount + 1
    #     print()

for items in tagsWithData:
    print(items)