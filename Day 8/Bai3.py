#Đếm số lượng số nguyên tố trong [1,100]
count = 0
for n in range(2,101):
    for x in range(2,n):
        if n % x == 0:
            break
    else:
        count += 1
        print(n,end = ' ')    
print(f"\n{count}")      
#cách 2