units = int(input("enter your units"))

if units < 100:
    bill = units*2
elif units < 200:
    bill = units*3
else:
    bill = units*5
    
print("bill=" , bill)            
