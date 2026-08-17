numbers = [11,34,57,12,39,41]

even = 0
odd = 0

for num in numbers:
    if num%2==0:
        even+= 1
    else:
        odd+= 1
print("even:" , even)
print("odd:" , odd)            