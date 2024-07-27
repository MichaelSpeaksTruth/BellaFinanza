# Modules
import time
import sys
import random
from threading import Timer
import time
import datetime
import pandas as pd
import csv
from csv import writer
from csv import reader
import os
import playsound as ps


## Predefined List
protection_list_yes = ['Y', 'y','YES', 'yes','Yes']
protection_list_no = ['N', 'n', 'NO','no','No']


## [ VARIABLES ]

today_count = 0
backslash = "/"

## [ FUNCTIONS ]


## Function for Processing
def animate_processing():
    dots = ['.   ', '..  ', '... ', '....', '.....','......','.......','........']
    for i in range(4):  # Loop through the animation frames
        sys.stdout.write('\rProcessing' + dots[i % len(dots)])
        sys.stdout.flush()
        time.sleep(0.8)  # Pause for half a second
    print("\n\n\n")


## Function for 5 Line Space
def fiven():
    print("\n\n\n")

## Function for Wrong entry


def invalid_entry(init_input):
    while True:
        if init_input not in list:
            print("!! Error !!")
            init_input = input("Enter Menu Value. : ")
        else:
            init_input = int(init_input)
            break



##  [ MAIN PROGRAM ] Starts Here,

# Suggestion : Add name of the user also
print("\n\n")
print(" Welcome to Bella-Finanza ")
print("\n\n")
animate_processing()

## LOGIN & Sign-Up,



print("1. Login \n\n2. Signup\n")
list = [1,2]
# 1. LOGIN
# 2. Signup


init_input = int(input("Enter Menu Value. : "))
animate_processing()
invalid_entry(init_input)


if init_input == 2:
    local_signup_list = []

    ct = datetime.datetime.now()
    date = str(ct.date())

    df=pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")

    df_str =str(len(df)+1)

    member_id = str(date + "-" + df_str)

    local_signup_list.append(member_id)

## [ Security Y/N ]
    print(" Do    want    to    enable    PASSWORD    protection    for    your    account    ? ")
    time.sleep(0.9)
    fiven()
    protection_list =['Y','y','N','n','NO','YES','yes','no','Yes','No']

    secured = input("Enter 'Y' for YES or 'N' for NO   :   ")

    while True:
        if secured not in protection_list:
            animate_processing()
            print("!! Error !!")
            secured = input("Enter 'Y' for YES or 'N' for NO")
        else:
            local_signup_list.append(secured)
            break




## USERNAME

    df = pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")

    username_list = [df["username"][x] for x in range(len(df))]

    username_input = str(input("Enter the username of your choice : "))

    while True:
        if username_input in username_list:
            print("!! Username already taken !!")
            username_input = str(input("Enter the username of your choice : "))
        else:
            break

    local_signup_list.append(username_input)


## PASSWORD

    protection_list_yes = ['Y', 'y','YES', 'yes','Yes']
    #protection_list_no = ['N', 'n', 'NO','no','No']

    if secured in protection_list_yes:
        user_password = str(input("Create your password. : "))
        local_signup_list.append(user_password)
    else:
        user_password = "*****"
        local_signup_list.append(user_password)


    with open(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv","a") as csvfile:
        csvwriter = writer(csvfile,lineterminator = "\n")
        csvwriter.writerow(local_signup_list)
        csvfile.close()

    df= pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")


    # creating a csv file for newly registered members.
    path = (r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server")
    member_id_extracted= df["tag"][((len(df))-1)]
    filename = member_id_extracted+".csv"

    # Password Extractor
    password = str(df["password"][((len(df))-1)])

    with open(os.path.join(path,filename),"w") as fp:
        pass

    new_file = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server" + "\\"+filename

    first_row = ["Work","Time","Date","Year","E.Time"]


    with open(new_file, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row)
        csvfile.close()

    animate_processing()




    if secured in protection_list_yes:
        print("Your credentials are as follows. : -\n", "USERNAME : ", username_input, "\n", "Password  : ", password)
    else:
        print("Your credentials are as follows. : -\n", "USERNAME : ", username_input, "\n", "Password Protection  :  Off ", )

    print("You are being exited, Please restart the software and login using your credentials.\n")


    waiter = input("\nPress any key to continue. ")
    print("\n")
    exit()



elif init_input ==1 : # Login

    df = pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")

    username_list = [df["username"][x] for x in range(len(df))]

    username_input = str(input("Enter your USERNAME : "))

    while True:
        if username_input not in username_list:
            print("!! Incorrect Username.")
            username_input = str(input("Enter your correct USERNAME : "))
        else:
            break

    for i in range(len(username_list)):
        if username_list[i]==username_input:
                password_value = i
        else:
            pass

    #Preparing Path

    finame = df["tag"][password_value]
    new_file = r"D:\Rt-Ant\Server"+"\\"+finame+ ".csv"

    ##Security Status
    sec_status = df["secured"][password_value]


    ##Password Verification
    if sec_status in protection_list_yes:
        user_password_input = str(input("Enter your password. : "))  # secured
        df = pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")
        while True:
            if user_password_input != df["password"][password_value]:
                print("!! Incorrect Password !!")
                user_password_input = str(input("Enter your password. : "))
            else:
                break
    else:
        pass



    animate_processing()

    print("\nACCESS GRANTED\n\n")
    #ps(r"D:\Rt-Ant\Server\Sound_effects\welcome.mp3")


## Login Signup System Designing Done. || Date : 28/07/2024 || Time : 2:22 am




