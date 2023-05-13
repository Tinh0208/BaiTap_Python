"""
1.Cho 2 tập hợp (set)
- art_students ={"Jhon","Max","Anna","Bob","Obito"}
- math_students = {"Max","Mery","David","Anna","Naruto","John"}
- Tìm các bạn học cả vẽ và toán
- Tìm những người bạn học vẽ nhưng không học toán
- Tìm những người bạn học toán nhưng không học vẽ
- Tìm những người bạn học vẽ hay toán không phải cả 2
- Tìm tất cả những người bạn
"""
#Cho 2 tập hợp set
art_students ={"John","Max","Anna","Bob","Obito"}
math_students = {"Max","Mery","David","Anna","Naruto","John"}
#-Tìm các bạn học cả vẽ và toán(both: cả 2)

both_art_math_student = art_students.intersection(math_students)
print("Các bạn học cả vẽ và toán: ",both_art_math_student)
# - Tìm những người bạn học vẽ nhưng không học toán(but:nhưng )
art_but_math = art_students.difference(math_students)
print("Những người bạn học vẽ nhưng không học toán: ",art_but_math)
# - Tìm những người bạn học toán nhưng không học vẽ
math_but_art = math_students.difference(art_students)
print("Những người bạn học toán nhưng không học vẽ: ",math_but_art)
#- Tìm những người bạn học vẽ hay toán không phải cả 2
art_or_math = art_students.symmetric_difference(math_students)
print("Những người bạn học vẽ hay toán không phải cả 2: ",art_or_math)
#- Tìm tất cả những người bạn
all_art_math = art_students.union(math_students)
print("Tất cả những người bạn: ",all_art_math)