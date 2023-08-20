# Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list
integer = list(map(int, input("Nhap vao danh sach so nguyen: ").split()))

lst = [n*2 for n in integer]
print(lst)
