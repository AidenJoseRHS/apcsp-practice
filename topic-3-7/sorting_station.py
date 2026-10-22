# 1. Read one label and extract all five fields. Convert size and mass to numbers.
# 2. Apply the first matching rule. Use a nested conditional and print exactly one destination.
# 3. Run the examples, then test your own boundary cases. Fix the first mismatch and retest.

label = input()
shape = label[0:4]
color = label[4:7]
size = label[7:10]
sizeint = int(size)
mass = label[10:14]
massint = int(mass)
con = label[14:]


getLabelLen = len(label)
Labellen = int(getLabelLen)


if(Labellen == 15):
    if(con == "D" or sizeint > 50 or massint > 2000) :
        print("INSPECT")
    else :
        if(shape == "BALL") :
            if(color == "RED" and sizeint > 10) :
                print("B")
            else : print("A")
        else : 
            if(shape == "CUBE") :
                if(sizeint < 10 and color == "BLU" or color == "GRN") :
                    print("C")
                else : print("D")
            else : print("E")

    
else : print("Doesnt work nerd")