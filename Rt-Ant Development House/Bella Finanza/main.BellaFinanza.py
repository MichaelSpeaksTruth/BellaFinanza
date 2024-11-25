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
#import playsound as ps


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
    new_folder_path = r".\Server"+"\\"+new_folder_name
    os.mkdir(new_folder_path)

    #print("\nCheckpoint 1\n")

    os.system(f'attrib +h "{new_folder_path}"')

    #print("\nCheckpoint 2\n")

    path_balance  = r".\Server"+"\\"+new_folder_name
    path_bank     = r".\Server"+"\\"+new_folder_name
    path_debt     = r".\Server"+"\\"+new_folder_name
    path_expense  = r".\Server"+"\\"+new_folder_name
    path_transac  = r".\Server"+"\\"+new_folder_name

    filename_balance = "balance"+".csv"
    filename_bank = "bank"+".csv"
    filename_debt = "debt"+".csv"
    filename_expense = "expense"+".csv"
    filename_transac = "transac"+".csv"

    ## Balance
    with open(os.path.join(path_balance,filename_balance),"w") as fp:
        pass

    new_file_balance = r".\Server"+"\\"+new_folder_name + "\\"+filename_balance

    first_row_balance = ["Time","Date","Year","Balance"]

    with open(new_file_balance, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_balance)
        csvfile.close()


    ## Bank

    with open(os.path.join(path_bank,filename_bank),"w") as fp:
        pass

    new_file_bank = r".\Server"+"\\"+new_folder_name + "\\"+filename_bank

    first_row_bank = ["Bank" ]

    with open(new_file_bank, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_bank)
        csvfile.close()

    ##Banking Customization Folder


    ## Debt
    with open(os.path.join(path_debt,filename_debt),"w") as fp:
        pass

    new_file_debt = r".\Server"+"\\"+new_folder_name + "\\"+filename_debt

    first_row_debt = ["Time","Date","Year","Debts","Category","Note" ]

    with open(new_file_debt, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_debt)
        csvfile.close()

    ## Expense
    with open(os.path.join(path_expense,filename_expense),"w") as fp:
        pass

    new_file_expense = r".\Server"+"\\"+new_folder_name + "\\"+filename_expense

    first_row_expense = ["Time","Date","Year","Expenses","Note"]

    with open(new_file_expense, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_expense)
        csvfile.close()


    ## Transaction
    with open(os.path.join(path_transac,filename_transac),"w") as fp:
        pass

    new_file_transac = r".\Server"+"\\"+new_folder_name + "\\"+filename_transac

    first_row_transac = ["Time","Date","Year","Transactions","Category"]

    with open(new_file_transac, 'a') as csvfile:
        csvwriter = writer(csvfile, lineterminator='\n')
        csvwriter.writerow(first_row_transac)
        csvfile.close()



##Function for generating Transaction id
#def transac_id():





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
    x = str(x)
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
        print("!! Error !!\n")
        init_input = input("Enter Menu Value. : ")
    else:
        init_input = int(init_input)
        break


