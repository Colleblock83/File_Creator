import os       #OS Module to create files.


header1 = "Welcome to File_CreatorV1!"
middle = header1.center(130)
print(middle)
header2 = "Made by Colleblock83 (\033[33mGithub\033[0m)"
middle2 = header2.center(140)
print(middle2)
print()
#---------------------------------------------------------------------------
#Create functions:
def create_file():
    try:
        with open(created_file_name, "x") as file:
            print(f"{created_file_name} successfully created.")
    except FileExistsError:
        print("File already exists!")

def edit_file_name():
    try:
        os.rename(created_file_name, new_file_name)
        print(f"File-Name changed from {created_file_name} to {new_file_name}.")
    except FileExistsError:
        print("This file already exists!")

def edit_file_container():

    the_whole_fcking_text = input("Please enter the text you want to write into the file: ")
    with open(created_file_name, "w") as file:
        file.write(the_whole_fcking_text)
        print(f"Inhalt wurde erfolgreich in die Datei {created_file_name} geschrieben!")


#---------------------------------------------------------------------------
#Create List:
while True:
    print("What do you want to do?")
    for list in["(\033[33m1\033[0m) Create-File", "(\033[33m2\033[0m) Rename-File", "(\033[33m3\033[0m) Write into the File", "(\033[33m4\033[0m) End the program"]:
        print(list)
    ch1 = input("Option: ")

    if ch1 == "1":
        created_file_name = input("Please enter the File name you want to create (with .txt, .csv or whatever): ")
        create_file()
    elif ch1 == "2":
        ask_to_edit = input("Do you really want to edit the file-name? (yes/no): ").lower()
        if ask_to_edit == "yes":
            new_file_name = input("Please enter the new file name (Example: new_file.txt): ")
            edit_file_name()
        else:
            print("Alright.")
    elif ch1 == "3":
        edit_file_container()
    elif ch1 == "4":
        input("Thanks for using my program. \033[33mGod bless you!\033[0m")
        exit()


