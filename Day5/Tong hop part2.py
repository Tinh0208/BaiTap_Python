"""2.Tạo một set trống có tên là set_a
a.Thêm "Anna " vào set_a
b.Thêm một tuple ('Kenny','Jen','Danny')
c.In ra set_a và tính chiều dài của nó
d.Xóa 'jen' ra ra khỏi set_a
e.Xóa tất cả các giá trị từ set_a"""

set_a = set()
#a.
set_a.add("Anna")
print ("a:set_a: ",set_a)
#b.
set_a.update(('Kenny','Jen','Danny'))
"""or
tup = ('Kenny','Jen','Danny')
set_a.update(tup)"""

print (f"b: set_a: ",set_a)
print('-' * 50)
#c.
length = len(set_a)
print ("c:Set_a:",set_a, "Chiều dài của set_a :",length,sep=" ")
#d.
set_a.remove('Jen')
print ("d:set_a sau khi xóa Jen",set_a)
#e.
set_a.clear()
print (set_a)