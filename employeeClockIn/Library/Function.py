from csv import DictWriter
import csv
import os.path
import System
import glob
from datetime import datetime
class inForm(): #   
#
#   Function to login identification data
#
    def Identification():
        while True:
            Identity = {
                "First Name": "",
                "First Letter of Last Name": "",
                "Date of Birth": "",
                "Time of Arrival": ""
            }
            print("\tPlease identify yourself: ")
            Identity["First Name"] = str(input("\tFirst Name: "))
            Identity["First Letter of Last Name"] = str(input("\tFirst Letter of Last Name: "))
            Identity["Date of Birth"] = str(input("\tIn the format Day/Month/Year\n\tDate of Birth: "))
            choice = str(input("""Are you satisfied with the data collected:
----------------------------
            First Name: {}
            First Letter of your last name: {}
            Date of Birth: {}
----------------------------
Type 'confirm' to accept this information: """.format(Identity['First Name'],Identity['First Letter of Last Name'],Identity['Date of Birth'])))
            if choice == 'confirm':
                break
            else:
                pass
        Identity["Time of Arrival"] = datetime.today().strftime('%Y-%m-%d-%H:%M')
        return Identity

class inFile(): #   Functions which include import csv
#
#   Register Identity to csv
#
    def Register(Identity):
        csv_columns = ['First Name','First Letter of Last Name','Date of Birth','Time of Arrival']
        Noise = 0
        if ((os.path.exists('../employeeClockIn/Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d'))) == True)):
            with open('../employeeClockIn/Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d')), mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if (row[0] == Identity['First Name']) and (row[1] == Identity['First Letter of Last Name']):
                        Noise = 1
                    else:
                        pass
            if not(Noise == 1):
                with open('../employeeClockIn/Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d')),'a+', newline='') as write_obj:
                    dict_writer = DictWriter(write_obj, fieldnames=csv_columns)
                    dict_writer.writerow(Identity)
            else:
                System.Messages.registerError()
        else:
            with open('../employeeClockIn/Database/{}.csv'.format(datetime.today().strftime('%Y-%m-%d')),'a+', newline='') as write_obj:
                dict_writer = DictWriter(write_obj, fieldnames=csv_columns)
                dict_writer.writeheader()
                dict_writer.writerow(Identity)
#
#   Employee lookup
#
    def employeeRegister():
        mylist = [f for f in glob.glob("../employeeClockIn/Database/*.csv")]
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
        try:
            separator = ', '
            print((choiceList[(choice)-1]))
            tempList = []
            counter = 0
            with open(('../employeeClockIn/Database/' + choiceList[(choice)-1]), mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        System.Separator.Line()
                        print(str(counter) + ". " + separator.join(row))
                        tempList.append(separator.join(row))
                    System.Separator.Line()
        except:
            System.Messages.invalidFile()