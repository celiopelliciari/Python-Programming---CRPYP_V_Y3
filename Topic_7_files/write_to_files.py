#! /usr/bin/env python3

file_list = ["user_file_dir", "root_file.txt", "user_file.txt"]

for x in file_list:
    try:
        fh = open(x, "a")
        fh.write(f"Appending to the file {x}\n")
        fh.close()
    except PermissionError:
        raise Exception(f"No rights to access the file {x}")
    except IsADirectoryError:
        raise Exception(f"{x} is actually a directory")
    except:
        print(f"An undefined error accessing the file {x}")
    else:
        print(f"Added to the file {x} successfully")
