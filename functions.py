
def remove_whitespace(Lines):
    list=[]
    for line in Lines:
        newline = line.replace(" ","")
        if newline.startswith('\n') is False :
            # file2.write(newline)
            list.append(newline)
    return list

def remove_singlecommand(Lines):
    list=[]
    for line in Lines:
        if line.startswith('//') is False:
            if '//' in line:
                indexStart = line.index('/')
                if indexStart == -1 :
                    list.append(line)
                else :     
                    list.append(line[0:indexStart])
            else:
                list.append(line)
    return list


def remove_blockcommand(Lines):
    command = False
    list=[]
    for line in Lines:
        if command == True :
            if '*/' in line:
                    command = False
            else :
                break
        elif line.startswith('/*') is False:
            if '/*' in line:
                indexStart = line.index('/')
                if indexStart == -1 :
                    list.append(line)
                else :     
                    list.append(line[0:indexStart]+'\n')
            if '*/' in line:
                command = False
            else:
                list.append(line)
    return list

def remove_externallibraries(Lines):
    list=[]
    for line in Lines:
        if line.startswith('#') is False and line.startswith('using') is False :
            list.append(line)
    return list
