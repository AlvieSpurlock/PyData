def PrintHeader(header):
    pHeader = "||=====[" + header + "]=====||\n\n"
    print(pHeader)
    return pHeader

def PrintSubHeader(subHead):
    if subHead == "":
        pSubHead = "[---[==]---]\n\n"
    else:
        pSubHead = "[---[" + subHead + "]---]\n\n"
    print(pSubHead)
    return pSubHead

def PrintNumberedList(mList):
    lines = []
    for index, item in enumerate(mList):
        line = f"{index + 1} - {item}"
        print(index + 1, "-", item)
        lines.append(line)
    return "\n".join(lines)

def PrintList(mList):
    lines = []
    for item in mList:
        line = f"{item}"
        print(item)
        lines.append(line)
    return "\n".join(lines)

# Debug

#PrintHeader("Test Header")
#PrintSubHeader("Test SubHeader")
#PrintNumberedList(["Test One", "Test Two", "Test Three"])