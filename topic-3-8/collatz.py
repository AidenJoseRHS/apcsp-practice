# label = input()

# getLabelLen = len(label)
# Labellen = int(getLabelLen)

n = 999999
peaking=0
steps = 0
limiter = False

print("START: ", n)

while n != 1 and n <= 1000000 :
    steps = steps + 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    if n > peaking:
        peaking = n
print("steps:", steps)
print("peak: ", peaking)
if n == 1 and limiter == False:
    print("REACHED 1")


