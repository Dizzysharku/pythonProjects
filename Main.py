import sys
sys.path.insert(1, '../Employee-login-main/Library')
from Library import Function
#
#   Main File for call
#
def Menu():
    Identity = Function.inForm.Identification(0)
    Function.Separator.Line(0)
    print("\tWelcome {} {}".format(Identity['First Name'],Identity['First Letter of Last Name']))
    while True:
        try:
            Function.Separator.Line(0)
            choice = int(input("""\tMenu:
            1. Employee Logs
            2. Register yourself
            3. Logout
            4. Quit
            What option do you pick: """))
            Function.Separator.Line(0)
            if choice == 1:
                Function.inFile.employeeRegister(0)
            elif choice == 2:
                Function.inFile.Register(0,Identity)
            elif choice == 3:
                Identity = Function.inForm.Identification(0)
            elif choice == 4:
                break
            else:
                Function.Messages.ERROR(0)
                pass
        except:
            pass

#Menu()
Function.inFile.employeeRegister(0)
