
#1 tạo một movies list chứa tên các bộ phim đã xem

movies_list = ["Cánh diều bay","Con thuyền ra khơi","Con yêu mẹ","Bánh trôi nước"]
print(movies_list)

#2 Sử dụng hàm input nhập vào một bộ phim khác k có trong movies list

Add_movie_list = movies_list.append(input("Nhập tên phim: "))

#3 Thêm bộ phim vừa nhập vào cuối danh sách movies 

print (f"Danh sách phim: " ,movies_list)

#4 In ra bộ phim đầu tiên,cuối cùng,ở giữa movies list

""" print("Tên bộ phim đầu tiên: ",movies_list[0])#Tên phim đầu tiên
print ("Tên bộ phim cuối cùng: ",movies_list[4])#Tên phim đầu cuối
print ("Tên bộ phim giữa: ",movies_list[2])#Tên phim giữa """

print ("In phim đầu,cuối,giữa:", movies_list[0],movies_list[4],movies_list[2] ,sep= " ||")

#5 Tính tổng số bộ phim đang có
Len = len(movies_list)
print("Tổng số bộ phim: ",Len)
#4 In ra bộ phim đầu tiên,cuối cùng,ở giữa movies list
print ("In phim đầu,cuối,giữa: ", movies_list[0],movies_list[Len // 2],movies_list[2] ,sep= " ||")
#6 Xóa bộ phim đầu và cuối
clear_movies_list_dau = movies_list.pop(0)
clear_movies_list_cuoi = movies_list.pop(-1)

"""cách khác cau 6
list = movies_list.remove(movies_list[0]#shift + alter + down)
list = movies_list.remove(movies_list[1])"""

print ("Movies list hiện tại: ",movies_list)
#7 Lấy ra và xóa bộ phim cuối trong movies
print ("Bộ phim đã xóa cuối:", movies_list.pop(-1) ,"\n Movies list hiện tại: ", movies_list,sep = "||")
#8 Chèn một bộ phim bấy kỳ vào đầu danh sách 

print (movies_list.insert((0),  input("Nhập vào tên bộ phim mới: ")), "\n Movies list:",movies_list)

""" cách khác
a = input("nhap ten phim moi")
movies_list.insert(0,a)
print ("movie",movies_list)"""
#9 Đếm số phim có tiêu đề onepiece

print ("Số phim có tiêu đề OnePiece:",movies_list.count("OnePice"))
#10 Tìm vị trí của bộ phim có tên "oanh"
print ("Vị trí của bộ phim có tên oanh: ",movies_list.index("oanh"))
#11 Thêm một danh sách bộ phim khá vào cuối danh sách movies ban đầu

movies_extend = movies_list.extend(["conan","hentaiz","manga"])
print ("Danh sách phim mới: " , movies_list)
#12 Xóa tất cả danh sách phim có trong  chuỗi
movies_list.clear()
print ("Đã xóa hết phim: ",movies_list)

