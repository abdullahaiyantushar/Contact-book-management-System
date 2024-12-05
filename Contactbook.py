import search_contact 
from savecontact import contactload
import remove_contact
import add_contact
from viewcontact import view

maincontact= contactload()# initialize empty list for contact book 
print(type(maincontact))
while True:
    print("Contact Book Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Remove Contact")
    print("4. Search Contact ")
# use try exception block for unexpected error
    try:
        choice = int(input("Enter your choice Option : "))

    except Exception as e:
            print (e)
    if choice == 0:
        print("Thanks for using Favourite Foods Manager")
        break

    elif choice == 1:
            add=add_contact.addcontact(maincontact)
        
    elif choice == 2:
            view(add)
        
    elif choice ==3:
            remove_contact.remove_con(maincontact)

    elif choice== 4:
            search_contact.searchtwo(maincontact)

    else:
        print("Invalid Input")


   

    