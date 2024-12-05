def searchtwo(searchkaku):
    Name=input("enter your contact name what are you tring to find: ")
    for i in searchkaku:
        if i["Name"] ==Name:
             print(f"Name : {i["Name"]} | Email : {i["Email"]} | Phone Number : {i["Phone Number"]} | Address : {i["Address"]} | Profession : {i["Profession"]}") 
        else:
            Print("Your Contact is not Found")
            