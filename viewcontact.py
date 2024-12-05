def view(contactview):
    if contactview != []:
        for i in contactview:
            print(f"Name : {i["Name"]} | Email : {i["Email"]} | Phone Number : {i["Phone Number"]} | Address : {i["Address"]} | Profession : {i["Profession"]}") 

    else : 
        print(" Contact book is no found ")
