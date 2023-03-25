# reading the file
with open("project3.py") as fp:
    contents=fp.readlines()

# initialize two counter to check mismatch between "(" and ")"
open_bracket_counter=0
close_bracket_counter=0

# whenever an element deleted from the list length of the list will be decreased
decreasing_counter=0

for number in range(len(contents)):

    # checking if the line contains "#" or not
    if "#" in contents[number-decreasing_counter]:

        # delete the line if startswith "#"
        if contents[number-decreasing_counter].startswith("#"):
            contents.remove(contents[number-decreasing_counter])
            decreasing_counter+=1

        # delete the character after the "#"
        else:
            newline=""
            for character in contents[number-decreasing_counter]:
                if character=="(":
                    open_bracket_counter+=1
                    newline+=character
                elif character==")":
                    close_bracket_counter+=1
                    newline+=character
                elif character=="#" and open_bracket_counter==close_bracket_counter:
                    break
                else:
                    newline+=character
            contents.remove(contents[number-decreasing_counter])
            contents.insert(number-decreasing_counter,newline)


# writing into a new file
with open("newfile.py","w") as fp:
    fp.writelines(contents)

    import re

    # read the file
    with open('project.txt') as f:
        read_file = f.read()
        print(type(read_file))  # to confirm that it's a string

    read_file = re.sub(r'\s{2,}', ',', read_file)  # find/convert 2+ whitespace into ','

    # write the file
    with open('project.txt', 'w') as f:
        f.writelines('read_file')

        with open(str_path, 'r') as file:
            str_lines = file.readlines()

        # remove spaces
        if bl_right is True:
            str_lines = [line.rstrip() + '\n' for line in str_lines]
        elif bl_left is True:
            str_lines = [line.lstrip() + '\n' for line in str_lines]
        else:
            str_lines = [line.strip() + '\n' for line in str_lines]

        # Write the file out again
        with open(str_path, 'w') as file:
            file.writelines(str_lines)