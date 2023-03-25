def commentRemove(lines):
    com_line = ""
    i = []
    j = []
    for line in lines:
        words = line.split()
        ind = lines.index(line)
        for word in words:
            if word.startswith('/') == True:
                if word[1] == '/':
                    break
            else:
                com_line += line
                break    
    for txt in com_line:
        if txt == ('*'):
            i.append(com_line.index(txt)-1)
            break
    for txt in com_line:
        if txt == ('*'):
            j.append(com_line.index(txt)+1)
            continue
    com = com_line[:i[0]]
    return(com)

def spaceRemove(lines):
    l = ''.join(lines)
    words = l.split(' ')
    nline = ''.join(words)
    return(nline)

def libRemove(lines):
    nl = ""
    for line in lines.split('\n'):
        words = line.split('<')
        if words[0] == '#include':
            continue
        else:
            nl += line
    return(nl)

cppfile = open('Cfile.cpp', 'r')
Lines = cppfile.readlines()
cr = commentRemove(Lines)
sr = spaceRemove(cr)
lr = libRemove(sr)

res = open('resultFile', 'w')
res.write(lr)
res.close