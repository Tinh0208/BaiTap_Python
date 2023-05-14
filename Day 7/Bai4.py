# Solution và biện minh phương trình bậc nhất có một ẩn ax + b = 0 (ẩn x và a,b là số cho trước)
a, b = map(int, input("Nhập vào 2 số a và b: ").split())

print(f"Phương trình hiện tại là: {a}x + {b} = 0")
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    print(f"Phương trình có một nghiệm duy nhất X = {-b/a}")
