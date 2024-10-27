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
