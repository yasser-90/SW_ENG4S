import re
class New:
    def removeLibrary(output_file):
        with open('f.cpp', "r+") as file:
            output = ''
            for line in file:
                if re.match(r'#include\s*<.*>', line):
                    print(line)
                else:
                    if line:
                        output += str(line)+'\n'
            file.seek(0)
            file.write(output)

    output_file = removeLibrary('f.cpp')



    def removeComment(output_file):
        with open("f.cpp", "r") as input_file:
            contents = input_file.read()
            stripped_contents = re.sub(r'//.*?\n|/\*.*?\*/', '', contents, flags=re.DOTALL)
        
        with open('f.cpp', 'w') as file:
            file.write(stripped_contents)

    removeComment('f.cpp')


    def removeSpace(output_file):
        with open('f.cpp', "r+") as file:
            out = ''
            for line in file:
                stripped_line = line.strip()
                #print(stripped_line)
                if stripped_line:
                    out += str(stripped_line)+'\n'                     
            file.seek(0)
            file.write(out)
            file.truncate()

    output_file = removeSpace('f.cpp')

x = New()


