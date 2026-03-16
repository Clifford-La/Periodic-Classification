#Periodic Table element classification
from tqdm import tqdm
from zoneinfo import ZoneInfo
import json, sys, time, datetime, os, utc

green = "\033[32m"
bright_cyan = "\033[96m"
red = "\033[31m"
yellow = "\033[33m"
magenta = "\033[35m"
blue = "\033[34m"
grey = "\033[90m"

def clear(): 
    os.system("clear")

def main():
    loading("Loading")
    with tqdm(total=100) as pbar:
        for i in range(25):
            time.sleep(0.1)
            pbar.update(4)
    print()
    clear()
    
    element_input = input("Would you like to look for an element? If not then enter '9' to quit. ").title() #ask the user for any element on the periodic table, '.title' capitalizes the first letter of the element
    if element_input == '9': #user can end program key9
        turning_off()
    element, element_dict = element_loader(element_input) #gets the element and the whole dict from the json file
    if element in element_dict:
        print(f"{green}Element name: {element["Name"]}")
        print(f"{blue}Symbol: {element["Symbol"]}")
        print(f"{magenta}Atomic number: {element["Atomic number"]}")
        print(f"{grey}Atomic mass: {element["Atomic mass(u)"]}")
        print(f"{bright_cyan}Protons: {element["Protons"]}")
        print(f"{red}Neutrons: {element["Neutrons"]}")
        print(f"{yellow}Electrons: {element["Electrons"]}")


def element_loader(element_input):
    with open("element.json", "r") as file: #this is where it opens the json file but it is in read mode only.
        element_dict = json.load(file)
    for element in element_dict:
        if element['Name'] == element_input: #if i enter hydrogen then it will return the element hydrogen and the rest of the information from the json file
            return element, element_dict 


def turning_off():
    time.sleep(1.5)
    print(f"Periodic Table Classification out! Stay noble like the gases. 🧪 ⚛︎ {green}💧︎")
    today = datetime.datetime.now()
    print(f'Current time: {today.time()}')
    print(f'Current date: {today.date()}')
    quit()

def loading(load_screen):
    print(load_screen, end="")
    dots_delay_time = 0.5

    for i in range(5):
        time.sleep(dots_delay_time)
        print(" . ", end="")
        sys.stdout.flush()
main()
