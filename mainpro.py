# def removeLibrary(file_ ):
#     file = open('FILE.cpp', 'r')
#     file_ = file.readlines()
    
#     for it in file_:
#         if it.startswith('#include'):
#             it = ' '  
#         #print(it)
#         file_ = it 
#         #print(file_)        
#     return file_

 

 
# def removeComment(file_):
#     file = open('FILE.cpp', 'r')
#     file_ = file.readlines()
#     for line in file_:
#         line = line.strip()
#         if line.startswith('//') :
#             line = ' '
#         elif  line.startswith('/*')  :
#             while line!=line.endswith('*\\'):
#                 line = ' '
#         file_ = line 
#         #print(file_)
#     return file_                   


# def removeSpace(file_):
#     file = open('FILE.cpp', 'r')
#     file_ = file.readlines()
#     for line in file_:
#         if  line.strip():
#             file_ = line            
#         else:
#             continue
#         #print(file_)
#     return file_

# file_ = removeLibrary('FILE.cpp')
# file_ = removeComment('FILE.cpp')
# file_ = removeSpace("FILE.cpp")


# # def readFile(path):
# #     file_ = open(path, 'r')
# #     fwrite = open(path, 'w')
# #     for info in file_.readlines():
# #         fwrite.write(info)

# # readFile('FILE.cpp')

# with open("output.txt", "w") as f:
#     f.write(file_)




# 18 hour working for this repo🤐😥
import re
def removeLibrary(output_file):
    with open('file.cpp', "r+") as file:
        output = ''
        for line in file:
            if re.match(r'#include\s*<.*>', line):
                print(line)
            else:
                if line:
                    output += str(line)+'\n'
        file.seek(0)
        file.write(output)

output_file = removeLibrary('FILE.cpp')



def removeComment(output_file):
    with open("FILE.cpp", "r") as input_file:
        contents = input_file.read()
        stripped_contents = re.sub(r'//.*?\n|/\*.*?\*/', '', contents, flags=re.DOTALL)
    
    with open('FILE.cpp', 'w') as file:
        file.write(stripped_contents)

removeComment('FILE.cpp')


def removeSpace(output_file):
    with open("FILE.cpp", "r+") as file:
        out = ''
        for line in file:
            stripped_line = line.strip()
            #print(stripped_line)
            if stripped_line:
                out += str(stripped_line)+'\n'
                     
        file.seek(0)
        file.write(out)
        file.truncate()

removeSpace('FILE.cpp')

# output_file = removeSpace('FILE.cpp')
# output_file = removeComment('FILE.cpp')
# output_file = removeLibrary('FILE.cpp')

# with open('new2.txt','r') as f2:
#     text2 = f2.read()
# with open('new.txt','r') as f:
#     text = f.read()
# with open('new2.txt','r') as f3:
#     text3 = f3.read()
# # print(text)
# # print(text2)
# set1 = set(text)
# set2 = set(text2)
# set3 = set(text3)

# common_words = (set1.intersection(set2))
# cc = (common_words.intersection(set3))
# with open('new5.txt','w') as f5:
#     f5.write(str(cc))