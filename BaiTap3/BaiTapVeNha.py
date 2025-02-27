# Câu 1
# import infoSV as sv
# ten_sinhvien1 = sv.ten()
# mssv_sinhvien1 = sv.mssv()
# Câu 2
import infoSV
infoSV.thongtincanhan()
# Câu 3
import lopLapTrinhMang
lopLapTrinhMang
# Câu 4
string = input("Nhập dãy số mới: ")
my_list = string.split(", ")
re_list = list(map(lambda x: int(((2*50*int(x))/30)**0.5), my_list))
for re in re_list:
    print("kết quả là: ", re, end=" ")
# Câu 5
x = int(input("Nhập số cột: "))
y = int(input("Nhập số hàng: "))
matrix2 = [[i * j for j in range(x)] for i in range(y)]
print(matrix2)
# Câu 6
string = input("Nhập chuỗi: ")
print(','.join(sorted(string.split(','))))
# Câu 7
chuoi = input("Nhập chuỗi: ")
print((lambda string : string.upper())(chuoi))
# Câu 8
string = input("Nhập chuỗi: ")
print(' '.join(sorted(set(string.split(" ")))))
# Câu 9
def is_num(num):
    if len(str(int(num))) == 4 and int(num) % 5 == 0:
        return num
    return ' '
num = input("Nhập chuỗi số: ")
my_l = num.split(',')
re = list(map(lambda num : is_num(num), my_l))
for i in re:
    if i != ' ':
        print(i, end=' ')
# Câu 10
