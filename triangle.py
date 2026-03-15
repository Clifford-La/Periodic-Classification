sideA = int(input("SIDE A: "))
sideB = int(input("SIDE B: "))
sideC = int(input("SIDE C: "))

if sideC * sideC == sideA * sideA + sideB * sideB:
    print("RIGHT ANGLED TRIANGLE")
elif sideA == sideB and sideB == sideC:
    print("Equilateral triangle")
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print("Isosceles Triangle")
else:
    print("Scalene triangle")