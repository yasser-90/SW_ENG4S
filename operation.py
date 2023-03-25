class operations:
    def single_cooment(text):
        for line in text:
            if '//' in line  :
                text.remove(line)
        return(text)
    
    def block_cooment(text):
        ind1=0
        ind2=0
        for line in text:
            if '/*' in line:
                ind1=text.index(line)
                print(ind1)
            if '*/' in line:
                ind2=text.index(line)
                print(ind2)
        del text[ind1:ind2+1]

        return text


    def space(text):
        new_list = [line.replace(" ", "") for line in text]
        return(new_list)

    def lib(text):
        txt = []
        for line in text:
            if '#include' not in line:
                txt.append(line)
        return txt
    def one_line(text):
        new_list = [line.replace('\n', '') for line in text]
        return(new_list)

    def open_curlly(text):
        new = [line.replace('{', '')  for line in text]
        return(new)
    def close_curlly(text):
        new = [line.replace ('}', '')  for line in text]
        return(new)

    def semi_colon(text):
        new_li = [line.replace(';','')  for line in text]
        return(new_li)
    def cin(text):
        new_li = [line.replace('>>','') for line in text]
        return(new_li)
    def cout(text):
        new_li = [line.replace('<<','') for line in text]
        return(new_li)
