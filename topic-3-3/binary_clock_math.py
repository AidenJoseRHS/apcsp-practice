clock_value = 45
remaining = clock_value

bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2

#45/2 22 remainder #1 22/2 11 remainder #0 11/2 5 remainder #1 5/2 2 remainder #1 2/2 1 remainder 0 1/1 0 remainder 1 
# prediction 1,0,1,1,0,1
# actual 1,0,1,0,1,1
# modulo calculates the remainder of a number. 


clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
clock_values.append(59) # 1,1,1,0,1,1 
labels.append("seconds")
labels.append("milliseconds") # the report code did not need to change when the lists grew because selected_index grabs values in the clock_values string and the labels string in accordance to which number they are in the list. then clock_value is set to the number selected index grabs and the calculator is ran afterwards.

selected_index = int(input("enter 0,1,2 or 3: "))

clock_value = clock_values[selected_index]
label = labels[selected_index]

remaining = clock_value

bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2

bits =[bit_32, bit_16, bit_8, bit_4, bit_2, bit_1]

bit_text = str(bits[0]) + str(bits[1]) + str(bits[2]) + str(bits[3]) + str(bits[4]) + str(bits[5])

check_value = bits[0]*32 + bits[1]*16 + bits[2]*8 + bits[3]*4 + bits[4]*2 + bits[5]

print(label, ":", check_value, " = ", bit_text)
print("original: ", clock_value)
print("reconstructed: ", check_value)

