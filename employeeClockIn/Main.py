import sys
sys.path.insert(1, '../employeeClockIn/Library')
from Library import Function
from Library import System
#
#   Main File for call
#
def Menu():
    Identity = Function.inForm.Identification()
    System.Separator.Line()
    print("\tWelcome {} {}".format(Identity['First Name'],Identity['First Letter of Last Name']))
    while True:
        try:
            System.Separator.Line()
            choice = int(input("""\tMenu:
            1. Registered Employees Today
            2. Register yourself
            3. Logout
            4. Quit
            What option do you pick: """))
            System.Separator.Line()
            if choice == 1:
                Function.inFile.employeeRegister()
            elif choice == 2:
                Function.inFile.Register(Identity)
            elif choice == 3:
                Identity = Function.inForm.Identification()
            elif choice == 4:
                break
            else:
                System.Messages.ERROR()
                pass
        except:
            pass

Menu()
