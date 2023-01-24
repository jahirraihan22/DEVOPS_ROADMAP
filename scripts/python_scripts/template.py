#! /usr/bin/python3
import os
import datetime
print("Please provide filename you want to create: ")

file = input()
if os.path.isfile(file+".py"):
    print("File already exists, try another: ")
    file = input()

file = file+".py"
file = open(file, "a")
file.write("#! /usr/bin/python3 \n")
file.write("#Purpose: \n")
file.write("#Version: \n")
file.write("#Created Date: "+ datetime.datetime.now().strftime("%c") +"\n")
file.write("#Modified Date: \n")
file.write("#Author: "+ os.getlogin().upper() +"\n")
file.write("# Start # \n")
file.write("###################################### \n")
file.write("\n")


file.write("\n")
file.write("###################################### \n" )
file.write("# End # \n" )
file.close()
