print("Welcome to Rt-Ant, Your productivity is our priority")
# Module Needed
import random
from threading import Timer
import time
import datetime
import pandas as pd
import csv
from csv import writer
from csv import reader
import os
from playsound import playsound as ps

print("")

#Variable
today_count = 0
backslash = "/"

print("1. Login \n\n2. Signup\n")
list = ["1","2"]
# 1. LOGIN
# 2. Signup
print("")

init_input = input("Enter Menu Value. : ")
while True:
    if init_input not in list:
        print("!! Error !!")
        init_input = input("Enter Menu Value. : ")
    else:
        init_input = int(init_input)
        break


if init_input == 2:
    local_signup_list = []

    ct = datetime.datetime.now()
    date = str(ct.date())

    df=pd.read_csv(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects"
                   r"\pythonProject\SERVER -  Helpers High\signup data.csv")

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


    with open(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\signup data.csv","a") as csvfile:
        csvwriter = writer(csvfile,lineterminator = "\n")
        csvwriter.writerow(local_signup_list)
        csvfile.close()

    df= pd.read_csv(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\signup data.csv")


    # creating a csv file for newly registered members.
    path = (r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High")
    member_id_extracted= df["Member_id"][((len(df))-1)]
    filename = member_id_extracted+".csv"

    # Password Extractor
    password = str(df["Password"][((len(df))-1)])

    with open(os.path.join(path,filename),"w") as fp:
        pass

    new_file = r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High" + "\\"+filename

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
        r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\signup data.csv")

    member_id_list = [df["Member_id"][x] for x in range(len(df))]

    member_id_input = str(input("Enter Member ID . :"))

    while True:
        if member_id_input not in member_id_list:
            print("!! Incorrect Username.")
            member_id_input = str(input("Enter Member ID . :"))
        else:
            break



    #Preparing Path
    new_file = r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High"+"\\"+member_id_input+ ".csv"


    for i in range(len(member_id_list)):
        if member_id_list[i]==member_id_input:
                password_value = i
        else:
            pass


    user_password_input = str(input("Enter your password. :")) #secured
    df = pd.read_csv(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\signup data.csv")
    while True:
            if user_password_input != df["Password"][password_value]:
                print("!! Incorrect Password !!")
                user_password_input = str(input("Enter your password. :"))
            else:
                break

    print("\n\nProcessing",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".",end="");time.sleep(2);print(".")

    print("\nACCESS GRANTED\n\n")
    ps(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\welcome.mp3")


    while True:
        print("Menu:",
              "1. Commit",
              "2. View commit count(today) ",
              "3. View commit count(all-time) ",
              "4. Edit counter submission",
              "5. View Total Counter Submissions (in csv format)",
              "6. Logout",
              "Break - Enter *break* to take it",sep="\n\n")
        print("\n")

        entries = ["1", "2", "3", "4", "5", "6", "7","B","b","11","Break","break"]  # Currently 4 is not available
        menu_var = input("Select your Task. : ")
        menu_var = str(menu_var)
        while True:
            if menu_var not in entries:
                print("!! Error !!")
                menu_var = input("Enter : ")
            else:
                break
        print("\n")
        menu_var = str(menu_var)

        if menu_var == "1":  # For Menu value 1

            hcount = []

            # Helpers count
            h_var = input("Enter here = ")  # H-Count Cursor
            ps(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\beep.mp3")
            # Characters Needed
            colon = ":"
            hypen = "-"
            backslash = "/"

            # Time Detailing
            current_time = datetime.datetime.now()
            dh1 = str(current_time.hour)
            dm1 = str(current_time.minute)

            t1 = (dh1 + colon + dm1)

            sc1 = (int(dh1)*60*60)+(int(dm1)*60)


            # Date Detailing
            dd = str(current_time.day)
            dmt = str(current_time.month)

            date = (dd + backslash + dmt)

            # Year Detailing
            dy = str(current_time.year)

            # List Updation
            hcount.append(h_var)
            hcount.append(t1)
            hcount.append(date)
            hcount.append(dy)

            # print(pd.read_csv(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\Future Devlopment\helpers high.csv"))
            #ps(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\beep.mp3")
            print("\n\nSuccess waiting, Ahead")



            #Saving-Duration
            waiter = input("\n Press s to save the commit : ")

            while True:
                if waiter not in "sS":
                    print("!! Error !!\n")
                    waiter = input("\n Press s to save the commit : ")
                else:
                    break

            while True:
                if waiter == "s" or waiter == "S":
                    current_time = datetime.datetime.now()
                    dh2 = str(current_time.hour)
                    dm2 = str(current_time.minute)

                    t2 = (dh2 + colon + dm2)
                    sc2 = (int(dh2) * 60 * 60) + (int(dm2) * 60)


                    #com_duration = ((sc2//600)-(sc1/3600))
                    # List Updation

                    hcount.append(t2)
                    #hcount.append(com_duration)


                    with open(new_file, 'a') as csvfile:
                        csvwriter = writer(csvfile, lineterminator='\n')
                        csvwriter.writerow(hcount)
                        csvfile.close()
                    break
                else:
                    waiter = input("\n Press s to save the commit")
            ps(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\beep.mp3")


            waiter = input("\nPress Enter to exit menu.")
            print("\n")

        elif menu_var == "2":

            df = pd.read_csv(
                new_file)

            ct = datetime.datetime.now()
            d = ct.day
            m = ct.month
            d, m = str(d), str(m)
            date = (d + backslash + m)

            # print("Work", "|", "Time", " |", "Date", "|", "Year")
            for i in range(len(df.values)):
                if df["Date"][i] == date:
                    # print("Todays Counter Check : ",i+1)
                    print("Today's Counter Check : ", i + 1, "\n", "Time :", df["Time"][i], "|", "Date : ",
                          df["Date"][i], "|", "Year : ", df["Year"][i], "\n\n")

                else:
                    pass

            waiter = input("Press Enter to exit menu.")
            print("\n")


        elif menu_var == "3":
            df = pd.read_csv(
                new_file)

            # print("H-Count", "|", "Time", " |", "Date", "|", "Year")

            for i in range(len(df.values)):
                print("Counter Check : ", i + 1, "\n", "Work :",df["Work"][i],"|", "Time :", df["Time"][i], "|", "Date : ", df["Date"][i], "|",
                      "Year : ", df["Year"][i], "\n")

            waiter = input("\nPress Enter to exit menu.")
            print("\n")


        elif menu_var == "4":
            print("!! S00RY !!", "We are currently working upon this # # Functionality !!")

            waiter = input("\nPress Enter to exit menu.")
            print("\n")


        elif menu_var == "5":
            df = pd.read_csv(
                new_file)
            df.index = [x for x in range(1, len(df.values) + 1)]
            print(df)
            waiter = input("\nPress Enter to exit menu.")


        elif menu_var =="Break" or menu_var =="break":
            bt = int(input("enter duration(in mins) : "))

            hcount = []

            # Helpers count
            btstr = str(bt)
            h_var = btstr+" Min/Break"  # H-Count Cursor
            ps(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\beep.mp3")
            # Characters Needed
            colon = ":"
            hypen = "-"
            backslash = "/"

            # Time Detailing
            current_time = datetime.datetime.now()
            dh1 = str(current_time.hour)
            dm1 = str(current_time.minute)

            t1 = (dh1 + colon + dm1)

            sc1 = (int(dh1) * 60 * 60) + (int(dm1) * 60)

            # Date Detailing
            dd = str(current_time.day)
            dmt = str(current_time.month)

            date = (dd + backslash + dmt)

            # Year Detailing
            dy = str(current_time.year)

            # List Updation
            hcount.append(h_var)
            hcount.append(t1)
            hcount.append(date)
            hcount.append(dy)

            bt = bt*60
            time.sleep(bt)
            x=rdm_value = random.randint(10863,970329)
            print("Confirmation Code :",rdm_value,"\n\n")

            #Time Constraint
            current_time = datetime.datetime.now()
            dh = int(current_time.hour)
            dm = int(current_time.minute)
            ds1 = int(current_time.second)

            s1 = (dh*60*60) + (dm*60) + (ds1)

            s2 = 0



            while s2-s1<int(14):

                #Time Constraint 2

                current_time = datetime.datetime.now()
                dh = int(current_time.hour)
                dm = int(current_time.minute)
                ds2 = int(current_time.second)

                s2 = (dh * 60 * 60) + (dm * 60) + (ds2)


                ps(r'C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\arabNukes.mp3')

                y = int(input("enter confirmation code : "))
                if y==rdm_value:
                    current_time = datetime.datetime.now()
                    dh2 = str(current_time.hour)
                    dm2 = str(current_time.minute)

                    t2 = (dh2 + colon + dm2)
                    sc2 = (int(dh2) * 60 * 60) + (int(dm2) * 60)

                    # com_duration = ((sc2//600)-(sc1/3600))
                    # List Updation

                    hcount.append(t2)
                    # hcount.append(com_duration)

                    with open(new_file, 'a') as csvfile:
                        csvwriter = writer(csvfile, lineterminator='\n')
                        csvwriter.writerow(hcount)
                        csvfile.close()
                    break
                else:
                    x = rdm_value = random.randint(10863, 970329)
                    print("Confirmation Code :", rdm_value, "\n\n")
                    pass
            ps(r"C:\Users\ANURAG KUMAR VERMA\PycharmProjects\pythonProject\SERVER -  Helpers High\Sound_effects\beep.mp3")

            waiter = input("\nPress Enter to exit menu.")
            print("\n")





        elif menu_var == "6":  # Logout

            # print("After you Logout you'll be exited from this Software")
            print("Logging you out.", end="");
            waiter = input("\nPress any key to continue. ")
            print("\n")
            exit()

        elif menu_var == "7":
            print("Thank You for using this Software, \n"
                  "                                 Come Back SOON...")

            waiter = input("Press Enter to exit.")

            break
