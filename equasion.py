import math
print("Welcome! Let's solve a quadratic equation together :)")

print("Program solves the equasion: ax² + bx + c = 0")
print("Please, input integer coefficients")
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
    exit()
D = b**2 - 4*a*c
sqrt_D = math.sqrt(abs(D))

if D > 0:
    x1 = (-b + sqrt_D) / (2*a)
    x2 = (-b - sqrt_D) / (2*a)
    print("Equasion has two distinct real roots:")
    print("Root 1 = ", x1)
    print("Root 2 = ", x2)

elif D == 0:
    x = -b / (2*a)
    print("Equasion has one real root:")
    print("Root = ", x)

else:
    real_part = -b / (2*a)
    imag_part = sqrt_D / (2*a)
    x1 = complex(real_part, imag_part)
    x2 = complex(real_part, -imag_part)
    print("Equasion has two complex roots:")
    print("Root 1 = ", x1)
    print("Root 2 = ", x2)
