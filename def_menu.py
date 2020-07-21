# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 


def run_menu():

    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
            1: goods to csv
            2: get pics to csv
            3: get pics to list and save pisc from url
            4: from custom .csv
            q: Quit/Log Out

            Please enter your choice: """)
    if choice in ['1','2','3','4']:
        return(choice)
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        run_menu()



# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 