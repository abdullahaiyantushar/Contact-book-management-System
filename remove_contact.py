def remove_con(conmove):
    for conner in conmove:
        # use try exception block for unexpected error
        try:
            Name=input(" Enter you Contact name to remove: ")
        except Exception as e:
            print (e)   
            
        if conner["Name"] == Name:
            conmove.remove(conner)
            print("contact remove Successfully ")
            return 
        else: 
            print("Contact is not Found")
