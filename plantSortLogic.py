def plantSort(tag):
    if tag.startswith("CUF-"):
        tag = tag.replace("CUF-", "")

    structureDict = {}
    lineCount = 0

    with open("structure.txt") as structureFile:
        branch = structureFile.readlines()
        branch = [line.rstrip() for line in branch]
        
    for branchLine in branch:
        tempString = ""
        startingIndicator = False
        for alphabets in branchLine:
            if alphabets.isalpha() or alphabets.isnumeric():
                startingIndicator = True
            if startingIndicator:
                tempString = tempString + alphabets
        structureDict[lineCount] = tempString
        lineCount = lineCount + 1

    # Assumes 1 instance of tag in structure.txt
    for key, value in structureDict.items():
        if tag in value:
            if 'COGEN' in value:
                return 'COGEN'
            elif 'DEMIN' in value:
                return 'DEMIN'
            elif 'ASU1' in value:
                return 'ASU1'
            elif 'ASU2' in value:
                return 'ASU2'
    
    startLine = None

    for key, value in structureDict.items():
        if value.startswith(tag):
            startLine = key
    
    if startLine is None:
        tag = "CUF-" + tag
        structureDict = {}
        lineCount = 0

        with open("structure.txt") as structureFile:
            branch = structureFile.readlines()
            branch = [line.rstrip() for line in branch]
            
        for branchLine in branch:
            tempString = ""
            startingIndicator = False
            for alphabets in branchLine:
                if alphabets.isalpha() or alphabets.isnumeric():
                    startingIndicator = True
                if startingIndicator:
                    tempString = tempString + alphabets
            structureDict[lineCount] = tempString
            lineCount = lineCount + 1

        # Assumes 1 instance of tag in structure.txt
        for key, value in structureDict.items():
            if tag in value:
                if 'COGEN' in value:
                    return 'COGEN'
                elif 'DEMIN' in value:
                    return 'DEMIN'
                elif 'ASU1' in value:
                    return 'ASU1'
                elif 'ASU2' in value:
                    return 'ASU2'
        
        for key, value in structureDict.items():
            if value.startswith(tag):
                startLine = key

    if startLine is None:
        return 'NONE'

    while True:
        if 'COGEN' in structureDict.get(startLine) or 'HRSG' in structureDict.get(startLine) or 'CG' in structureDict.get(startLine):
            plant = 'COGEN'
            break
        elif 'DEMIN' in structureDict.get(startLine) or 'DW-' in structureDict.get(startLine):
            plant = 'DEMIN'
            break
        elif 'ASU1' in structureDict.get(startLine):
            plant = 'ASU1'
            break
        elif 'ASU2' in structureDict.get(startLine):
            plant = 'ASU2'
            break
        startLine = startLine - 1
        if startLine < 0:
            break

    try:
        return plant
    except:
        return 'NONE'