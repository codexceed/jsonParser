
class jsParse:

    data = []


    def __init__(self, file):


        i = 0
        while file[i]!='=':
            i+=1
        dataVal = file[i+3:].strip('\'')
        self.data = self.parse(dataVal)




    def parseDict(self, valString):

        newDict = {}
        i=0
        key = None
        while i<len(valString):

            if valString[i]=='\"':

                i+=1
                temp = []
                while valString[i] != '\"':
                    temp.append(valString[i])
                    i += 1

                if key==None:
                    key = "".join(temp)
                else:
                    newDict[key] = "".join(temp)

                    key = None
            elif valString[i]=='[':
                j = i
                while valString[j] != ']':
                    j += 1
                newDict[key] = self.parseList(valString[i+1:j])

                i = j

                key = None



            elif valString[i] == '{':


                j = i + 1

                ind = 0

                while True:

                    if valString[j] == '{':

                        ind += 1

                    elif valString[j] == '}':

                        if ind != 0:

                            ind -= 1

                        else:

                            break

                    j += 1
                newDict[key] = self.parseDict(valString[i+1:j])
                key = None
                i = j

            i+=1

        return newDict



    def parseList(self, valString):

        arr = []
        i=0
        while i<len(valString):
            if valString[i]=='[':
                j = i
                while valString[j]!=']':
                    j+=1
                arr.append(self.parseList(valString[i+1:j]))
                i = j
            elif valString[i]=='{':
                j = i+1
                ind = 0
                while True:
                    if valString[j]=='{':
                        ind+=1
                    elif valString[j]=='}':
                        if ind!=0:
                            ind-=1
                        else:
                            break
                    j += 1


                arr.append(self.parseDict(valString[i+1:j]))
                i = j
            else:
                if valString[i]=='\"':
                    i+=1
                    temp = []
                    while valString[i]!='\"':

                        temp.append(valString[i])

                        i+=1

                    arr.append("".join(temp))

                i+=1
        return arr



    def parse(self, val):
        for i in range(len(val)):
            if val[i]=='[' or val[i]=='{':
                if val[i]=='[':
                    return self.parseList(val.strip('[').strip(']'))











f = open('data.json')
x = jsParse(f.read())
print x.data[0]['state']['cities']