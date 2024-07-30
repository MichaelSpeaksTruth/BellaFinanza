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
colon = ":"
hypen = "-"


## [ FUNCTIONS ]


## Function for Processing
def animate_processing():
    print("\n\n")
    dots = ['.   ', '..  ', '... ', '....', '.....','......','.......','........']
    for i in range(4):  # Loop through the animation frames
        sys.stdout.write('\rProcessing' + dots[i % len(dots)])
        sys.stdout.flush()
        time.sleep(0.8)  # Pause for half a second
    print("\n\n")


## Function for 5 Line Space
def fiven():
    print("\n\n\n")

## Function for Wrong entry
def menu_invalid_entry(init_input,input_list):
    while True:
        if init_input not in input_list:
            print("!! Error !!")
            init_input = input("Enter Menu Value. : ")
        else:
            init_input = int(init_input)
            break

##Function for new folder
def new_folder(new_folder_name):
    new_folder_path = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name
    os.mkdir(new_folder_path)

    path_balance  = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name
    path_bank     = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name
    path_debt     = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name
    path_expense  = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name
    path_transac  = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name

    filename_balance = "balance"+".csv"
    filename_bank = "bank"+".csv"
    filename_debt = "debt"+".csv"
    filename_expense = "expense"+".csv"
    filename_transac = "transac"+".csv"

    ## Balance
    with open(os.path.join(path_balance,filename_balance),"w") as fp:
        pass

    new_file_balance = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name + "\\"+filename_balance

    first_row_balance = ["Time","Date","Year","Balance"]

    with open(new_file_balance, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_balance)
        csvfile.close()


    ## Bank
    #with open(os.path.join(path_bank,filename_bank),"w") as fp:
    #    pass

    #new_file_bank = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name + "\\"+filename_bank

    #first_row_bank = []

    #with open(new_file_bank, 'a') as csvfile:
    #    csvwriter = writer(csvfile, lineterminator='\n')
    #    csvwriter.writerow(first_row_bank)
    #    csvfile.close()

    ## Debt
    with open(os.path.join(path_debt,filename_debt),"w") as fp:
        pass

    new_file_debt = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name + "\\"+filename_debt

    first_row_debt = ["Time","Date","Year","Debts","Category","Note" ]

    with open(new_file_debt, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_debt)
        csvfile.close()

    ## Expense
    with open(os.path.join(path_expense,filename_expense),"w") as fp:
        pass

    new_file_expense = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name + "\\"+filename_expense

    first_row_expense = ["Time","Date","Year","Expenses","Note"]

    with open(new_file_expense, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_expense)
        csvfile.close()


    ## Transaction
    with open(os.path.join(path_transac,filename_transac),"w") as fp:
        pass

    new_file_transac = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name + "\\"+filename_transac

    first_row_transac = ["Time","Date","Year","Transactions","Category"]

    with open(new_file_transac, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_transac)
        csvfile.close()



##Function for new csv file




##Function for ENCRYPTION
def encrypt(xw):

    new_passwd = ""
    vacant_list = []
    vacant_list = list(xw)
    alpha_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    alpha_encrypt_c = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L', 'M']
    alpha_encrypt_s = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l', 'm']
    num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_encrypt = ["6", "7", "8", "9", "0", "1", "2", "3", "4", "5"]

    for i in vacant_list:
        if i in alpha_caps:
            indx = alpha_caps.index(i)
            new_passwd += alpha_encrypt_c[indx]
            x = new_passwd
        elif i in alpha_small:
            indx = alpha_small.index(i)
            new_passwd += alpha_encrypt_s[indx]
            x = new_passwd
        elif i in num_list:
            indx = num_list.index(i)
            new_passwd += num_encrypt[indx]
            x = new_passwd
        else:
            new_passwd += i
            x = new_passwd

    return new_passwd

def decrypt(x):
    true_passwd = ''
    vacant_list = []
    vacant_list = list(x)
    alpha_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    alpha_encrypt_c = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L', 'M']
    alpha_encrypt_s = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l', 'm']
    num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_encrypt = ["6", "7", "8", "9", "0", "1", "2", "3", "4", "5"]

    for i in vacant_list:
        if i in alpha_encrypt_c:
            indx = alpha_encrypt_c.index(i)
            true_passwd += alpha_caps[indx]
        elif i in alpha_encrypt_s:
            indx = alpha_encrypt_s.index(i)
            true_passwd +=alpha_small[indx]
        elif i in num_encrypt:
            indx = num_encrypt.index(i)
            true_passwd+=num_list[indx]
        else:
            true_passwd+=i

    return true_passwd



