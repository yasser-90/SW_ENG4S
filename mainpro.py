import re
def removeComments(text):
    pattern = r"""
           /\* *\*+  \\.| [^"\\] """
           
    regex = re.compile(pattern)   # re.compile use to we can use this pattern object to search for a match inside different target strings using regex methods  
    noncomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    return "".join(noncomments)

def commentRemover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " #  a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)
  

filename = 'ggg.cpp'
with open(filename) as f:
    uncmtFile = commentRemover(f.read())
    with open("ggg.cpp","w") as fp:
        fp.writelines(uncmtFile)
        
        
        
        
def labdel():
 file1 = open('ggg.cpp', 'r')
 Lines = file1.readlines()
 for line in Lines:
    import re

    with open('ggg.cpp', 'r') as d:
        cpp_text = d.read()

    # Remove all #include
    cleaned_text = re.sub(r'^#include .*$', '', cpp_text, flags=re.MULTILINE)

    with open('ggg.cpp', 'w') as d:
        d.write(cleaned_text)
        
        
        
        
labdel()


def delspace():
  # Open the file in read mode
 with open("ggg.cpp", "r") as file:

    # Read the contents of the file
    file_contents = file.read()

    # Remove spaces from the file contents
    file_contents = file_contents.replace("\n", "")

# Open the file in write mode and write the modified contents
 with open("mmm.cpp", "w") as file:
    file.write(file_contents)
    print("hello")
    
delspace()