# Nhập vào một năm bất kỳ,kiểm tra xem năm đó có phải là năm nhuận hay k
# Năm nhuận là năm chia hết cho 4 và k chia hết cho 100 hay năm chia hết cho 400
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap-year")  # năm nhuận
else:
    print("Common year")  # k nhuận
