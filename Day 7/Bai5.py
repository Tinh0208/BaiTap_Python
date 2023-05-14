# Giải và biện luận pt bậc 2 ax^2 + bx + c = 0
import math
a, b, c = map(eval, input("Nhập vào 3 số a,b,c: ").split())

print(f"Phương trình bậc 2: {a}x^2 + {b}x + {c} = 0")

if a == 0 or b == 0 or c == 0:
    print("Nhập lại ")
else:
    denta = b**b - 4*a*c
    if denta < 0:
        print("Phương trình vô nghiệm")
    elif denta == 0:
        print(f"Phương trình có nghiệm kép X1 = X2 = {-b /2 *a}")
    else:
        print(
            f"Phương trình có 2 nghiệm X1 = ", (-(b) + math.sqrt(denta)) / (2*a))
        print(
            f"Phương trình có 2 nghiệm X2 = {(-(b) - math.sqrt(denta )) / (2*a)}")
