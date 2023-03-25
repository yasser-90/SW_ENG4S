from tkinter import filedialog

class cpp_proseces:

# here the function that we remove the single line comments
    def remove_single_line_comments(self, content):
        # here we find the index of // in content
        find_double_slash_of_comment = content.find("//")
        
        # here we create while to remove all single comments 
        while find_double_slash_of_comment != -1:

            # here we loop in content to find the newline (\n)
            for head in range(len(content)):
            
                if content[head] == '\n':
                    # here we concantet the text (the text to doble slash and pluse it conttent after the newline of double slash line we split the content by \n)
                    content = content[:find_double_slash_of_comment] + content[find_double_slash_of_comment:].split('\n', 1)[1]
                    break
            else:
                # here if dont found newline take same text
                content = content[:find_double_slash_of_comment]
            # here we find the double slach index again for while loop contion
            find_double_slash_of_comment = content.find("//")
        return content
    
    # her the function of remove multi line comments
    def remove_multi_line_comments(self,content):
       # here we fuond the first of multi line comment and end of it
        find_slash_and_star = content.find('/*')
        find_star_and_slash = content.find('*/')
        # here we clean the text from the multi line comment
        while  find_slash_and_star != -1 :
            content = content[:find_slash_and_star] + content[find_star_and_slash + 2:]
            find_slash_and_star = content.find('/*')
            find_star_and_slash = content.find('*/')
        return content    
    
    

    # here the function of remove the libraries from the cpp file 
    def remove_libraries(self, content):
        # here we split the content based on newline and store it in lines var
        lines = content.split('\n')
        new_content = ''
        
        # here we loop in lines var that have all lines of content
        for line in lines:
            # if the line dont  stara withe #include word we add it to new_content var
            if not line.startswith('#include'):
                new_content += line + '\n'
        return new_content

    
    # here the function that remove all wahitspacse and newlines and tab spases from file
    def remove_whitespace(slef,content) : 
        # here we replace all one spaces wiht nothig 
        content = content.replace(' ','')
        # here we replace all newlines whieh nothing
        content = content.replace('\n','')
        # gere we reokace all tab spases whit nothig
        content = content.replace('\t','')
        return content
    

