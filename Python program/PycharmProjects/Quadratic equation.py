A=eval(input("Enter number A : "))
B=eval(input("Enter number B : "))
C=eval(input("Enter number C : "))
D=(B**2)-(4*A*C)
sol1 = (-B-Cmath.sqrt(D))/(2*A)
sol2 = (-B+Cmath.sqrt(D))/(2*A)
print("The solution are {0} and {1}" .format(sol1,sol2))