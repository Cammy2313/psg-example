print("Operador XNOR")
print((True == True)) 
print((True == False)) 
print((False == True)) 
print((False == False))

print("Operador XNOR")

a = True
b = True
print(not ((a or b) and not (a and b)))  # True

a = True
b = False
print(not ((a or b) and not (a and b)))  # False

a = False
b = True
print(not ((a or b) and not (a and b)))  # False

a = False
b = False
print(not ((a or b) and not (a and b))) 