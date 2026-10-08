# Use a>0, b>=0, each at most 1,000,000. While b is not 0, save a % b
# , replace a with the old b, then replace b with the saved remainder. Report the final a (the largest integer dividing both original inputs) and repetitions.
a = 7
b = 0
save = 0
step = 0

while b != 0:
    save = a % b
    a = b
    b = save
    step += 1
    print(step)
else: 
    print("reached")
    print("Gcd: ", a)
    