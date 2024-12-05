from savecontact import save_contacttwo

def addcontact(allcontact):
    name = input("Enter Your Name: ")
    email = input("Enter Your email: ")
    Phone_number = input("Enter your phone Number: ")
    address = input("Enter your Adress: ")
    profession = input("Enter your Profession: ")
    
    contact = {
        "Name": name,
        "Email": email,
        "Phone Number": Phone_number,
        "Address": address,
        "Profession": profession 
        }
    
    allcontact.append(contact)
    save_contacttwo(allcontact)
    
    print("Contact Added Successfully") 

    return allcontact
