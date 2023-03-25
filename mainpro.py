class Scanner:
    path = ''

    @staticmethod
    def readFile(path):
        information = []
        with open(path, 'r') as fileInfo:
            if fileInfo.readable():
                for info in fileInfo.readlines():
                    information.append(info)
            else:
                raise ValueError('Could not open source file')
        return information

    @staticmethod
    def writeFile(path, information):
        with open(path, 'w') as fileInfo:
            if fileInfo.writable():
                for info in information:
                    fileInfo.write(info)

    @staticmethod
    def removeComment(path):
        information = Scanner.readFile(path)
        newInformathion = []
        temp = []
        for counter in range(len(information)):
            # Remove Single Comment...

            if '//' in information[counter]:
                temp.append(counter)

            # Remove Double Comment...

            if '/*' in information[counter]:
                if '*/' in information[counter:]:
                    temp.append(counter)
                else:
                    for inerCounter in range(counter, len(information)):
                        if '*/' in information[inerCounter]:

                            temp.append(inerCounter)
                            break

                        temp.append(inerCounter)
            if counter not in temp:
                newInformathion.append(information[counter])

        Scanner.writeFile(path, newInformathion)

    @staticmethod
    def removeSpace(path):
        information = Scanner.readFile(path)
        newInformathion = []
        for counter in range(len(information)):
            # Remove White Space

            if len(information[counter]) != 1:
                newInformathion.append(information[counter])
        Scanner.writeFile(path, newInformathion)

    @staticmethod
    def removeLibrary(path):
        information = Scanner.readFile(path)
        newInformathion = []
        for counter in range(len(information)):
            # Remove White Library

            if '#include' not in information[counter]:
                newInformathion.append(information[counter])
        Scanner.writeFile(path, newInformathion)

    @staticmethod
    def showInformation(path):
        specialInfo = {
            'operations': [],
            'single_special_character': [],
            'double_special_character': [],
            'key_word': [],
            'variable': [],
            'numbers': []
        }
        operations = ['=', '+', '-', '*', '/', '%']
        singleSpecialCharacter = [';', ',', '<', '>', '.', '"', '\'',
                                  '(', ')', '[', ']', '{', '}', '|', '^', '$', '!', '@', ':', '&', '#']
        keyWord = ["int", "string", "char", "double", "break", "float", "for", "while", "do", "cout", "cin", "gets", "puts",
                   "endl", "using", "namespace", "std", "void", "system", "pause", "main", "if", "include", "iostream", "else"]
        doubleSpecialCharacter = ["&&", "==", "++", "\\", "||",
                                  "//", "<<", ">>", ">=", "<=", "+=", "-=", "*=", "!=", "--"]

        information = Scanner.readFile(path)
        allFindInfo = []
        temp = []
        for info in information:
            temp = info.split(" ")
            for tm in temp:
                if ';' in tm:
                    temp.remove(tm)
                    tm = tm.replace(';', '')
                    temp.append(tm)
                    allFindInfo.append(';')
                    specialInfo['single_special_character'].append(';')

            for num in temp:
                if num[0].isdigit():
                    allFindInfo.append(num)
                    specialInfo['numbers'].append(int(num))
            for op in operations:
                if op in temp:
                    allFindInfo.append(op)
                    specialInfo['operations'].append(op)

            for ssc in singleSpecialCharacter:
                if ssc in temp:
                    allFindInfo.append(ssc)
                    specialInfo['single_special_character'].append(ssc)

            for dsc in doubleSpecialCharacter:
                if dsc in temp:
                    allFindInfo.append(dsc)
                    specialInfo['double_special_character'].append(dsc)

            for kw in keyWord:
                if kw in temp:
                    allFindInfo.append(kw)
                    specialInfo['key_word'].append(kw)
            for tm in temp:
                if tm not in allFindInfo:
                    specialInfo['variable'].append(tm)
        return specialInfo
