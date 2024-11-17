# Su dung ham print
# BAI TAP 1
# CAU A
print("\n * * * * * \n * * * * * \n * * * * * \n * * * * * ")
# CAU B
print("\n * * * * * \n *       * \n * * * * * ")
# CAU C
print("\n   *  *  \n *       * \n *       * \n *       * \n   *  *  ")
# CAU D
print("\n * * * * * \n   * * *   \n   * * *   \n   * * *   \n * * * * * ")
# BAI TAP 2
print("xxxxx  xx  xx  xxxxxx xx  xx   xxxx    xx  xx")
print("xx  xx xx  xx    xx   xx  xx  xx  xx   xxx xx")
print("xxxxx  xx  xx    xx   xxxxxx  xx  xx   xxxxxx")
print("xx       xx      xx   xx  xx  xx  xx   xx xxx")
print("xx       xx      xx   xx  xx   xxxx    xx  xx")
# BAI TAP 3
print("QUÊ HƯƠNG")
print(". . .")
print("Quê hương là chùm khế ngọt")
print("    Cho con trèo hái mỗi ngày")
print("        Quê hương là đường đi học")
print("            Con về rợp bướm vàng bay \n")
print("                         Giáp Văn Thạch")
# Su dung ham Input
# BAI TAP 4
a = int(input("a = "))
b = int(input("b = "))
print(str(a) + " + " + str(b) + " = " + str(a+b))
# CAU A
a = int(input("a = "))
b = int(input("b = "))
# CAU B
a, b = input("a, b = ").split()
# CAU C
a, b = map(int, input("a, b = ").split(';'))
# BAI TAP 5
c, d = map(int , input("c, d = ").split())
print(str(c) + " * " + str(d) + " = " + str(c*d))
# BAI TAP 6
z = int(input("Nhap a: "))
print(str(z) + " + " + str(z*10 + z) + " + " + str(z*100 + z*10 + z) + " = " + str(z + z*10 + z + z*100 + z*10 + z))
# BAI TAP 7
x = "Python" 
y = "Python" 
e = "python"
d1 = hex(id(x))
d2 = hex(id(y))
d3 = hex(id(e))
print(str(d1) +  " " + str(d2) + " " + str(d3))
# Su dung phuong thuc format cua chuoi co trong print
# BAI TAP 8
a, b, c = map(int, input("Nhap a, b, c: ").split())
tong = a + b + c
print('{} {} {}'.format(min(a, b, c), tong - max(a, b, c) - min(a, b, c), max(a, b, c)))
# BAI TAP 9
d = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm) :>? "))
r = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm) :>? "))
h = float(input("Nhập chiều cao hình khối chữ nhật (cm) :>? "))
sole = int(input("Số lượng số lẻ cần hiển thị:>? "))
print("Diện tích đáy hình chữ nhật = " + str(round(d * r, sole)) + "cm\u00b2")
print("Thể tích hình khối = " + str(round(d * r * h, sole)) + "cm\u00b3")
# Tinh toan don gian
# BAI TAP 10
m = int(input("Nhập số tháng: "))
print("Sau " + str(m) + " đàn thỏ tăng lên là: " + str(2 * m) + " con")
# BAI TAP 11
import math
t = float(input("Nhập vào bán kính hình tròn: "))
print("Diện tích phần in đậm là: " + str(round((2 * t)**2 - t**2 * math.pi, 2)))
# BAI TAP 12
import math
t1 = float(input("Nhập vào bán kính hình tròn "))
print("Diện tích phần tô màu là: " + str(round(t1**2 * math.pi - ((2*t1)/math.sqrt(2))**2, 2)))
# BAI TAP 13
import datetime
ten = str(input("          Nhập tên: "))
tuoi = int(input("Nhập tuổi : "))
nam = datetime.datetime.now().year
print("Đến năm " + str(nam + (100 - tuoi)) + ", bạn {} sẽ tròn 100 tuổi".format(ten))
# BAI TAP 14
x = int(input("Nhap so tien: "))
print("So tien " + str(x) + " duoc doi thanh: ")
print("Loai 500 gom " + str(x//500) + " to")
print("Loai 200 gom " + str(x%500//200) + " to")
print("Loai 100 gom " + str(x%500%200//100) + " to")
print("Loai 50 gom " + str(x%500%200%100//50) + " to")
print("Loai 20 gom " + str(x%500%200%100%50//20) + " to")
print("Loai 10 gom " + str(x%500%200%100%50%20//10) + " to")    
print("Loai 5 gom " + str(x%500%200%100%50%20%10//5) + " to")
print("Loai 2 gom " + str(x%500%200%100%50%20%10%5//2) + " to")
print("Loai 1 gom " + str(x%500%200%100%50%20%10%5%2//1) + " to")
a = x//500 + x%500//200 + x%500%200//100 + x%500%200%100//50 + x%500%200%100%50//20 + x%500%200%100%50%20//10
b = x%500%200%100%50%20%10%5%2//1 + x%500%200%100%50%20%10%5//2 + x%500%200%100%50%20%10//5 
print("TỔNG CỘNG CÓ " + str(a + b) + " TỜ")
#Cau truc dieu kien
# BAI TAP 15 
# CAU A
n = int(input("Nhap so n: "))
if( n % 2 == 0):
    print("n la so chan")
else:
    print("n la so le")
# CAU B
n = int(input("Nhap so n: "))
if( n % 4 % 2 == 0):
    print("n chia chan cho 4")
elif(n % 2 % 2 == 0):
    print("n chia chan cho 2")
else:
    print("n khong chia chan cho 2 va 4")
# CAU C
n = int(input("Nhap so bi chia: "))
m = int(input("Nhap so chia: "))
if( (n / m) % 2 == 0 ):
    print("n chia chan cho m")
else:
    print("n khong chia chan cho m")
# BAI TAP 16
x = int(input("Nhap so tien: "))
print("So tien " + str(x) + " duoc doi thanh: ")
print("Loai 500 gom " + str(x//500) + " to")
if(x%500//200 > 0):
    print("Loai 200 gom " + str(x%500//200) + " to")
if(x%500%200//100 > 0):
    print("Loai 100 gom " + str(x%500%200//100) + " to")
if(x%500%200//100 > 0):
    print("Loai 50 gom " + str(x%500%200%100//50) + " to")
if(x%500%200%100%50//20 > 0):
    print("Loai 20 gom " + str(x%500%200%100%50//20) + " to")
if(x%500%200%100%50%20//10 > 0):
    print("Loai 10 gom " + str(x%500%200%100%50%20//10) + " to")    
if(x%500%200%100%50%20%10//5 > 0):
    print("Loai 5 gom " + str(x%500%200%100%50%20%10//5) + " to")
if(x%500%200%100%50%20%10%5//2 > 0):
    print("Loai 2 gom " + str(x%500%200%100%50%20%10%5//2) + " to")
if(x%500%200%100%50%20%10%5%2//1 > 0):
    print("Loai 1 gom " + str(x%500%200%100%50%20%10%5%2//1) + " to")
a = x//500 + x%500//200 + x%500%200//100 + x%500%200%100//50 + x%500%200%100%50//20 + x%500%200%100%50%20//10
b = x%500%200%100%50%20%10%5%2//1 + x%500%200%100%50%20%10%5//2 + x%500%200%100%50%20%10//5 
print("TỔNG CỘNG CÓ " + str(a + b) + " TỜ")
# Mo rong
a = int(input("Nhap so tien hang can phai tra: "))
b = int(input("Nhap so tien thuc te khach hang tra cho nhan vien: "))
if(a > b):
    print("So tien tra la cho khac" + str(b-a))
elif(a == b):
    print("Cam on khach hang. Hen gap lai")
else:
    x = b - a
    print("So tien " + str(x) + " duoc doi thanh: ")
    print("Loai 500 gom " + str(x//500) + " to")
    if(x%500//200 > 0):
        print("Loai 200 gom " + str(x%500//200) + " to")
    if(x%500%200//100 > 0):
        print("Loai 100 gom " + str(x%500%200//100) + " to")
    if(x%500%200//100 > 0):
        print("Loai 50 gom " + str(x%500%200%100//50) + " to")
    if(x%500%200%100%50//20 > 0):
        print("Loai 20 gom " + str(x%500%200%100%50//20) + " to")
    if(x%500%200%100%50%20//10 > 0):
        print("Loai 10 gom " + str(x%500%200%100%50%20//10) + " to")    
    if(x%500%200%100%50%20%10//5 > 0):
        print("Loai 5 gom " + str(x%500%200%100%50%20%10//5) + " to")
    if(x%500%200%100%50%20%10%5//2 > 0):
        print("Loai 2 gom " + str(x%500%200%100%50%20%10%5//2) + " to")
    if(x%500%200%100%50%20%10%5%2//1 > 0):
        print("Loai 1 gom " + str(x%500%200%100%50%20%10%5%2//1) + " to")
    a = x//500 + x%500//200 + x%500%200//100 + x%500%200%100//50 + x%500%200%100%50//20 + x%500%200%100%50%20//10
    b = x%500%200%100%50%20%10%5%2//1 + x%500%200%100%50%20%10%5//2 + x%500%200%100%50%20%10//5 
    print("TỔNG CỘNG CÓ " + str(a + b) + " TỜ")
    input("Nhan Enter de tiep tuc....")
    print("Cam on khach hang. Hen gap lai")
# BAI TAP 17
diem = int(input("Nhap diem: "))
if(diem < 0 or diem > 100):
    print("Chi nhan cac gia tri tu 0 den 100")
else:
    if( diem >= 90):
        print("Xep loai: A")
    elif( diem >= 80 and diem < 90):
        print("Xep loai: B")
    elif( diem >= 70 and diem < 80):
        print("Xep loai: C")
    elif( diem >= 65 and diem < 70):
        print("Xep loai: D")
    else:
        print("Xep loai: E")
# BAI TAP 18
n = int(input("NHap n: "))
if(n == 1):
    print("I")
elif(n == 2):
    print("II")
elif(n == 3):
    print("III")
elif(n == 4):
    print("IV")
elif(n == 5):
    print("V")
elif(n == 6):
    print("VI")
elif(n == 7):
    print("VII")
elif(n == 8):
    print("VIII")
elif(n == 9):
    print("IX")
else:
    print("X")
# BAI TAP 19
a = float(input("Nhap can nang: "))
b = float(input("Nhap chieu cao: "))
c = a / b**2
if( c < 18.5):
    print("Thieu can")
elif(c >= 18.5 and c < 23):
    print("Binh thuong")
elif(c >= 23 and c < 25):
    print("Binh thuong")
else:
    print("Beo phi")
# BAI TAP 20
# BAI TAP 21
a, b = map(int, input("Nhap a, b").split())
if( a == 0):
    print("Phuong trinh vo nghiem")
elif( a == 0 and b == 0):
    print("Phuong trinh vo so nghiem")
else:
    c = -b//a
    print("Phuong trinh co nghiem: " + str(c))
# BAI TAP 22
import math
a, b, c = map(int, input("Nhap a, b, c: ").split())
delta = b**2 - (4*a*c)
if(delta == 0):
    print("Phuong trinh co nghiem kep" + str(-b/2*a))
if(delta < 0):
    print("Phuong trinh vo nghiem")
else:
    nghiem1 = (-b + math.sqrt(delta)) / (2*a)
    nghiem2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phuong trinh co nghiem x1 = {}, x2 = {}".format(nghiem1, nghiem2))
# BAI TAP 23
xA, yA = map(int, input("Nhap xA, yA: ").split())
xB, yB = map(int, input("Nhap xB, yB: ").split())
xC, yC = map(int, input("Nhap xC, yC: ").split())
xP, yP = map(int, input("Nhap xP, yP: ").split())
x1 = (xB - xA) * (yP - yA) - (yB - yA) * (xP - xA)
x2 = (xC - xB) * (yP - yB) - (yC - yB) * (xP - xB)
x3 = (xA - xC) * (yP - yC) - (yA - yC) * (xP - xC)
if( x1 > 0 and x2 > 0 and x3 > 0):
    print("P nam trong tam giac ABC")
else:
    print("P khon nam trong tam gia ABC")
# BAI TAP 24
import math as m

x1 = int(input("Nhap toa do x C1: "))
y1 = int(input("Nhap toa do y C1: "))
r1 = int(input("Nhap ban kinh C1: "))
x2 = int(input("Nhap toa do x C2: "))
y2 = int(input("Nhap toa do y C2: "))
r2 = int(input("Nhap ban kinn C2: "))

if m.sqrt(y2-y1**2 + x2-x1**2) > r1 + r1:
    print("Hai duong tron khong giao nhau")
if m.sqrt(y2-y1**2 + x2-x1**2) == r1 + r1:
    print("Hai duong tron tiep xuc nhau")
if abs(r2-r1) < m.sqrt(y2-y1**2 + x2-x1**2) < r1 + r1:
    print("Hai duong tron cat nhau")
if m.sqrt(y2-y1**2 + x2-x1**2) < r1 + r1:
    print("Hai duong tron chua trong nhau")
if m.sqrt(y2-y1**2 + x2-x1**2) < abs(r1 - r1):
    print("Hai duong tron nam trong nhau")

# BAI TAP 25
a, b, c, d, e, f = map(int, input("Nhap cac so a, b, c, d, e, f: ").split())
d1 = a * e - b * d
d1X = c * e - b * f
d1Y = a * f - d * c
if d1 != 0:
    print("x = {}; y = {}".format(d1X/d1, d1Y/d1))
elif d1Y != 0 and d1X != 0:
    print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh vo so nghiem")
# BAI TAP 26
# CAU A
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

if abs(b - a) == abs(c - b):
    print("So tiep theo trong cap so cong: " + str(max(a, b, c) + abs(b - a)))
elif (b/a) == (c/b):
    print("So tiep theo trong cap so nhan: " + str(max(a, b, c) * (c//b)))
else:
    print("Khong co cap so nhan")
# CAU B
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

if abs(b - a) == abs(c - b):
    print("Co the tao thanh cap so cong")
elif (b/a) == (c/b):
    print("Co the tao thanh cap so nhan: ")
else:
    print("Khong co cap so nhan")
# Cau truc lap
# BAI TAP 27
n = int(input("Nhap so n: "))
# CAU A
for i in range(1, n + 1): print(i)
# CAU B
for i in range(1, n + 1):
    if (5 * i) % 5 == 0:
        print(i) 
# CAU C\
    sum = 0
for i in range(1, n + 1):
        sum+=i
print(sum)
# CAU D
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s+= i
print(s) 
# CAU E
tong = 0;
for i in range(1, n + 1):
    if i % n == 0:
        tong+=i;
        print(i)
print(tong)
# CAU F
max = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i > max:
        max = i
print(max)
# CAU G
max1 = 0;
for i in range(1, n + 1):
    if i % 2 != 0 and i > max:
        max = i
print(max)
# BAI TAP 28
n = int(input("Nhap so luong so can in: "))
a = int(input("Nhap so bat dau: "))
d = int(input("Nhap cong sai: "))
count = 0
for a in range(a, 100):
    count+=1
    if count <= n:
        print(a + d)
# BAI TAP 29
n = int(input("Nhap so luong so can in: "))
a = int(input("Nhap so bat dau: "))
d = int(input("Nhap cong boi: "))
count = 0
for a in range(a, 100):
    count+=1
    if count <= n:
        print(a * d)
# BAI TAP 30
# CAU A
while True:    
    a = int(input("Nhap vao so thu nhat: "))
    b = int(input("Nhap vao so thu hai: "))
    opt = input("Nhap phep tinh: ")
    if opt == "+" :
        print("{} + {} = {} ".format(a, b, a + b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "-" :
        print("{} - {} = {} ".format(a, b, a - b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "*" :
        print("{} * {} = {} ".format(a, b, a * b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "/" :
        print("{} / {} = {} ".format(a, b, a / b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "%" :
        print("{} % {} = {} ".format(a, b, a % b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "^" :
        print("{} ^ {} = {} ".format(a, b, a ** b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "<<" :
        print("{} << {} = {} ".format(a, b, a << b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == ">>" :
        print("{} >> {} = {} ".format(a, b, a >> b))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break    
# CAU B
import operator as o
while True:    
    a = int(input("Nhap vao so thu nhat: "))
    b = int(input("Nhap vao so thu hai: "))
    opt = input("Nhap phep tinh: ")
    if opt == "+" :
        print("{} + {} = {} ".format(a, b, o.add(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "-" :
        print("{} - {} = {} ".format(a, b, o.sub(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "*" :
        print("{} * {} = {} ".format(a, b, o.mul(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "/" :
        print("{} / {} = {} ".format(a, b, o.truediv(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "%" :
        print("{} % {} = {} ".format(a, b, o.mod(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "^" :
        print("{} ^ {} = {} ".format(a, b, o.pow(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == "<<" :
        print("{} << {} = {} ".format(a, b, o.lt(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break
    if opt == ">>" :
        print("{} >> {} = {} ".format(a, b, o.ge(a, b)))
        ask = input("Ban co muon tiep tuc (y/n): ")
        if ask == "n":
            break    
# BAI TAP 31
# C
m = int(input("Nhap so m: "))
n = int(input("Nhap so m: "))
c = 0
for i in range(1, m):
    if i % 2  == 0:
        print(i, end=", ")
        c+=1
if c == 0:
    print("Khong co uoc so nao cua n nho hon m")
         
         
