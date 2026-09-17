# 1. Read one label and extract all five fields. Convert size and mass to numbers.
# 2. Apply the first matching rule. Use a nested conditional and print exactly one destination.
# 3. Run the examples, then test your own boundary cases. Fix the first mismatch and retest.

label = input("Enter Object Label: ")

shape = label[0:4]
# if shape == "ball" or "cube" or "cone":
#     if shape == "ball" :
#         print("ball")
#     # if shape == "cube" 
#         print("cube")
#     if shape == "cone" :
#         print("cone")
#     else : print("invalid Shape")

color = label[4:7]
# if color == "red" or "ble" or "grn":
#     if color == "red" :
#         print("red")
#     if color == "blu" :
#         print("blue")
#     if color == "grn" :
#         print("green")
#     else : print ("Invalid Color")

size = label[7:10]
sizeint = int(size)
# print(size)

mass = label[10:14]
massint = int(mass)
# print(mass)

con = label[14:]
# if con == "N" or "D":
#     if con == "N" :
#         print("Normal")
#     if con == "D":
#         print("Damaged")
#     else : print("Invalid Number")
getLabelLen = len(label)
Labellen = int(getLabelLen)

#print(shape)
#print(color)
#print(size + "cm")
#print(mass + "grams")
if(Labellen == 15):
    if(con == "D" and size >= 50 or mass >= 2000) :
        print("INSPECT")
    else :
        if (shape = "ball") :
        else : print("")
    
else : print("Doesnt work nerd")