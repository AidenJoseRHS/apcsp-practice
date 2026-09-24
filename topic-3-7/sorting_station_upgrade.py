# 1. Read one label and extract all five fields. Convert size and mass to numbers.
# 2. Apply the first matching rule. Use a nested conditional and print exactly one destination.
# 3. Run the examples, then test your own boundary cases. Fix the first mismatch and retest.

label = input()

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

# print(shape)
# print(color)
# print(size + "cm")
# print(mass + "grams")
held = False
bypasscheck = False
if Labellen == 15:

    if shape == "CUBE" and sizeint <= 60 and massint <= 2500:
        bypasscheck = True


    if (bypasscheck == False) and con == "D" or sizeint > 50 or massint > 2000 : 
        print("INSPECT")
        held = True
    else :
        bypasscheck = True


    if shape == "BALL" and bypasscheck == True :
        if color == "RED" and sizeint > 10 :
            print("B")
        else:
            print("A")
    else:
        if shape == "CUBE":
            if (color == "BLU" or color == "GRN") and sizeint < 10 :
                print("C")
            else:
                print("D")
        else:
            print("E")
else:
    print("Doesnt work nerd")

if held == True and shape == "CONE" or massint > 1000:
    print("CRATE")
else:
    if shape == "BALL":
        print("PADDED")
    else:
        print("BOX")
