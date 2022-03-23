import sys

from FR import FR


def funcs(oName):
    o = eval("imp." + oName)

    if (type(o).__name__ == "function") and (len(oName) <= 4):
        return True
    elif (type(o).__name__ == "function") and (oName[:2] != '__' and oName[-2:] != '__'):
        return True
    else:
        return False


if __name__ == '__main__':
    imp = __import__(sys.argv[1][:-3])
    allFuncs = list(filter(funcs, dir(imp)))
    txt = "<html>\n\t<body>"

    for func in allFuncs:
        fText = FR(eval("imp." + func))
        txt += fText.create()
    txt += "\n\t</body>\n</html>"
    newFile = sys.argv[2]
    file = open(newFile, "w")
    file.write(txt)
    file.close()



