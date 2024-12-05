import csv

def save_contacttwo(contactone):
    with open('contact.csv',mode="w") as c:
        for i in contactone:
            Nam = f"{i["Name"]}, {i["Email"]}, {i["Phone Number"]}, {i["Address"]}, {i["Profession"]}"
            c.writerow(Nam)

import csv

def contactload():
    with open('contact.csv',mode="r") as C:
        contacts=csv.reader(C)
        return contacts

