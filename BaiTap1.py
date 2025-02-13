# Cau 1
print("Good morning")
# Cau 2
sv = 'Nguyen Dang Tien'
mssv = 3123580050
print(sv, mssv)
# Cau 3
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
print('Tong: ', a+b)
print('Hieu: ', a-b)
print('Tich: ', a*b)
print('Thuong: ', a/b)
# Cau 5
ho = input('Nhap ho: ')
dem = input('Nhap ten dem: ')
ten = input('Nhap ten: ')
print(ten, dem, ho)
# Cau 6
import math
x1 = int(input("Nhap x1: "))
y1 = int(input("Nhap y1: "))
x2 = int(input("Nhap x2: "))
y2 = int(input("Nhap y2: "))
print('Khoang cach la: ', math.sqrt((x2-x1)**2 + (y2-y1)**2))
# Cau 7
list_a = [1, 3, 4, 6, 9, 10, 'a', 'b', 'c']
s = 0
for i in list_a:
    if type(i) == int or type(i) == float:
        s+=i
print('Tong cua cac phan tu la so la: ', s)
# Cau 8
list_b = [1, 3, 5 , 4 , 0, 11]
print('So lon nhat la: ', max(list_b))
# Cau 9
print('So nho nhat la: ', min(list_b))
# Cau 10
sort_l = sorted(list_b)
print('So lon nhi la: ', sort_l[-2])
# Cau 11
print('So nho nhi la: ', sort_l[1])
# Cau 12
def prime(a):
    if a < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if a % i == 0:
            return False
    return True

n = 10
for i in range(2, n+1):
    if prime(i):
        print(i, end=' ')