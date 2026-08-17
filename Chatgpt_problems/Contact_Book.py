contact ={}
while True:
    name = input("Name:")
    phone = input("phone:")
    contact[name] = phone    
    again = input("Add another?(y/n):")
    if again == "n":
        break
print(contact)

