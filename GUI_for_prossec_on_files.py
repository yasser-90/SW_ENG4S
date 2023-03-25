#Create simple GUI to Process Cpp files and split the functions file
# here we call the library that provide GUI tools
from tkinter import * 

#here we call tkinter file dialoge tool
from tkinter import filedialog

# here we call the class of function
from class_of_function import *

# here we make copy of class
functions = cpp_proseces()


# here we creat the window or form 
window = Tk()

# window background color
window.configure(background="#0DA154")

# here we edit on window shap and size 
window.geometry('800x500+200+10')

# here we hide the tilte bar 
window.overrideredirect(True)

# here we create exit button
exit_button = Button(window,command=lambda:exit_button_function(),width=5,text="EXIT",bg="red",fg="black",font=("arial",10,"bold"))

# here we determine the exit button place on window
exit_button.place(x=740,y=10)

# here we create the import button whit edit on shap  
import_button = Button(window,font=("arial",10,"bold"),command=lambda:file_dialoge_open(),height=2,width=12,text="  Import",bg="gray",fg="black")

# here we determine place of button on window
import_button.place(x = "10",y = "20")

# here we creat the input or file path box
file_path_box = Entry(window,width= 30)

# here ww edit on input or file path box shap and size
file_path_box.config(font=("Arial", 20), bd=3, relief="sunken")

# here just clean this file path box if it have text prevesuly
file_path_box.config(text="0")

#here we determine box place on window
file_path_box.place(x = "130",y = "20")

# here we create frame to contane the text area
text_area_fram = Frame(window)

# here we create the text area that we display the file content in it 
text_area = Text(text_area_fram,height=5,width=90)

