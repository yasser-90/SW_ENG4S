from operation import operations as oper
file1 = open('C:\\Users\\PC\\SW_ENG4S\\pars.cpp', 'r')
Lines = file1.readlines()    
txt_comm=oper.single_cooment(Lines)  
txt_spa= oper.space(txt_comm)
txt_lib=oper.lib(txt_spa)
txt_block= oper.block_cooment(txt_lib)
txt_line=oper.one_line(txt_block)
txt_open=oper.open_curlly(txt_line)
txt_close=oper.close_curlly(txt_open)
txt_free=oper.semi_colon(txt_close)
txt_cin=oper.cin(txt_free)
txt_cout=oper.cout(txt_cin)

print(txt_cout)  

with open('C:\\Users\\PC\\SW_ENG4S\\output.txt', 'w+') as finaly_output:
    finaly_output.writelines(txt_cout)
        
