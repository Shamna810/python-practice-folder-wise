username = "Bioinformatics"
password = "Shamna123"

for i in range(1):
    user = input("enter username")
    pwd = input("enter password")
    
    if user == username and pwd == password:
        print("Login successfull")
        break
    else:
        print("Login Unsuccessfull and wrong credentials")
        