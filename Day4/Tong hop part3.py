#2.Cho danh sách các sinh viên chứa thông tin của  mỗi sinh viên[id,tên,tuổi] như sau:

students =[{"SV001","Bob",23},{"SV002","Kenny",34},{"SV003","Henry",45}]
print (students)

#1 Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID:{id},name:{name} - age:{age}"

student = students[0]
id, name, age = student
print(f"ID:{id}, name:{name} - age:{age}")

#2 Lấy tuổi của sinh viên số 2
print("Tuổi của sinh viên số 2:",age)

#Cách 2: age = list(students[1])[-1]
#print(age)

#3 Lấy ra thông tin của 2 sinh viên cuối cùng

student_2_sv = students[1:]
print(student_2_sv)
#4 Lấy ra id của sinh viên số 3

student_3_id = list(students[2])[0]# [-1][0]
print (student_3_id)


