#Periodic Table element classification
from tqdm import tqdm
import json, sys, os, utc, time
from datetime import datetime
import pytz

Black = "\033[0;30m"
Red = "\033[0;31m"
Green = "\033[0;32m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
Light_green = "\033[1;32m"
Yellow= "\033[1;33m"
Light_blue = "\033[1;34m"
Bold = "\033[1m"
Italics = "\033[3m"
Crossed = "\033[9m"
RESET = "\033[0m"

def clear(): 
    os.system("clear")

def main():
    clear()
    loading("Loading")
    with tqdm(total=100) as pbar:
        for i in range(25):
            time.sleep(0.1)
            pbar.update(4)
    print()
    clear()
    
    while True:
        element_input = input(f"Enter an element {Italics}{Light_green}NAME{RESET}, {Italics}{Light_green}SYMBOL{RESET}, or {Italics}{Light_green}ATOMIC NUMBER{RESET}.{RESET}{Light_blue} If not then enter '9' to QUIT. {RESET}").title() #ask the user for any element on the periodic table, '.title' capitalizes the first letter of the element
        if element_input == '9': #user can end program key9
            turning_off()
        breakpoint
        try:
            element, element_dict = element_loader(element_input) #gets the element and the whole dict from the json file
        except TypeError:
            print("This element has not been discoverd yet")
            continue
        clear()
        print(f"{Green}{Bold}Element name:{RESET} {element["Name"]}{RESET}")
        print(f"{Green}{Bold}Symbol:{RESET} {element["Symbol"]}{RESET}")
        print(f"{Purple}{Bold}Atomic number:{RESET} {element["Atomic number"]}{RESET}")
        print(f"{Purple}{Bold}Atomic mass({RESET}u{Purple}):{RESET} {element["Atomic mass(u)"]}{RESET}")
        print(f"{Cyan}{Bold}Protons:{RESET} {element["Protons"]}{RESET}")
        print(f"{Red}{Bold}Neutrons:{RESET} {element["Neutrons"]}{RESET}")
        print(f"{Yellow}{Bold}Electrons:{RESET} {element["Electrons"]}{RESET}")
        print()
        print()

def element_loader(element_input):
    with open("element_full.json", "r") as file: #this is where it opens the json file but it is in read mode only.
        element_dict = json.load(file)
    for element in element_dict:
        if element['Name'] == element_input: #if i enter hydrogen then it will return the element hydrogen and the rest of the information from the json file
            return element, element_dict
        elif element['Symbol'] == element_input:      #if i enter H then it will return the element hydrogen and the rest of the information from the json file
            return element, element_dict
        elif element['Atomic number'] == element_input: #if i enter 1 then it will return the element hydrogen and the rest of the information from the json file
            return element, element_dict

        

def turning_off():
    time.sleep(1.5)
    clear()
    print(f"{Green}Stay noble like the gases. 🧪 ⚛︎ {RESET}")
    time_zone = pytz.timezone("Australia/Sydney")
    today = datetime.now(time_zone)
    print(f'{Blue}{Bold}Current time:{RESET} {today.time()}')
    print(f'{Blue}{Bold}Current date:{RESET} {today.date()}')
    quit()

def loading(load_screen):
    print(load_screen, end="")
    dots_delay_time = 0.5

    for i in range(5):
        time.sleep(dots_delay_time)
        print(" . ", end="")
        sys.stdout.flush()#

main()
