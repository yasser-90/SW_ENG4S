def save(text):
    savee=open("C:\\Users\\ALMANAR\\Desktop\\new.txt",'a')
    savee.write(text)
    savee.close()

file1 = open("C:\\Users\\ALMANAR\\Desktop\\file.txt", 'r')
Lines = file1.readlines()
x=''
for line in Lines:
   a=line.find('function')
   print(a)
   a2 = line.replace("function", '')

   slash = line.find('//')
   print(slash)
   #{print('//  in =>' + slash)}
   a2=a2.replace("//", '')
   if(slash>=0):
        a2 = a2.replace(a2,'')

   if (len(line)>1):
       save(a2)
  # print(line)

   print(a2)
   x=a2






