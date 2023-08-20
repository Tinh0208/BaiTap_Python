# Nhập vào một số nguyên dương n tính tổng các chữ số của n
# ví dụ n = 4321 => 4+ 3+2+1 = 10
# range: n + 1
n = int(input("enter a positive integer  n: "))
total = 0
for x in str(n):
    total += int(x)
print(total)
# cách 2
print('-'*20)

count_sum = 0
while n > 0:
    count_sum += n % 10
    n //= 10
print("THe sum of digits of positive n is: ", count_sum)
