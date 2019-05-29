x1 = 100
y1 = 10
x2 = 100
y2 = 100
x3 = 50
y3 = 100
x4 = 150
y4 = 10
P1 = (x1,y1)
P2 = (x2,y2)
P3 = (x3,y3)
P4 = (x4,y4)
ligne = [P1,P2]
ligne = [P3,P4]
if x2 == x1:
	coef1 = 1000000
else:
	coef1 = (y2 - y1)/(x2 - x1)
if x4 == x3:
	coef2 = 10000000
else:
	coef2 = (y4 - y3)/(x4 - x3)
ord1 = (-x1*coef1)+y1
ord2 = (-x3*coef2)+y3
if coef1 == coef2 :
	print("paralèle")
else:
	print(ord1,coef1)
	interX = (ord2 - ord1)/(coef1-coef2)
	interY = coef1*interX + ord1
	print(interX,interY)