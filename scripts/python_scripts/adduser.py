#! /usr/bin/python3 
#Purpose: Create User and Group
#Version: 
#Created Date: Tue Jan 24 07:05:41 2023
#Modified Date: 
#Author: JAHIR RAIHAN
# Start # 
###################################### 

import os

users = ["alpha","beta","gamma"]

print("Adding users to system")
print("##############################")

# Loop to add users frim userlist

for user in users:
   exitcode = os.system("id {} ".format(user))
   if exitcode != 0:
       print("User{} does not exist. Adding it.\n".format(user))
       print("###########################\n")
       os.system("useradd {}".format(user))
   else:
       print("User already exist, skipping it\n")
       print("###########################\n")


# Check if group exist or not



exitcode = os.system("grep science /etc/group")

if exitcode != 0:
    print("Group science does not exist. Adding it. \n")

    print("###########################\n")
    os.system("groupadd science")
else:
    print("Group already exist, skipping it.")

    print("###########################\n")

print("Adding Users in group\n")
print("###########################\n")

for user in users:
    print("Adding user {} in the science group\n".format(user))

    print("###########################\n")
    os.system("usermod -G science {}".format(user))



###################################### 
# End # 
                      