##  [ MAIN PROGRAM ] Starts Here,

# Suggestion : Add name of the user also
print("\n\n")
print(" Welcome to Bella-Finanza ")
print("\n\n")
animate_processing()

## LOGIN & Sign-Up,



print("1. Login \n\n2. Signup\n")
input_list = ['1','2']
# 1. LOGIN
# 2. Signup


init_input = input("Enter Menu Value. : ")
animate_processing()
while True:
    if init_input not in input_list:
        print("!! Error !!")
        init_input = input("Enter Menu Value. : ")
    else:
        init_input = int(init_input)
        break


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
        user_password = str(user_password)
        user_password = encrypt(user_password)
        local_signup_list.append(user_password)

        print("Encrypting your Password...")
        time.sleep(0.2)

    else:
        user_password = "*****"
        user_password = str(user_password)
        user_password = encrypt(user_password)
        local_signup_list.append(user_password)


    with open(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv","a") as csvfile:
        csvwriter = writer(csvfile,lineterminator = "\n")
        csvwriter.writerow(local_signup_list)
        csvfile.close()

    df= pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")


    # creating a file for newly registered members.
    path = (r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server")
    member_id_extracted= df["tag"][((len(df))-1)]
    filename = member_id_extracted

    # Password Extractor
    password = str(df["password"][((len(df))-1)])
    password = decrypt(password)
    # Creates a new folder as per the user
    new_folder(filename)


##Previous Method is now discarded
    #with open(os.path.join(path,filename),"w") as fp:
    #    pass
    ##new_file = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server" + "\\"+filename
    ##first_row = ["Work","Time","Date","Year","E.Time"]
    #with open(new_file, 'a') as csvfile:
    #    csvwriter = writer(csvfile, lineterminator='\n')
    #    csvwriter.writerow(first_row)
    #    csvfile.close()



##Processing Animation
    animate_processing()




    if secured in protection_list_yes:
        print("Your credentials are as follows. : -\n", "USERNAME : ", username_input, "\n", "Password : ", password)
    else:
        print("Your credentials are as follows. : -\n", "USERNAME : ", username_input, "\n", "Password Protection  :  Off \n\n", )

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
    #new_file = r"D:\Rt-Ant\Server"+"\\"+finame+ ".csv"

    ##Security Status
    sec_status = df["secured"][password_value]


    ##Password Verification
    if sec_status in protection_list_yes:
        user_password_input = str(input("Enter your password : "))  # secured
        #print("Entered Password (pending for verification): ",user_password_input ) #To Be Deleted
        df = pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\signup.csv")
        user_passwd = df["password"][password_value]
        #print("Extracted Password ( Encrypted password) : ",user_passwd) #To Be Deleted
        user_passwd = decrypt(user_passwd)
        #print("Extracted Password ( Decrypted password) : ", user_passwd)  # To Be Deleted

        while True:
            if user_password_input != user_passwd:
                print("!! Incorrect Password !!")
                #print(user_password_input," NOT EQUAL TO ",user_passwd)  # To Be Deleted
                user_password_input = str(input("Enter your password. : "))
            else:
                break
    else:
        pass



    animate_processing()

    print("\nACCESS GRANTED\n\n")
    #ps(r"D:\Rt-Ant\Server\Sound_effects\welcome.mp3")


## Login Signup System Designing Done. || Date : 28/07/2024 || Time : 2:22 am

    ## Start Program

    while True:
        print("\n\nMenu:",
              "1. Know your Balance",
              "2. Bank Management ",
              "3. Debt Management",
              "4. Add Expense(s)",
              "5. View all Transactions",
              "6. Gains",
              "7. losses",
              "8. Logout",sep="\n\n")
        print("\n")

        entries = ["1", "2", "3", "4", "5", "6","7","8"]  # Valid Entries
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

        if menu_var == "1":
            #print("Finame : ",finame)

            df = pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+finame+"\\"+"balance.csv")
            #print(df)



            if len(df)==0:
                print("No Record Found")
            else:
                current_balance = str(df["Balance"][(len(df) - 1)])

                print("Current Balance = ₹", current_balance)

        elif menu_var=="2":
            print("Later")

        elif menu_var == "3":
            new_file = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server" + "\\" + finame + "\\" + "debt.csv"
            print(" Welcome to Debt Management")
            animate_processing()
            debt_valid_entries = ["1","2","3"]
            print("\n\n1. Take Debt",
                  "2. Re-Pay Debt",
                  "3. View Debt",sep="\n\n")

            input_debt = str(input("\nEnter your choice : "))

            while True:
                if input_debt not in debt_valid_entries:
                    print("\n!! Invalid Entry !!")
                    input_debt = str(input("\n\nEnter your choice : "))
                else:
                    break

            if input_debt == "1":

                debt_carry_forwarder = []

                # Time Detailing
                current_time = datetime.datetime.now()
                dh1 = str(current_time.hour)
                dm1 = str(current_time.minute)

                t1 = (dh1 + colon + dm1)

                #sc1 = (int(dh1) * 60 * 60) + (int(dm1) * 60)

                # Date Detailing
                dd = str(current_time.day)
                dmt = str(current_time.month)

                date = (dd + backslash + dmt)

                # Year Detailing
                dy = str(current_time.year)

                # List Updation

                debt_carry_forwarder.append(date)
                debt_carry_forwarder.append(t1)
                debt_carry_forwarder.append(dy)

                debt = int(input(" Enter Debt Amount : ₹ "))

                debt_carry_forwarder.append(debt)

                debt_category = "Received Debt"
                debt_carry_forwarder.append(debt_category)

                debt_note = str(input(" Enter a Note for Debt : "))

                debt_carry_forwarder.append(debt_note)

                with open(new_file, 'a') as csvfile:
                    csvwriter = writer(csvfile, lineterminator='\n')
                    csvwriter.writerow(debt_carry_forwarder)
                    csvfile.close()

            elif input_debt == "2":

                debt_carry_forwarder = []

                # Time Detailing
                current_time = datetime.datetime.now()
                dh1 = str(current_time.hour)
                dm1 = str(current_time.minute)

                t1 = (dh1 + colon + dm1)

                # sc1 = (int(dh1) * 60 * 60) + (int(dm1) * 60)

                # Date Detailing
                dd = str(current_time.day)
                dmt = str(current_time.month)

                date = (dd + backslash + dmt)

                # Year Detailing
                dy = str(current_time.year)

                # List Updation

                debt_carry_forwarder.append(date)
                debt_carry_forwarder.append(t1)
                debt_carry_forwarder.append(ye)

                debt = int(input(" Enter Re-Pay Debt Amount : ₹ "))

                debt = ((-1)*(debt))

                debt_carry_forwarder.append(debt)

                debt_category = "Re-Paid Debt"
                debt_carry_forwarder.append(debt_category)

                debt_note = str(input(" Enter a Note for Re-Pay Debt : "))

                debt_carry_forwarder.append(debt_note)

                with open(new_file, 'a') as csvfile:
                    csvwriter = writer(csvfile, lineterminator='\n')
                    csvwriter.writerow(debt_carry_forwarder)
                    csvfile.close()



            elif input_debt == "3":

                debt_df = pd.read_csv(r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server" + "\\" + finame + "\\" + "debt.csv")
                debt_amount = 0

                if len(debt_df) == 0:
                    print("\nNo Record Found")
                else:

                    debt_df_list = []

                    for x in range(len(debt_df)):
                        debt_procs_1 = int(debt_df["Debts"][x])
                        debt_df_list.append(debt_procs_1)

                    #print(" Debt list check : ",debt_df_list)

                    for i in debt_df_list:

                        debt_amount += i
                        #print("debt amount check : ₹", debt_amount)  # To Be Deleted

                    print("\nCurrent Debt Amount = ₹", debt_amount)

        elif menu_var == "4":
            pass





        elif menu_var == "5":
            pass





        elif menu_var == "6":
            pass





        elif menu_var == "7":
            pass





        ## Logout

        elif menu_var == "8":  # Logout
            animate_processing()

            # print("After you Logout you'll be exited from this Software")
            print("Logging you out.", end="");
            waiter = input("\nPress any key to continue. ")
            print("\n")
            exit()







