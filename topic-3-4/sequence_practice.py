scores = [72, 86, 91, 68, 88]
title = "weekly score report"
print(title + str(scores))
print(scores[0])
print(scores[2])
print(scores[4])
scores.append(93)

first_word = title[0:6]
last_word = title[13:]
print(first_word)
print(last_word)

label = "Top 3!" + ": ", scores[2], scores[4], scores[1]
print(label)

#a list element can change because one of the values can change into a different number or character but a if you replace a character in a string value it reads it as an error or it will be invalid