# Đếm số chẵn và lẻ trong đoạn [0,100] :thông thường và list comprehension
odd = even = 0
for number in range(0, 101):
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Cac so chan la: {even}\nCac so le la: {odd}')

# dung comprehension
lst = list(range(0, 101))
lst_comprehension_even = sum([1 for n in lst if n % 2 == 0])
lst_comprehension_odd = sum([1 for n in lst if n % 2 != 0])

print("Even:", lst_comprehension_even)

print("Odd:", lst_comprehension_odd)
