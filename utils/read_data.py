from models.number import Number

dataPath = "data.txt"

f = open(dataPath, "r")
data = f.read()


class DataRead:

    def getValueFromText(self, data, startText, endText):
        data = data[(data.find(startText) + len(startText)):]
        index = data.find(endText)
        if (index != -1):
            data = data[:index]
            return data
        else:
            return None

    def getNumbersAndNames(self):
        if (data != None):
            numberAndNames = []
            tempData = self.getValueFromText(
                data, "<numbers>", "</numbers>").strip()

            while (True):
                if tempData.find(";") == -1:
                    break

                number = tempData[:tempData.find(":")]
                name = tempData[tempData.find(":") + 1:tempData.find(";")]
                numberAndNames.append(Number(name, number))
                tempData = tempData[tempData.find(";") + 1:].strip()

            return numberAndNames

        else:
            return None
