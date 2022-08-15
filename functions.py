def listOutTags():
    # Import Libraries
    import pandas as pd
    import PySimpleGUI as sg
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
    ## Make sure Excel has a column name "tags" with all tag numbers provided under this col
    tagsToScan = tagExcel_df['tags'].tolist()

    # To check number of tag numbers to scan matches
    print("Number of Tag Numbers to Scan:", len(tagsToScan))

    print("Checking if Excel is IW69 generated...")
    excelColumnCheck = True
    for col in sourceFile_df.columns:
        if col not in correctColumns:
            excelColumnCheck = False

    if excelColumnCheck == True:
        print("Check PASSED! File is usable...\n")
    else:
        print("Check FAILED! File is unusable...\n")

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

    for items in tagsWithData:
        print(items)

def detailedData():
    # Import Libraries
    import pandas as pd
    import PySimpleGUI as sg
    import sys
        
    # GUI Menu
    sg.theme("DarkTeal2")
    layout = [  [sg.T("")], 
                [sg.Text("IW69 Excel File: "), sg.Input(), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), key="-IN-")],
                [sg.Button("Submit")]
                ]
    window = sg.Window('My File Browser', layout, size=(600,150))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            sourceFile = values["-IN-"]
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

    print("Checking if Excel is IW69 generated...")
    excelColumnCheck = True
    for col in sourceFile_df.columns:
        if col not in correctColumns:
            excelColumnCheck = False

    if excelColumnCheck == True:
        print("Check PASSED! File is usable...\n")
    else:
        print("Check FAILED! File is unusable...\n")

    while True:
        tagNum = input("Input Tag Number [type 'done' to end program]: ")
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

        filteredTag_df.sort_values(by='Notif.date')
        filteredTag_df.reset_index(inplace=True)
        print("\n=== FULL DATA OVERVIEW ===")
        print("Number of Data Points:", len(filteredTag_df.index))
        print("\n\n")

        dataCount = 1
        while dataCount <= len(filteredTag_df.index):
            rowNum = dataCount - 1
            print("DATA #" + str(dataCount))
            print("=====================")
            print("Tag Number: " + str(filteredTag_df.at[rowNum, "Functional Loc."]))
            print("Tag Description: " + str(filteredTag_df.at[rowNum, "Description"]))
            print("Notification Number: " + str(filteredTag_df.at[rowNum, "Notification"]))
            print("Notification Description: " + str(filteredTag_df.at[rowNum, "Description.1"]))
            print("Part Damage: " + str(filteredTag_df.at[rowNum, "ObjPartCodeText"]))
            print("Damage Description: " + str(filteredTag_df.at[rowNum, "Prob. code text"]))
            print("Cause Description: " + str(filteredTag_df.at[rowNum, "Cause code text"]))
            
            # Date selecting logic
            print(filteredTag_df.at[rowNum, "Notif.date"])
            print(type(filteredTag_df.at[rowNum, "Notif.date"]))
            # dateTargetColumn = None
            # print("Malfunction Start Date: " + str(filteredTag_df.at[rowNum, "Cause code text"]))
            # filteredTag_df.at[rowNum, "Notif.date"]
            # filteredTag_df.at[rowNum, "Malfunct. start"]
            dataCount = dataCount + 1
            print()

