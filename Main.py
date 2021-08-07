from csv import DictWriter
import csv
import os.path
import glob
from datetime import datetime
import random
import sys
sys.path.insert(1, 'D:\Google Drive\Source Code\GitCipher')
from Cipher25514 import Command as Encrypt
#
#   Main File for call
#

Key = 1111111111111111111111111
class inForm(): 
    def Identification(self,Key):
        while True:
            Identity = {
                "First Name": "",
                "First Letter of Last Name": "",
                "Date of Birth": "",
                "Time of Arrival": ""
            }
            print("\tPlease identify yourself: ")
            Identity["First Name"] = Encrypt(f"-run encrypt manual {Key} {str(input('First Name: ')).capitalize()}")[1]
            while True:
                Identity["First Letter of Last Name"] = Encrypt(f"-run encrypt manual {Key} {str(input('First Letter of Last Name: ')).capitalize()[0]}")[1]
                if len(Encrypt(f"-run decrypt manual {Key} {Identity['First Letter of Last Name']}")[1]) == 1:
                    break
                else:
                    Messages.ERROR(0)
            while True:
                Separator.Line(0)
                dateBirth = str(input("In the format Day/Month/Year\nDate of Birth: "))
                tempString = dateBirth.split("/")
                if (len(tempString[0]) == 2) and (len(tempString[1]) == 2) and (len(tempString[2]) == 4):
                    Identity["Date of Birth"] = Encrypt(f"-run encrypt manual {Key} {dateBirth}")[1]
                    break
                else:
                    Messages.ERROR(0)
            choice = str(input(f"""Are you satisfied with the data collected:
----------------------------
            First Name: {Encrypt(f"-run decrypt manual {Key} {Identity['First Name']}")[1]}
            First Letter of your last name: {Encrypt(f"-run decrypt manual {Key} {Identity['First Letter of Last Name']}")[1]}
            Date of Birth: {Encrypt(f"-run decrypt manual {Key} {Identity['Date of Birth']}")[1]}
----------------------------
Type 'confirm' to accept this information: """))
            if choice == 'confirm':
                break
            else:
                pass
        Identity["Time of Arrival"] = Encrypt(f"-run encrypt manual {Key} {datetime.today().strftime('%H:%M')}")[1]
        return Identity

class inFile(): 
    def Register(self,Identity):
        csv_columns = ['First Name','First Letter of Last Name','Date of Birth','Time of Arrival']
        Noise = 0
        if ((os.path.exists('Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d'))) == True)):
            with open('Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d')), mode='r',encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if (row[0] == Identity['First Name']) and (row[1] == Identity['First Letter of Last Name']):
                        Noise = 1
                    else:
                        pass
            if not(Noise == 1):
                with open('Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d')),'a+', newline='',encoding="utf-8") as write_obj:
                    dict_writer = DictWriter(write_obj, fieldnames=csv_columns)
                    dict_writer.writerow(Identity)
            else:
                Messages.registerError(0)
        else:
            with open('Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d')),'a+', newline='',encoding="utf-8") as write_obj:
                dict_writer = DictWriter(write_obj, fieldnames=csv_columns)
                dict_writer.writeheader()
                dict_writer.writerow(Identity)
        print("You've Registered!")

    def employeeRegister(self):
        mylist = [f for f in glob.glob("Database/*.csv")]
        choiceList = []
        counter = 0
        while not(len(mylist) == counter):     
            string = (mylist[counter]).split("\\")
            stringTwo = string[(len(string))-1]
            stringThree = stringTwo.split(".")
            print(str(counter + 1) + ". " + stringThree[0])
            choiceList.append(stringTwo)
            counter += 1
        choice = int(input("Which date would you like to lookup: "))
        separator = ', '
        print((choiceList[(choice)-1]))
        tempList = []
        counter = 0
        with open(('Database/' + choiceList[(choice)-1]), mode='r',encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    print("")
                    Separator.Line(0)
                    if not(counter == 0):
                        print(f"{counter}", end =" | ")
                        for x in row:
                            print(Encrypt(f"-run decrypt manual {Key} {x}")[1], end =" | ")
                    else:
                        print("\n")
                        print(separator.join(row))
                    tempList.append(separator.join(row))
                    counter += 1
                print("\n")
                Separator.Line(0)

            
class Messages():
    def ERROR(self):
        print("""--------------------
- Error with Input -
--------------------""")
    def registerError(self):
        print("""----------------------------
-You are already registered-
----------------------------""")
    def invalidFile(self):
        print("""--------------
-Invalid File-
--------------""")
class Separator():
    def Line(self):
        print("----------------------------")
        
def Menu(Key):
    Identity = inForm.Identification(0,Key)
    Separator.Line(0)
    print("\tWelcome {} {}".format(Encrypt(f"-run decrypt manual {Key} {Identity['First Name']}")[1],Encrypt(f"-run decrypt manual {Key} {Identity['First Letter of Last Name']}")[1]))
    while True:

        Separator.Line(0)
        choice = int(input("""\tMenu:
        1. Employee Logs
        2. Register yourself
        3. Logout
        4. Quit
        What option do you pick: """))
        Separator.Line(0)
        if choice == 1:
            inFile.employeeRegister(0)
        elif choice == 2:
            inFile.Register(0,Identity)
        elif choice == 3:
            Identity = inForm.Identification(0)
        elif choice == 4:
            break
        else:
            Messages.ERROR(0)
            pass
Menu(Key)
