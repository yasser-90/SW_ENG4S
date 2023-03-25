from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
filename = askopenfilename()
print(f"filepath : {filename}")


class Functions():
    def __init__(self,filepath):
        self.filepath=filepath
    def remove_Spaces(self):
        with open(self.filepath, 'r') as file:
            content = file.readlines()
        stripped_lines=""
        for line in content:
            for l in line:
                if l ==" " or l=="\n":
                    l=""

                else:
                    stripped_lines+=l
        f = open("D:\\test.txt", "a")
        f.write(stripped_lines)
        f.close()
        print(f"remove Spaces:\n{stripped_lines}")

    def remove_Libraries(self):
        with open(self.filepath, 'r') as file:
            content = file.readlines()

        stripped_lines = ""
        for line in content:
            if not line.startswith('#include'):
                stripped_lines+= line
        f = open("D:\\test.txt", "a")
        f.write(stripped_lines)
        f.close()
        print(f"remove Libraries:\n{stripped_lines}")
        
    def remove_Comments(self):
        with open(self.filepath, 'r') as file:
            content = file.readlines()
        stripped_lines = ""
        for line in content:
            if not line.startswith('/*') and not line.endswith('*/') and not line.startswith('//'):
                stripped_lines+= line
        f = open("D:\\test.txt", "a")
        f.write(stripped_lines)
        f.close()
        print(f"remove Comments:\n{stripped_lines}")


# test Functions Class

Functions(filename).remove_Spaces()
Functions(filename).remove_Libraries()
Functions(filename).remove_Comments()