if init_input == 2:
    local_signup_list = []

    ct = datetime.datetime.now()
    date = str(ct.date())

    df=pd.read_csv(r".\Server\signup.csv")

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

    df = pd.read_csv(r".\Server\signup.csv")

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


    with open(r".\Server\signup.csv","a") as csvfile:
        csvwriter = writer(csvfile,lineterminator = "\n")
        csvwriter.writerow(local_signup_list)
        csvfile.close()


    df= pd.read_csv(r".\Server\signup.csv")


    # creating a file for newly registered members.
    path = (r".\Server")
    member_id_extracted= df["tag"][((len(df))-1)]
    filename = member_id_extracted

    # Password Extractor
    password = str(df["password"][((len(df))-1)])
    password = decrypt(password)
    # Creates a new folder as per the user
    new_folder(filename)

    #print("\nCheckpoint 3\n")

    new_folder_path_procs_z1 = r".\Server" + "\\" + filename+"\\"+"Bank Management"
    os.mkdir(new_folder_path_procs_z1)



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

    df = pd.read_csv(r".\Server\signup.csv")

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
        df = pd.read_csv(r".\Server\signup.csv")
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

            #df = pd.read_csv(r".\Server"+"\\"+finame+"\\"+"balance.csv")
            #print(df)

            print("AS OF NOW, This function is not available.")

            #if len(df)==0:
            #    print("No Record Found")
            #else:
            #    current_balance = str(df["Balance"][(len(df) - 1)])

            #    print("Current Balance = ₹", current_balance)



        elif menu_var=="2":




            while True:
                print(" Welcome to Bank Management")
                print("\n\n1. My Banking Accounts",
                      "2. Add Banking Account(s)",
                      "3. Exit ", sep="\n\n")

                bank_valid_entries = ["1", "2", "3"]

                input_bank_menu = str(input("\nEnter your choice : "))

                while True:
                    if input_bank_menu not in bank_valid_entries:
                        print("\n!! Invalid Entry !!")
                        input_bank_menu = str(input("\n\nEnter your choice : "))
                    else:
                        break
                if input_bank_menu == "1":
                    bank_df = pd.read_csv(r".\Server" + "\\" + finame + "\\" + "bank.csv")
                    # print(df)

                    if len(bank_df) == 0:
                        print("\nNo Bank Record Found, Please add your Banking Account(s) \n")
                        #print("\n...Testing 27/10/2024/Bank_Management...(1)\n")###

                    else:
                        #print("\n...Testing 27/10/2024/Bank_Management...(2)\n")###
                        animate_processing()
                        print("\n")
                        bank_df_list = []

                        for x in range(len(bank_df)):
                            bank_procs_1 = str(bank_df["Bank"][x])
                            bank_df_list.append(bank_procs_1)

                        print("\n", "Your Banking Account(s) are as below : \n\n", )
                        print("Serial No.       Bank ")
                        for i in range((len(bank_df_list))):
                            print((i + 1), "." + "             ", bank_df_list[i])  ##17
                            bank_procs_2_valid_entries = []
                            bank_procs_2 = (i + 1)
                            bank_procs_2 = str(bank_procs_2)
                            bank_procs_2_valid_entries.append(bank_procs_2)
                        print("\n")

                        bank_procs_3 = str(input("Enter serial no. of the Bank : "))

                        while True:
                            if bank_procs_3 not in bank_procs_2_valid_entries:
                                print("!! Incorrect !!")
                                bank_procs_3 = str(input("Enter serial no. of the Bank : "))
                            else:
                                bank_procs_3 = int(bank_procs_3)
                                bank_procs_4 = str(bank_df_list[(bank_procs_3 - 1)])

                                break

                                ###### DEVELOP an algorithm to open the file of specific bank as requested by the user.  ## Bank Management

                        user_bank_path = r".\Server" + "\\" + finame + "\\" + "Bank Management" + "\\" + bank_procs_4 + ".csv"
                        df_user_bank_records = pd.read_csv(user_bank_path)
                        len_user_bank_records = len(df_user_bank_records)

                        bank_procs_5 = 0
                        for i in range(len_user_bank_records):
                            bank_procs_5 += df_user_bank_records["Amount"][i]

                        latest_bank_balance = bank_procs_5

                        print("Your", bank_procs_4, "account_balance is : ", " ₹ ", bank_procs_5)
                        fiven()
                        print("Bank Records are as folows :- \n\n")

                        bank_procs_3_ext_path = r".\Server" + "\\" + finame + "\\" + "Bank Management" + "\\" + bank_procs_4 + ".csv"

                        df_bank_procs_3_ext_path = pd.read_csv(bank_procs_3_ext_path)

                        if len(df_bank_procs_3_ext_path) == 0:
                            print("!!    No Record Found / No Transaction(s) to show    !!")
                        else:
                            print(
                                "D a t e    ||    Y E A R    ||    T i m e    ||    D / C    ||    Transactions    \n")

                            for i in range(len_user_bank_records):
                                print(df_user_bank_records["Date"][i], "      ", "    ",
                                      df_user_bank_records["Year"][i],
                                      "       ", "     ", df_user_bank_records["Time"][i], "     ", "      ",
                                      df_user_bank_records["Type"][i], "      ", "     ₹ ",
                                      df_user_bank_records["Amount"][i])

                                ## Finished Banking Records display system || 4/08/2024 ||  3:22 A.M  ||  Sunday




                elif input_bank_menu == "2":
                    fiven()
                    print("DISCLAIMER : We don't ask for your bank account number or any other private info(s). ")
                    fiven()

                    bank_df = pd.read_csv(
                        r".\Server" + "\\" + finame + "\\" + "bank.csv")
                    # print(df)

                    if len(bank_df) == 0:
                        print("AS OF NOW",
                              "No Bank Record(s) Found, Please add your Banking Account(s) in the next step.", "",
                              sep="\n")


                    else:
                        animate_processing()
                        print("\n")
                        bank_df_list = []

                        for x in range(len(bank_df)):
                            bank_procs_1 = str(bank_df["Bank"][x])
                            bank_df_list.append(bank_procs_1)

                        print("\n", "Your Banking Account(s) are as below : \n\n", )
                        print("Serial No.       Bank ")
                        for i in ((len(bank_df_list) + 1)):
                            print("(" + (i + 1) + "." + ")" + "             " + bank_df_list[i])  ##1
                        print("if your preferred account is NOT available, Register your BANK.\n")
                        print("\n")

                    print("SUB-MENU (BANKING DEPT.)\n",
                          "1. Register your BANK ACCOUNT ",
                          "2. Exit this sub-menu (Banking Dept.)", sep="\n\n")

                    print("\n\n")

                    bank_valid_entries_procs_2 = ["1", "2"]

                    bank_valid_entries_procs_3 = str(input("Select your Task. : "))
                    while True:
                        if bank_valid_entries_procs_3 not in bank_valid_entries_procs_2:
                            print("!! INVALID Input !!\n\n")
                            bank_valid_entries_procs_3 = str(input("Select your Task. : "))
                        else:
                            break

                    if bank_valid_entries_procs_3 == "1":
                        bank_name = str(input("Enter BANK name : "))

                        bank_name_list = []
                        bank_name_list.append(bank_name)

                        ## Update bank.csv List
                        bank_new_file = r".\Server" + "\\" + finame + "\\" + "bank.csv"
                        with open(bank_new_file, 'a') as csvfile:
                            csvwriter = writer(csvfile, lineterminator='\n')
                            csvwriter.writerow(bank_name_list)
                            csvfile.close()

                        ##Prepare file of specific Bank for user

                        filename_procs_1 = bank_name + ".csv"
                        user_bank_path_procs_1 = r".\Server" + "\\" + finame + "\\" + "Bank Management"

                        with open(os.path.join(user_bank_path_procs_1, filename_procs_1), "w") as fp:
                            pass

                        filename_procs_2 = r".\Server" + "\\" + finame + "\\" + "Bank Management" + "\\" + filename_procs_1

                        first_row_bank_procs_2 = ["Date", "Year", "Time", "Type", "Amount"]

                        with open(filename_procs_2, 'a') as csvfile:
                            csvwriter = writer(csvfile, lineterminator='\n')
                            csvwriter.writerow(first_row_bank_procs_2)
                            csvfile.close()
                    else:
                        ##print("\n...Testing 27/10/2024/Bank_Management...(3)\n")###
                        pass

                elif input_bank_menu == "3":
                    ##print("\n...Testing 27/10/2024/Bank_Management...(4)\n")###
                    break



        ## Finished Bank Management System  || 4/08/2024 ||  5:22 A.M  ||  Sunday



        elif menu_var == "3":
            new_file = r".\Server" + "\\" + finame + "\\" + "debt.csv"
            print(" Welcome to Debt Management")
            animate_processing()
            debt_valid_entries = ["1","2","3","4"]
            print("\n\n1. Take Debt",
                  "2. Re-Pay Debt",
                  "3. View Debt",
                  "4. Exit",sep="\n\n")

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
                debt_carry_forwarder.append(dy)

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

                debt_df = pd.read_csv(r".\Server" + "\\" + finame + "\\" + "debt.csv")
                debt_amount = 0

                if len(debt_df) == 0:
                    print("No Record Found")
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

            elif input_debt == "4":
                pass

        elif menu_var == "4":
            fiven()
            print("\n\nWelcome to Expense Management Dept.")
            fiven()
            print("\n1. Add Expense(s)",
                  "2. Exit",sep="\n\n")
            fiven()

            expense_valid_entries = ["1","2"]
            input_expense = str(input("\nEnter your choice : "))

            while True:
                if input_expense not in expense_valid_entries:
                    print("!! Invalid Entry !!")
                    input_expense = str(input("\nEnter your choice : "))
                else:
                    break

            while input_expense == "1":
                expense_depository = []

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
                expense_depository.append(t1)
                expense_depository.append(date)
                expense_depository.append(dy)

                ##Expenses

                exp_amt = int(input("Enter Expense Amount : ₹ "))
                exp_note = str(input("Enter Note : "))

                ##List Updation
                expense_depository.append(exp_amt)
                expense_depository.append(exp_note)
                fiven()

                print("Do you want to add another expense ?")

                print("Sub-Menu(Expenses) : ","1. Yes","2. No",sep="\n\n")
                print("\n")


                re_entry_expense = str(input("Enter your choice : "))
                print("\n")
                re_entry_expense_list = ["1","2"]

                while True:
                    if re_entry_expense not in re_entry_expense_list:
                        print("!! Invalid Entry !!")
                        re_entry_expense = str(input("Enter your choice : "))
                    else:
                        break

                if re_entry_expense == "1":
                    pass
                else:
                    input_expense = "2"

            if input_expense == "2":
                pass
            else:
                pass

        elif menu_var == "5":
            new_file_transac = r".\Server" + "\\" + finame + "\\" + "transac.csv"
            transac_df = pd.read_csv(new_file_transac)
            len_transac_df = len(transac_df)

            if len_transac_df == 0:
                print("\n\nNo Record Found\n\n")
            else:
                print("T i m e    ||    D a t e    ||    Y e a r    || Category ||    E x p e n s e\n")

                for i in range(len_transac_df):
                    print(transac_df["Time"][i] + "      " + "     " + transac_df["Date"][i] + "     " + "    " + transac_df["Year"][i] + "       " + " "+transac_df["Category"][i] + "     " + "     " + "  ₹ " + transac_df["Transactions"][i])

                x_continue = str(input("\n\nPress Enter to EXIT\n\n"))

            ##### TRANSACTION ID will be of 10 digits.







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







