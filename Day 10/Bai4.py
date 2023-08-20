# #Sử dụng zip function để tạo 2 list sau trở thành một dict

fruits = ["Banana", "Apple", "Kiwi", "Mango", "Cherry", "Orange"]
amounts = [12, 34, 90, 100, 300, 45, 60, 70, 678]
new_lst = list(zip(fruits, amounts))
print(new_lst)
