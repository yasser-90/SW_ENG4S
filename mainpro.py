def remove_comments(text):
    """Removes both single and multi-line comments from the text"""

    while True:

        start =text.find('/*')
        end = text.find('*/')
        if start != -1 or end != -1:
            text=text[:start]+text[end+2 :]
        else:
            break


    while True:
        start = text.find('//')
        if start != -1:
            i = start
            while i < len(text):
                if text[i] == '\n':
                    end = i
                    break
                i += 1
            text = text[:start] + text[end:]
        else:
            break

    return text

def remove_whitespace(text):
    """Removes all whitespace characters from the text"""
    return "".join(text.split())

def remove_libraries(text):
    """Removes all import statements from the text"""
    while True:
        start = text.find('#include')
        if start != -1:
            i = start
            while i < len(text):
                if text[i] == '\n':
                    end = i
                    break
                i += 1
            text = text[:start] + text[end:]
        else:
            break

    return text
# Read input file

with open("test.cpp", "r") as file:
    text = file.read()

# Remove comments, whitespace, and libraries
text = remove_comments(text)
text = remove_libraries(text)
text = remove_whitespace(text)




with open("output.txt", "w") as file:

    file.write(text)



#just to check something in github
print('andkjfaklsdjfkldsjfkldsjfkljflkdasjf;kl')