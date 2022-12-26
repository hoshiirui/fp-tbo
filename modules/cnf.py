hasil = {}

def removeUnitProduction(keyList):
    global hasil
    for key, value in hasil.items():
        if key in keyList:
            tempList = []
            for prod in value:
                if len(prod.split(" ")) == 2:
                    tempList.append(prod)
                else:
                    for i in hasil[prod]:
                        if i not in tempList:
                            tempList.append(i)
            hasil[key] = tempList

def setOfProduction():
    global hasil
    hasil.clear()
    f = open("./variable_list.txt", "r", encoding="utf-8")
    for lines in f:
        line = lines.splitlines()
        line = line[0].split(" -> ")
        lhs = line[0]
        rhs = line[1].split(" | ")
        if lhs in hasil.keys():
            hasil[lhs].extend(rhs)
        else:
            hasil[lhs] = rhs
    f.close()
    for key, value in hasil.items():
        if key == "PropNoun":
            tempList = []
            for val in value:
                if val not in tempList:
                    tempList.append(val.lower())
            hasil[key] = tempList
    phrases = ["NumP", "AdvP", "AdjP", "PP", "NP", "VP"]
    removeUnitProduction(phrases)
    patterns = ["S", "P", "O", "Pel", "Ket"]
    removeUnitProduction(patterns)
    tempList = []
    tempDict = {}
    counter = 1
    for key, value in hasil.items():
        if key == "K":
            for val in value:
                if len(val.split(" ")) > 2:
                    temp = val.split(" ")
                    while len(temp) > 2:
                        checkStr = temp[0] + " " + temp[1]
                        isFound = False
                        for k, v in tempDict.items():
                            if checkStr == v:
                                isFound = True
                                temp.pop(0)
                                temp.pop(0)
                                temp.insert(0, k)
                                break
                        if not isFound:
                            tempDict["K" + str(counter)] = checkStr
                            temp.pop(0)
                            temp.pop(0)
                            temp.insert(0, "K" + str(counter))
                            counter += 1
                    tempList.append(" ".join(temp))
                else:
                    tempList.append(val)
            hasil[key] = tempList
    for key, value in tempDict.items():
        hasil[key] = [value]
    return hasil
