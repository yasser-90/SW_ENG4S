def remove_spaces():
    """
    Removes all spaces from the input code.
    """
    file1 = open('code.txt', 'r')
    for line in file1.readlines():
        line = line.replace(' ', '')
        # write line in file
        print(line)
        
        



def remove_libraries():
    """
    Removes all libraries from the input code.
    """
    file1 = open('code.txt', 'r')
    for line in file1.readlines():
        if line.find('#include'):
            # write line in file
            print(line)


def remove_comments():
    """
    Removes all comments from the input code.
    """
    file1 = open('code.txt', 'r')
    for line in file1.readlines():
        if line.find('//') or line.find('*/') or line.find('/*'):
            # write line in file
            print(line)


x= remove_spaces()
y= remove_libraries()
z= remove_comments()

