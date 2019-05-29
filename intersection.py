x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
x3 = int(input("x3 : "))
y3 = int(input("y3 : "))
x4 = int(input("x4 : "))
y4 = int(input("y4 : "))
# x1 = 10
# y1 = 10
# x2 = 100
# y2 = 100
# x3 = 10
# y3 = 100
# x4 = 100
# y4 = 10
P1 = (x1,x2)
P2 = (x2,y2)
P3 = (x3,y3)
P4 = (x4,y4)
ligne = [P1,P2]
ligne = [P3,P4]
if x2 == x1:
	coef1 = 0
else:
	coef1 = (y2 - y1)/(x2 - x1)
if x4 == x3:
	coef2 = 0
else:
	coef2 = (y4 - y3)/(x4 - x3)
ord1 = (-x1*coef1)+y1
ord2 = (-x3*coef2)+y3
if coef1 == coef2 :
	print("paralèlle")
else:
	inter_x = (ord2 - ord1)/(coef1-coef2)
	inter_y = coef1*inter_x + ord1
	print(P1,P2,coef1,ord1,P3,P4,coef2,ord2,inter_x,inter_y)
