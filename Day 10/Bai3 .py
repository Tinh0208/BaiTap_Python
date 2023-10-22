# cho dict như sau:
import json
people = {
    'Emma': 71,
    'Jack': 45,
    'Amy': 15,
    "Ben": 29
}
# In ra người lớn tuổi nhất
max_age = 0
new_name = ''
for name, age in people.items():
    if age > max_age:
        max_age = age
        new_name = name
print(new_name)
# Tạo ra một dict mới vào people dict với age của mỗi người tăng gấp đôi
new_people = {
    name: age * 2
    for name, age in people.items()
}
print(json.dumps(new_people,indent= 4))

# In ra enumerate các key trong people dict
new_lst = [k for k in people]
print(list(enumerate(new_lst)))
# Sử dụng hàm dict để biến enumerate bên trên trở thành dict
new_people1 = dict(enumerate(people.keys()))
print(json.dumps(new_people1, indent=4))
