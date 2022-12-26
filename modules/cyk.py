from modules.cnf import *

tabelsegitiga = {}
g = None
previousNode = None

def getValid(inputString):
    global tabelsegitiga
    tabelsegitiga.clear()
    prodRules = setOfProduction()
    temp = inputString.lower().split(" ")
    inputString = temp
    for i in range(1,len(inputString)+1):
        for j in range(i, len(inputString)+1):
            tabelsegitiga[(i,j)] = []
    for i in reversed(range(1, len(inputString)+1)):
        for j in range(1, i+1):
            if (j == j + len(inputString) - i):
                tempList = []
                for key, value in prodRules.items():
                    for val in value:
                        if (val == inputString[j-1] and key not in tempList):
                            tempList.append(key)
                tabelsegitiga[(j, j + len(inputString) - i)] = tempList
            else:
                tempList = []
                resultList = []
                for k in range(len(inputString) - i):
                    first = tabelsegitiga[(j,j+k)]
                    second = tabelsegitiga[(j+k+1,j+len(inputString) - i)]
                    for fi in first:
                        for se in second:
                            if (fi + " " + se not in tempList):
                                tempList.append(fi + " " + se)
                for key, value in prodRules.items():
                    for val in value:
                        if (val in tempList and key not in resultList):
                            resultList.append(key)
                tabelsegitiga[(j,j+len(inputString) - i)] = resultList
    if "K" in tabelsegitiga[(1, len(inputString))]:
        return True
    else:
        return False

def getTable(inputString):
    global tabelsegitiga
    result = []
    n = len(inputString.split(" "))
    for i in range(1, n+1):
        temp = []
        for j in range(i):
            res = tabelsegitiga[(j+1, n-i+j+1)]
            if len(res) == 0:
                temp.append("\u2205")
            else:
                temp.append("{" + ", ".join(res) + "}")
        result.append(temp)
    result.append(inputString.split(" "))
    return result

print(getValid("Alex bercita-cita menjadi pilot"))
print(*getTable("Alex bercita-cita menjadi pilot"), sep="\n")
#print(TRIANGULAR_TABLE)
