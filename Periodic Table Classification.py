#Periodic Table element classification
import json

def main():
    element_input = input("What element are you looking for? ").title()
    element, element_dict = element_loader(element_input)
    if element in element_dict:
        print(f"Element: {element}")

def element_loader(element_input):
    with open("element.json", "r") as file:
        element_dict = json.load(file)
    for element in element_dict:
        if element['Name'] == element_input:
            return element, element_dict
        
main()
