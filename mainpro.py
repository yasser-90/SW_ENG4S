import re

def remove_comments(file_contents):
    with open(file_contents, "r") as f:
        file_contents = f.read()
    file_contents = re.sub(r"//.*", "", file_contents) #Remove single-line comments
    file_contents = re.sub(r"/\*[\s\S]*/", "", file_contents) 
    return file_contents


def remove_whitespace(content ):
    with open(content, 'r') as f:
        content = f.read()
    # match and replace all whitespace characters with an empty string
    content = "\n".join([line for line in content.strip().split("\n") if line.strip()])
    return content


def remove_calls(file_contents):
    # Open the file
    with open(file_contents, "r") as f:
        # Read the file contents into a string
        file_contents = f.read()
    file_contents = re.sub(r"#.*", "", file_contents)
    return file_contents

def copmression(filename):
    with open(filename, 'r') as f:
        content = f.read()
    content = re.sub(r'\s+', '', content)  # كبس الملف بسطر واحد
    return content

def change(filename):
    with open(filename, 'r') as f:
        content = f.read()
    new_content = content.replace(' ', '')
    return new_content

