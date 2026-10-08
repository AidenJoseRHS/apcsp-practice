
pointspergame = [20,29,31,23,32,40]
points = 80
games = len(pointspergame)

for pointsavg in range(2,len(pointspergame),1):
    points = points - (points / (games))

print(points)