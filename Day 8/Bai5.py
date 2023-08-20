#Nhập vào một số nguyên duong n .Đếm số lương số chẵn và số lẻ trong đoạn [0,n]
""" n = int(input("Nhập vào số nguyên dương n:"))
even = []
odd = []
for x in range(0,n):
    if x % 2 == 0:
        odd.append(x)
    else:
        even.append(x)
print("Odd",odd)
print("Even",even)   
 """
n = int(input("Nhập vào số nguyên dương n:"))
even = []
count_even = 0
count_odd = 0
odd = []
for x in range(0, n):
    if x % 2 == 0:
        odd.append(str(x))
        count_even += 1
    else:
        even.append(str(x))
        count_odd += 1
""" odd_str = " ".join(odd)
even_str = " ".join(even)

print("Odd: ", odd_str)
print("Even: ", even_str) """

#or 
print("Even: ",','.join(map(str,even)))
print("Odd: ",','.join(map(str,odd)))
print(f"There are {count_even} even number")#có number số chẵn
print(f"There are {count_odd} odd number")
print(len(even))
print(len(odd))
 #cách 2
