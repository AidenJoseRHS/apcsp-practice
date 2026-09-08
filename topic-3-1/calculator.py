print("lets count how much apples are fresh!" ) #output
apples_stored = int(input("Apples stored: ")) #inputs & assignment

boxes_expired = int(input("Boxes expired: ")) #inputs & assignment

amount_apples_box = int(input("Apples per box: ")) #inputs & assignment

fresh_apples = apples_stored - boxes_expired * amount_apples_box #assignment and expresson
print("Amount of fresh apples", fresh_apples) #output

#int is needed because it changes the values into integers