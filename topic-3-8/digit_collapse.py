# Use an integer 0-1,000,000. Add its decimal digits; repeat complete passes until one digit remains.
# Use % 10 to get a digit and Python // 10 or Java integer / 10 to remove it. Do not convert to text. An inner while loop consumes digits; an outer while loop repeats passes.
#  Reset the sum for each pass. Report the final digit and pass count.

#Also temporarily set the step limit to 5: start 6 ends at 8, after 5 transformations, peak 16, LIMIT REACHED. Restore 1,000 afterward. Starting at 6 produces 6, 3, 10, 5, 16, 8, 4, 2, 1.
number = 9875
sum = 0

while number != 0:
    sum = sum + number%10
    number = number//10


print(sum)
print(number)