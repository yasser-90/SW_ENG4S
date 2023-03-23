from mainpro import remove_comments
file_contents = remove_comments("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest.cpp")
#print(file_contents)
with open("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp", "w") as f:
    f.write(file_contents)

from mainpro import remove_calls
file_contents = remove_calls("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp")
with open("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp", "w") as f:
    f.write(file_contents)

from mainpro import remove_whitespace
content = remove_whitespace("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp")
with open("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp", "w+") as f:
    f.write(file_contents)
    f.write(content)

from mainpro import copmression
content = copmression("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp")
with open("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest4.cpp", "w") as f:
    f.write(content)

from mainpro import change
new_content = change("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp")
with open("C:\\Users\\zubaida\\Desktop\\SW_ENG4S-main\\SW_ENG4S\\facttest3.cpp", "w") as f:
    f.write(new_content)





