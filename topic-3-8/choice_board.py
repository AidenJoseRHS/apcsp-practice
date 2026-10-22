# Average of points a player gets in a season
pointspergame = [29,20,31,40,32,24]
games = len(pointspergame)
greatest = 0
least = pointspergame[0]
check = 0
value = check +1

for i in range(0,len(pointspergame),1):
        if least > pointspergame[i]:
            least = pointspergame[i]
        if greatest < pointspergame[i]:
            greatest = pointspergame[i]

print(greatest)
print(least)

# for i in range(0,len(charges),1):
#     if lowest > charges[i]:
#         lowest = charges[i]
#     if greatest < charges[i]:
#         greatest = charges[i]
#     if charges[i] < 30:
#         below30 = charges[i]
#     if charges[i] >= 80:
#         any80 = True
#         if charges[i] < 30:
#             count = count + 1
#     if charges[i] > 0:
#         temp = charges[i]
#         sums = charges[i] + temp
# for charge in charges:
#     if charge < 30:
#         below30 += 1