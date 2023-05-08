#1.Cho một list chứa các tuple như sau: friends = [("Bob","Male"),("Anna","Female"),("Max","Male")]
""""a.Cho biết chiều dài của list firends
b.Lấy ra phần tử đầu,cuối,và giữa kiểm tra kiểu của chúng
c.Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó sẽ append 
vào freiends tuple gồm 2 giá trị {name,gender}"""


friends = [("Bob","Male"),("Anna","Female"),("Max","Male")]
#a.

tup_len = len(friends)
print(tup_len)
#b.
tup_first = friends[0]
tup_middle = friends[1]
tup_last = friends[2]
print("Phần tử đầu:",tup_first)
print("Phần tử giữa:",tup_middle)
print("Phần tử cuối:",tup_last)
#c.
name = str(input("Nhập vào tên: "))
gender = str(input("Nhập vào giới tính: "))

tup_last1 = (name, gender)
new_friends = friends.append(tup_last1)
print("Friend: ",friends)
