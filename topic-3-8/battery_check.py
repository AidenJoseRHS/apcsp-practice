charges = [62,28,85,14,47]
lowest = charges[0]
hightest = 0
count = 0
any80 = False
below30 = 0
greatest=0
# checkval = 0
# checkval2 = checkval +1

# for i in range(0,len(charges), 1):
#     if charges[checkval] > charges[checkval2]:
#         greatest = charges[checkval]
#         checkval = checkval +1
#     elif charges[checkval] < charges[checkval2]:
#         greatest = checkval2
#         checkval = checkval+1
#         least = checkval2

# print(greatest)

for i in range(0,len(charges),1):
    if lowest > charges[i]:
        lowest = charges[i]
    if greatest < charges[i]:
        greatest = charges[i]
    if charges[i] < 30:
        below30 = charges[i]
    if charges[i] >= 80:
        any80 = True
        if charges[i] < 30:
            count = count + 1
    if charges[i] > 0:
        temp = charges[i]
        sums = charges[i] + temp
for charge in charges:
    if charge < 30:
        below30 += 1
        
    

print(lowest)
print(greatest)
print(sums)


my_list = [1,2,3,4]

for i in range(0, len(my_list), 1):
    my_list[i] = my_list[i] * 2

for value in my_list:
    value = value *2