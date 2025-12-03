import sys,os,time


# Python AIO tool, Has build in a Variety of functions

class main():
    def __init__(self):
        print("Welcome to Python AIO Calculator Tool")
        time.sleep(1)
        print("Select the operation you want to perform:")
        print("Check connectivity to internet: 1 \n Open control panel: 2 \n Reset winsock & TCP/IP: 3 \n Check system info: 4 \n Open CMD: 5 \n Exit: 6")

run = input("Would you like to run the tool? (y/n): ")
if run.lower() != 'y':
    print("Exiting the program.")
    sys.exit()
else:
    run_status = True

while run_status==True:
    main()
    choice = input("Enter choice(1-5): ")


    if choice == '1':
        print("Checking internet connectivity...")
        response = os.system("ping 8.8.8.8 -n 1")
        if response == 0:
            print("Internet is connected")
        else:
            print("No internet connection")
    elif choice == '2':
        print("Opening Control Panel...")
        os.system("control")
    elif choice == '3':
        print("Resetting Winsock and TCP/IP...")
        os.system("netsh winsock reset")
        os.system("netsh int ip reset")
        print("Please restart your computer to apply changes.")
    elif choice == '4':
        print("Fetching system information...")
        os.system("systeminfo")
        save = input("Do you want to save the system info to a text file? (y/n): ")
        if save.lower() == 'y':
            os.system("systeminfo > system_info.txt")
            print("System information saved to system_info.txt")

    elif choice == '5':
        print("Opening Command Prompt...")
        os.system("start cmd")
    else:
        print("Invalid input. Please select a valid option.")
        break

    if input("Do you want to perform another operation? (y/n): ").lower() != 'y':
        print("Exiting the program.")
        run_status = False

#Made by An0nCTF
