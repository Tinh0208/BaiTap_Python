# Nhập vào một số nguyên n.Kiểm tra và in ra n là só chẵn hay lẽ
integer = int(input("Enter your integer:"))

s = "it's odd"
if integer % 2 == 0:
    s = "it's even"  # no la so chan

print(s)
