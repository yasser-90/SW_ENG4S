from mainpro import Scanner
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Scanner Program")
root.geometry("1920x1080")


def browse_file():
    file_path = filedialog.askopenfilename()
    Scanner.path = file_path
    if file_path:
        file_path_label.config(text=file_path)
    open_file(Scanner.path)


def remove_library():
    Scanner.removeLibrary(Scanner.path)
    open_file(Scanner.path)


def remove_comment():
    Scanner.removeComment(Scanner.path)
    open_file(Scanner.path)


def remove_space():
    Scanner.removeSpace(Scanner.path)
    open_file(Scanner.path)


def show_spacial_info():
    info = Scanner.showInformation(Scanner.path)
    spacial_info(info)


def open_file(path):
    if path:
        with open(path, "r") as file:
            file_contents = file.read()
            file_contents_text.delete(1.0, tk.END)
            file_contents_text.insert(tk.END, file_contents)


def spacial_info(dic):
    info_contents_text.delete(1.0, tk.END)
    for info in dic.keys():
        space = ' '
        if len(dic[info]) > 0:
            info_contents_text.insert(tk.END, f'\n{info}:\n')
        for i in range(len(dic[info])):
            info_contents_text.insert(tk.END, f'{dic[info][i]}{space}')


# Create the label for the file path
file_path_label = tk.Label(
    root, text="No file selected", font=("Helvetica", 14), fg="#555555")
file_path_label.pack(pady=20)


browse_button = tk.Button(root, text="Browse", font=(
    "Helvetica", 12), bg="#007bff", fg="#ffffff", command=browse_file)
browse_button.pack(pady=10)


remove_librarybutton = tk.Button(root, text="Remove Library", font=(
    "Helvetica", 12), bg="#28a745", fg="#ffffff", command=remove_library)
remove_librarybutton.pack(pady=10)

remove_comment_button = tk.Button(root, text="Remove Comment", font=(
    "Helvetica", 12), bg="#28a745", fg="#ffffff", command=remove_comment)
remove_comment_button.pack(pady=10)

remove_space_button = tk.Button(root, text="Remove Space", font=(
    "Helvetica", 12), bg="#28a745", fg="#ffffff", command=remove_space)
remove_space_button.pack(pady=10)

show_details_button = tk.Button(root, text="Show Details", font=(
    "Helvetica", 12), bg="#28a745", fg="#ffffff", command=show_spacial_info)
show_details_button.pack(pady=10)


file_name = tk.Label(
    root, text="File", font=("Helvetica", 14), fg="#555555")
file_name.place(x=1200, y=350)

scanner = tk.Label(
    root, text="Scanner", font=("Helvetica", 14), fg="#555555")
scanner.place(x=300, y=350)

# For Display Text
file_contents_text = tk.Text(root, width=80, height=20)
file_contents_text.pack(side=tk.RIGHT, padx=10, pady=10)


info_contents_text = tk.Text(root, width=80, height=20)
info_contents_text.pack(side=tk.LEFT, padx=10, pady=10)


root.mainloop()
