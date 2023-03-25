 
file1 = open('file.cpp', 'r')
Lines = file1.readlines()
for line in Lines:
    
    def Remove(line):
     return line.replace(" ", "")
 
def RemoveComments(line, text):
        result = text
        ofs = 0
        if text:
            lines = text.split('\*' ,'*/','//')
            if lines.strip() == '/*': # remove comment
                ofs = -1
            elif  lines.strip() == '/*': # remove comment
                ofs = -1
            elif  lines.strip() == '*/': # remove comment
                   ofs = -1
            elif  lines.strip() == '//': # remove comment
                      ofs = -1
        else:
          ofs=1
          return result, ofs
        
def remove(line):
          if "#" in contents[line]:

        # delete the line if startswith "#"
            if contents[line].startswith("#"):
               contents.remove(contents[line])
               line+=1

          
          

print(remove(line))


print(line)
