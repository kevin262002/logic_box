name = input("Enter Month : ")

if name == "February":
    print("28/29 days")
elif name in ("April", "June", "September", "November"):
    print("30 days")
elif name in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 days")
else:
    print("Invalid Month")
    
