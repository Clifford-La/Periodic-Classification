#Periodic Table element classification
import json
import math
import time
import datetime
green = "\033[32m"
def main():
    element_input = input("Would you like to look for an element? If not then enter '9' to quit. ").title() #ask the user for any element on the periodic table, '.title' capitalizes the first letter of the element
    if element_input == '9': #user can end program key9
        turning_off()
    element, element_dict = element_loader(element_input) #gets the element and the whole dict from the json file
    if element in element_dict:
        print(f"{green}Element: {element}")

def element_loader(element_input):
    with open("element.json", "r") as file: #this is where it opens the json file but it is in read mode only.
        element_dict = json.load(file)
    for element in element_dict:
        if element['Name'] == element_input: #if i enter hydrogen then it will return the element hydrogen and the rest of the information from the json file
            return element, element_dict 
        
def turning_off():
    time.sleep(1.5)
    today = datetime.datetime.now()
    print("Periodic Table Classification out! Stay noble like the gases. ")
    print(today)
    print(f'Current time: {today.time()}')
    print(f'Current date: {today.date()}')
    quit()

main()
