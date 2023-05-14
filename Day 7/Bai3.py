#Nhập vào 2 số in ra số lớn nhất và nhỏ nhất trong 2 số
""" a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))

if a > b:
    print(f"Số lớn nhất trong 2 số {a} và {b} là :" ,a)
    print(f"Số bé nhất trong 2 số {a} và {b} là :" ,b)
else:
    print(f"Số lớn nhất trong 2 số {a} và {b} là :" ,b)
    print(f"Số bé nhất trong 2 số {a} và {b} là :" ,a) """

a, b = map(float,input("Nhập vào 2 số a,b: ").split())
if a > b:
    print(f"Số lớn nhất trong 2 số {a} và {b} là :" ,a)
    print(f"Số bé nhất trong 2 số {a} và {b} là :" ,b)
else:
    print(f"Số lớn nhất trong 2 số {a} và {b} là :" ,b)
    print(f"Số bé nhất trong 2 số {a} và {b} là :" ,a)