def separateFiles():
    # Import Libraries
    import pandas as pd
    import PySimpleGUI as sg
    import os
    import shutil
    import openpyxl
    from collections import Counter
    from plantSortLogic import plantSort

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
    ## Make sure Excel has a column name "tags" with all tag numbers provided under this col
    tagsToScan = tagExcel_df['tags'].tolist()

    # To check number of tag numbers to scan matches
    print("Number of Tag Numbers to Scan:", len(tagsToScan))

    print("Checking if Excel is IW69 generated...")
    excelColumnCheck = True
    for col in sourceFile_df.columns:
        if col not in correctColumns:
            excelColumnCheck = False

    if excelColumnCheck == True:
        print("Check PASSED! File is usable...\n")
    else:
        print("Check FAILED! File is unusable...\n")

    print("Handling file creation, copying, and data processing...")

    if os.path.exists('filtered tags'):
        shutil.rmtree('filtered tags')

    # Create a folder named "filtered tags"
    if os.path.exists('filtered tags'):
        pass
    else:
        os.makedirs('filtered tags')

    emptyFile = "filtered tags/EMPTY.xlsx"
    shutil.copy(sourceFile, emptyFile)
    excel_file = openpyxl.load_workbook(emptyFile)
    excel_sheet = excel_file.worksheets[0]
    excel_sheet.delete_rows(idx=2, amount=excel_sheet.max_row + 1)
    excel_file.save(emptyFile)

    noDataCount = 0
    withDataCount = 0

    counts = dict(Counter(tagsToScan))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    print("DUPLICATES FOUND IN TAGS-TO-SCAN:")
    print(duplicates)

    for tags in tagsToScan:
        print("Processing " + tags + "...")
        tagNum = tags
        if tagNum.startswith("CUF-"):
            rewrittenTagNum = tagNum.replace("CUF-", "")
            filteredTag_df = sourceFile_df.loc[sourceFile_df['Functional Loc.'] == tagNum]
            filteredTag_df = filteredTag_df.append(sourceFile_df.loc[sourceFile_df['Functional Loc.'] == rewrittenTagNum], ignore_index=True)
        else:
            rewrittenTagNum = "CUF-" + tagNum
            filteredTag_df = sourceFile_df.loc[sourceFile_df['Functional Loc.'] == tagNum]
            filteredTag_df = filteredTag_df.append(sourceFile_df.loc[sourceFile_df['Functional Loc.'] == rewrittenTagNum], ignore_index=True)

        filteredTag_df.sort_values(by='Notif.date')
        filteredTag_df.reset_index(drop=True, inplace=True)

        if len(filteredTag_df.index) == 0:
            # Create a new Excel File with the necessary headers
            if "/" in tagNum:
                temporaryTagNum = tagNum.replace("/", "-")
            else:
                temporaryTagNum = tagNum
            # Create plant name folders
            if os.path.exists("filtered tags/" + plantSort(tagNum)):
                pass
            else:
                os.makedirs("filtered tags/" + plantSort(tagNum))
            targetFileName = "filtered tags/" + plantSort(tagNum) + "/" + str(temporaryTagNum) + "__NO_DATA" + ".xlsx"
            shutil.copy(emptyFile, targetFileName)
            noDataCount = noDataCount + 1
        
        elif len(filteredTag_df.index) > 0:
            # Create a new Excel File with the necessary headers
            if "/" in tagNum:
                temporaryTagNum = tagNum.replace("/", "-")
            else:
                temporaryTagNum = tagNum
            # Create plant name folders
            if os.path.exists("filtered tags/" + plantSort(tagNum)):
                pass
            else:
                os.makedirs("filtered tags/" + plantSort(tagNum))
            targetFileName = "filtered tags/" + plantSort(tagNum) + "/" + str(temporaryTagNum) + ".xlsx"
            filteredTag_df.to_excel(targetFileName, index=False)
            withDataCount = withDataCount + 1

    print("Total NO DATA =", noDataCount)
    print("Total WITH DATA =", withDataCount)
    print("Total tag numbers processed =", noDataCount + withDataCount)
    os.remove(emptyFile)

def failureData(sourceFile_df, tagNum):
    # Import Libraries
    import pandas as pd
        
    if tagNum.startswith("CUF-"):
        rewrittenTagNum = tagNum.replace("CUF-", "")
        filteredTag_df = sourceFile_df.loc[sourceFile_df['Functional Loc.'] == tagNum]
        filteredTag_df = filteredTag_df.append(sourceFile_df.loc[sourceFile_df['Functional Loc.'] == rewrittenTagNum], ignore_index=True)
    else:
        rewrittenTagNum = "CUF-" + tagNum
        filteredTag_df = sourceFile_df.loc[sourceFile_df['Functional Loc.'] == tagNum]
        filteredTag_df = filteredTag_df.append(sourceFile_df.loc[sourceFile_df['Functional Loc.'] == rewrittenTagNum], ignore_index=True)

    filteredTag_df.sort_values(by='Notif.date')
    filteredTag_df.reset_index(inplace=True)

    return filteredTag_df