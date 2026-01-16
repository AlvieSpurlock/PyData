import PyTable
import PyConsole

class PyData:

    def __init__(self, dataName, data):
        self.name = dataName
        self.table = PyTable(data)

    def AddData(self, data, nameIndex, useIndex):
        self.table.AddItem(data)
        self.SaveData(self.ConsolidateData(nameIndex, useIndex))

    def ReplaceData(self, i, data, nameIndex, useIndex):
        self.table.ReplaceItem(i, data)
        self.SaveData(self.ConsolidateData(nameIndex, useIndex))

    def RemoveItem(self, i, nameIndex, useIndex):
        self.table.RemoveItem(i)
        self.SaveData(self.ConsolidateData(nameIndex, useIndex))

    def ConsolidateData(self, nameIndex, useIndex):

        consolidated_output = PyConsole.PrintHeader(self.name)

        for table_row in self.table.col:
            if not table_row:
                continue
            consolidated_output += PyConsole.PrintSubHeader(table_row[nameIndex])
            if isinstance(table_row, dict):
                formatted_fields = [f"{field}: {value}" 
                                    for field, value in table_row.items()]
            elif isinstance(table_row, list):
                formatted_fields = [str(item) for item in table_row]
            else:
                formatted_fields = [str(table_row)]

            if useIndex:
                consolidated_output += PyConsole.PrintNumberedList(formatted_fields)
            else:
                consolidated_output += PyConsole.PrintList(formatted_fields)

            
            consolidated_output += "\n" + PyConsole.PrintSubHeader("") + "\n"

        return consolidated_output

    def SaveData(self, data):
        dataFile = open(f"{self.name}.txt", "w+")
        dataFile.write(data)
        dataFile.close()