# here we put scroll bar to text area
scrollbar = Scrollbar(text_area_fram, command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# here we determine the the texr area place on Frame
text_area.pack(side=LEFT, fill=Y)

# here we detemine the frame place on window
text_area_fram.place(x = "10",y = "70")

# create entery of count letter of text we import
count_label_import = Label(window,bg="#0DA154",fg="black",font=("arial",12,"bold"))
count_label_import.place(x=120,y=160)
count_label2_import = Label(window,text="Count Of Letter :")
count_label2_import.place(x=10,y=160)

# here just we put line in window
canvas = Canvas(window, width=800, height=1,bg="black")
canvas.place(x = "0",y = "200")


# create label to question and edit its shape and text ...
question_label = Label(window,bg="#0DA154",text="What do you want Choose and Click Process :",fg="white",font=("arial", 16))

# here we determine the place of label on window
question_label.place(y = 210)

# create  variables to hold the value of check button (true or false)
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()


# here we create the Check buttons
remove_whitspace_radio = Checkbutton(window,variable=var1,font=("arial",10,"bold"),bg="#0DA154",text="Remove WhiteSpaces")
remove_library_radio = Checkbutton(window,font=("arial",10,"bold"),variable=var2,bg="#0DA154",text= "Remove Libraries ")
remove_single_line_comment_radio = Checkbutton(window,font=("arial",10,"bold"),variable=var3,bg="#0DA154",text="Remove Single Line Comments")
remove_multi_line_comment_radio = Checkbutton(window,font=("arial",10,"bold"),bg="#0DA154",text= "Remove Multi line comments",variable=var4)
remove_all_what_mentioned_before = Checkbutton(window,font=("arial",10,"bold"),bg="#0DA154",text= "Remove All What Mentioned Before",variable=var5)

# here we set the radio buttons on the window
remove_library_radio.place(x=650,y=213);remove_multi_line_comment_radio.place(x=10,y=240);remove_single_line_comment_radio.place(x=270,y=240);remove_whitspace_radio.place(x=460,y=213)
remove_all_what_mentioned_before.place(x=530,y=240)


# here we create frame to contane the text area
result_text_area_fram = Frame(window)

# here we create the text area that we display the file content in it 
result_text_area = Text(result_text_area_fram,height=5,width=87)

# here we put scroll bar to text area
scrollbar = Scrollbar(result_text_area_fram, command=result_text_area.yview)
result_text_area.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# here we determine the the texr area place on Frame
result_text_area.pack(side=LEFT, fill=Y)

# here we detemine the frame place on window
result_text_area_fram.place(x = "10",y = "300")

# we create button of prossece
prossece_button = Button(window,command=lambda:prossece_button_click(),width=7,height=5,text="Process")

# create label to question and edit its shape and text ...
after_label = Label(window,bg="#0DA154",text="The content after Process :",fg="white",font=("arial", 16))

# here we determine the place of label on window
after_label.place(y = 270)

# here we determine the place of button on window
prossece_button.place(x = 730, y = 300)


# we create the save button 
save_button = Button(window,command=lambda:save_file(),height=2,text="Save The Process Text",width=800,bg="green",fg="black",font=("arial",15),highlightthickness=2,highlightcolor="red")

# here the function that run when the mouse move on and leave on the save button
def enter(e):
    save_button.config(bg="red")
def leave(e):
    save_button.config(bg="green")

# here we set the functions to event
save_button.bind("<Enter>", enter) 
save_button.bind("<Leave>", leave)  


# here we determinet the save button place on window
save_button.pack(side=BOTTOM)


 # here we creat label of count of letter
count_label_result = Label(window,bg="#0DA154",fg="black",font=("arial",12,"bold"))
count_label_result.place(x=120,y=390)
count_label2_result = Label(window,text="Count Of Letter :")
count_label2_result.place(x=10,y=390)



def prossece_button_click():

    # Get the content from the input box or result box 
    if result_text_area.get("1.0", "end-1c") == "":
    
        content = text_area.get("1.0", "end-1c")
    
    else:
    
        content = result_text_area.get("1.0", "end-1c")

    
    # Get the selected values from check buttons
    remove_spaces_checked = var1.get()
    remove_libraries_checked = var2.get()
    remove_single_line_comments_checked = var3.get()
    remove_multi_line_comments_checked = var4.get()
    remove_all_what_mentioned_before_checked = var5.get()



    # here we set the content to an other var
    processed_content = content

    # here we call the function from class based on selected check buttons
    # here we call the remove whitespases function
    if remove_spaces_checked:
        processed_content = functions.remove_whitespace(processed_content)

    # here we call the remove libraries function
    if remove_libraries_checked:
        processed_content = functions.remove_libraries(processed_content)

    # here we call the remove sigle line comments function
    if remove_single_line_comments_checked:
        processed_content = functions.remove_single_line_comments(processed_content)
    # here we call the remove multi line comments function 
    if remove_multi_line_comments_checked:
        processed_content = functions.remove_multi_line_comments(processed_content)
    # here we call all the  functions
    if remove_all_what_mentioned_before_checked:
        processed_content = functions.remove_multi_line_comments(processed_content)
        processed_content = functions.remove_single_line_comments(processed_content)
        processed_content = functions.remove_whitespace(processed_content)
        processed_content = functions.remove_whitespace(processed_content)

    # Display the result in the result_text_area
    # delet the old text if it found
    result_text_area.delete("1.0", "end")
    # inser new content to result text area
    result_text_area.insert("1.0", processed_content)

    # here we just display the count of letter
    count_label_result.config(text=len(result_text_area.get('1.0', 'end-1c')))    



# here the function of save button to save the prosseced file text
def save_file():

    # here we get the prosseced text from result text area
    prosseced_text = result_text_area.get("1.0", "end-1c")

    # here we call the function to get file dialog of pc and ask us to save file and we set the defualt extintion to save it .txt
    save_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    # here we open file in write mode
    with open(save_file_path, "w") as saved_file:
       # herer we write the content to the file
        saved_file.write(prosseced_text)
  

#here the function of import button to get file from pc to prossec it
def file_dialoge_open():
    # here we call the built in function to file dialog that ask us to select file 
     file_path = filedialog.askopenfilename()
     # here we open file in read mode
     with open(file_path, 'r') as selected_file:
            # here we read file
            content = selected_file.read()

            #here we delet the file path box if its found text 
            file_path_box.delete(0, END)
            # here we inset the select file path to file path box
            file_path_box.insert(0, file_path)
            # her we delet the text area if it  found text
            text_area.delete('1.0', END)
            # here we inset the selected file content to text area
            text_area.insert('1.0', content)

            # here we just display the count of letter
            count_label_import.config(text=len(text_area.get('1.0', 'end-1c')))


# here the function of exit button
def exit_button_function() : 
    # here just end the run or get out of windos
    window.quit()            
    
# here we display the window until we close it by self
window.mainloop()




