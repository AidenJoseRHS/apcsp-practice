# AP CSP Day 10: input/output scaffold, not a completed binary report.
# In your existing binary_clock_math.py, preserve your lists, labels, index,
# conversion, report features, and test comments. Use your existing variable names.
# These sample lists make this template runnable on its own.
values = [13, 45, 63]
labels = ["Sample A", "Sample B", "Sample C"]
selected_index = 0

# PROVIDED INPUT: Run, click the Terminal, type an integer, and press Enter.
# Text and decimal input handling is outside today's task.77
values[selected_index] = int(input("Enter a number: "))
clock_value = values[selected_index]
selected_label = labels[selected_index]
print("You entered:", clock_value)


if (clock_value >= 0) and (clock_value <= 63):
    print("Invalid Number")
    remaining = clock_value

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

if (check_value %2 == 1) :
        print("Odd")
else : print ("Even")
print(selected_label, ":", check_value, " = ", bit_text)
print("original: ", clock_value)
print("reconstructed: ", check_value)




# YOUR CODE START
# 1. Add a range decision for whole numbers from 0 through 63.
# 2. Put your existing extraction, bit_text, reconstruction, and report
#    inside the valid branch. Keep the selected label in the report.
# 3. Inside that branch, add an even/odd decision using the remainder.
# 4. In the invalid branch, print only the invalid message after the input echo.
# YOUR CODE END

# OUTPUT PATTERNS: move/uncomment these only in the appropriate branches.
# print(label + ": " + bit_text)
# print("Even")  # or print("Odd")
# print("Outside six-bit range")
