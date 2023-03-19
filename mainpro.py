class Functions():
    def remove_Spaces(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
        stripped_lines=""
        for line in content:
            for l in line:
                if l ==" " or l=="\n":
                    l=""

                else:
                    stripped_lines+=l
        print(f"remove Spaces:\n{stripped_lines}")

    def remove_Libraries(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()

        stripped_lines = ""
        for line in content:
            if not line.startswith('#include'):
                stripped_lines+= line
        print(f"remove Libraries:\n{stripped_lines}")
        # Join the stripped lines and write them back to the file
        
    def remove_Comments(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
        stripped_lines = ""
        for line in content:
            if not line.startswith('/*') and not line.endswith('*/') and not line.startswith('//'):
                stripped_lines+= line
        print(f"remove Comments:\n{stripped_lines}")


# test class functions
Functions.remove_Libraries("C:\\Users\DELL\Desktop\mat2.txt")
Functions.remove_Comments("C:\\Users\DELL\Desktop\mat2.txt")
Functions.remove_Spaces("C:\\Users\DELL\Desktop\mat2.txt")