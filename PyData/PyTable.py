class PyTable:
    def __init__(self, value):
        self.bRow = value
        self.col = [self.bRow]

    def AddItem(self, val):
        self.col.append(val)

    def ReplaceItem(self, i, val):
        self.col[i] = val

    def RemoveItem(self, i):
        self.col[i] = {}   