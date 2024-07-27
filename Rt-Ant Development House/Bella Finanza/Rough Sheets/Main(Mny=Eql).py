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
import playsound as pd

print("")
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
    print("\n\n\n\n\n")

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

print(" Welcome to Bella-Finanza ")
fiven()
animate_processing()

## LOGIN & Sign-Up,



print("1. Login \n\n2. Signup\n")
list = ["1","2"]
# 1. LOGIN
# 2. Signup


init_input = input("Enter Menu Value. : ")
animate_processing()
invalid_entry(init_input)

x = (input("Press Enter to exit"))

if init_input == 2:
    local_signup_list = []

    ct = datetime.datetime.now()
    date = str(ct.date())

    df=pd.read_csv(r"D:\Delvitide\Rt-Ant Development House\Bella Finanza\Server\signup data.csv")

    df_str =str(len(df)+1)

    member_id = str(date + "-" + df_str)

    local_signup_list.append(member_id)

    users_name = input("Enter Your Name. :")
    local_signup_list.append(users_name)

    purpose_of_usage: str  = str(input("Purpose of Usage :"))
    local_signup_list.append(purpose_of_usage)

    user_aeg = int(input("Enter Your Age . :"))
    if user_aeg <= 5:
            print("Hey Kid, Apply to this Software",(5-user_aeg),"Years later","You Kiddo.")
            exit()
    else:
        local_signup_list.append(user_aeg)

    user_password = str(input("Create your password. :"))
    local_signup_list.append(user_password)


    with open(r"D:\Rt-Ant\Server\signup data.csv","a") as csvfile:
        csvwriter = writer(csvfile,lineterminator = "\n")
        csvwriter.writerow(local_signup_list)
        csvfile.close()

    df= pd.read_csv(r"D:\Rt-Ant\Server\signup data.csv")


    # creating a csv file for newly registered members.
    path = (r"D:\Rt-Ant\Server")
    member_id_extracted= df["Member_id"][((len(df))-1)]
    filename = member_id_extracted+".csv"

    # Password Extractor
    password = str(df["Password"][((len(df))-1)])

    with open(os.path.join(path,filename),"w") as fp:
        pass

    new_file = r"D:\Rt-Ant\Server" + "\\"+filename

    first_row = ["Work","Time","Date","Year","E.Time"]


    with open(new_file, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row)
        csvfile.close()

    print("\nProcessing your Data",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".")
    print("You are being exited, Please restart the software.\n")


    print("Your credentials are as follows. : -\n","Member ID : ",member_id_extracted,"\n","Password  : ",password)




    waiter = input("\nPress any key to continue. ")
    print("\n")
    exit()



elif init_input ==1 : # Login

    df = pd.read_csv(
        r"D:\Rt-Ant\Server\signup data.csv")

    member_id_list = [df["Member_id"][x] for x in range(len(df))]

    member_id_input = str(input("Enter Member ID . :"))

    while True:
        if member_id_input not in member_id_list:
            print("!! Incorrect Username.")
            member_id_input = str(input("Enter Member ID . :"))
        else:
            break



    #Preparing Path
    new_file = r"D:\Rt-Ant\Server"+"\\"+member_id_input+ ".csv"


    for i in range(len(member_id_list)):
        if member_id_list[i]==member_id_input:
                password_value = i
        else:
            pass


    user_password_input = str(input("Enter your password. :")) #secured
    df = pd.read_csv(r"D:\Rt-Ant\Server\signup data.csv")
    while True:
            if user_password_input != df["Password"][password_value]:
                print("!! Incorrect Password !!")
                user_password_input = str(input("Enter your password. :"))
            else:
                break

    print("\n\nProcessing",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".")

    print("\nACCESS GRANTED\n\n")
    ps(r"D:\Rt-Ant\Server\Sound_effects\welcome.mp3")



