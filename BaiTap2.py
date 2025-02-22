# Phần bài tập các kiểu dữ liệu
# List
# Câu 1
my_list = ["*","**","***","****",]
for i in my_list:
    print(i)
# Câu 2
ten = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C"]
diem = [[7.4, 6.5, 7.0],[7.0, 6.5, 8.5], [5.5, 6.0, 7.5]]
hs = input("Nhập tên học sinh: ")
for i in range(len(ten)):
    if hs == ten[i]:
        print(f"{ten[i]} có điểm trung bình là: {sum(diem[i])//3}")
    else:
        print("Không có học sinh này")
# Câu 3
frs = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mon = [1.0, 7.5, 8.0, 8.3, 2.1, 3.3, 7.0]
for i in range(len(frs)):
    print(f"{frs[i]} có số tiền là: {mon[i]}/kg")
# Câu 4
ten = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C"]
diem = [[7.4, 6.5, 7.0],[7.0, 6.5, 8.5], [5.5, 6.0, 7.5]]
hs = input("Nhập tên học sinh: ")
if hs in ten:
    print("Học sinh có tồn tại")
    for i in range(len(ten)):
        if hs == ten[i]:
            print(f"{ten[i]} có điểm trung bình là: {sum(diem[i])//3}")
else:
    print("Không có học sinh này")
# Câu 5
frs.pop()
frs.insert(4, "coconut")
mon.insert(4, 9.0)
# Câu 6
mssv = []
ten = []
ngay_thang_nam = []
ten_lop = []
diem_thuong_ky = []
diem_giua_ki = []
diem_cuoi_ky = []
trungbinh = []
kq = []
choice = int(input("Nhập lựa chọn (1: Nhập/0: Tìm): "))
if choice == 1:
    ms = input("Nhập MSSV: ")
    mssv.append(ms)
    t = input("Nhập Họ và tên: ")
    ten.append(t)
    n = map(int, input("Nhập ngày tháng năm: "))
    ngay_thang_nam.append(n)
    lop = input("Nhập Tên lớp: ")
    ten_lop.append(lop)
    diemtk = float(input("Nhập Điểm thường kỳ: "))
    diem_thuong_ky.append(diemtk)
    diemgk = input("Nhập Điểm giữa kỳ: ")
    diem_giua_ky.append(diemgk)
    dck = input("Nhập Điểm cuối kỳ: ")
    diem_cuoi_ky.append(dck)
    tk = float(input("Nhập Trung bình tổng kết: "))
    trungbinh.append(tk)
    kqdr = input("Nhập MSSV: ")
    kq.append(kqdr)
else:
    hs = input("Nhập mssv cần tìm: ")
    if hs in mssv:
        for i in range(len(mssv)):
            if hs == mssv[i]:
                print(f"{ten[i]}")
    else:
        print("Không tìm thấy sinh viên này")
# Dictionary
# Câu 7
my_dic = {"STT": 1, 
          "Họ và tên": "Nguyen Van A",
          "MSSV": 12345678,
          "Ngày tháng năm sinh": "07122005",
          "Quê quán":"Nam Định",
          "Học Phí": 5000000,
          "Sở thích": "Chơi game",
        }
print(my_dic["Sở thích"])
my_dic["Sở thích"] = "Đọc truyện"
print(my_dic["Sở thích"])
# Câu 8
print(my_dic.keys())
print(my_dic["Họ và tên"])
print(my_dic.values())
print(my_dic)
# Câu 9
print("Số lượng thành phần trong dic là",len(my_dic))
new_item  = {"Ngoại ngữ": "Tiếng Anh", "Dân tộc" : "Kinh"}
my_dic.update(new_item)
print(my_dic)
del my_dic["Sở thích"]
print(my_dic)
# Câu 10
sinh_vien1 = {"MSSV": 23456781,
            "Tên": "Nguyen Van A",
            "Lớp": "DDU1231",
            }
sinh_vien2 = {"MSSV": 12345678,
            "Tên": "Nguyen Van B",
            "Lớp": "DDU1231",
            }
sinh_vien3 = {"MSSV": 987654321,
            "Tên": "Nguyen Van C",
            "Lớp": "DDU1231",
            }

DHDT12B_class = {"sv1": sinh_vien1,
           "sv2": sinh_vien2,
           "sv3":sinh_vien3,
           }
print(DHDT12B_class.keys())
dic_new = DHDT12B_class.copy()
ANHVAN01_class = {}
ANHVAN01_class["sv1"] = DHDT12B_class["sv1"]
ANHVAN01_class["sv2"] = DHDT12B_class["sv1"]
# Câu 11
sinh_vien4 = {"MSSV": 3334343434,
            "Tên": "Nguyen Van D",
            "Lớp": "DDU1231",
            } 
sinh_vien5 = {"MSSV": 6337373627,
            "Tên": "Nguyen Van E",
            "Lớp": "DDU1231",
            }
new_stu = {"sv4": sinh_vien4, "sv5" : sinh_vien5}
DHDT12B_class.update(new_stu)
ANHVAN01_class.update(new_stu)
sinh_vien4["Điểm TOEIC"] = 660
sinh_vien4["Tình trạng học phí"] = "Chưa nộp"
sinh_vien5["Điểm TOEIC"] = 700
sinh_vien5["Tình trạng học phí"] = "Đã nộp"
del DHDT12B_class["sv4"]
# Tuples
# Câu 12
sinhvienA = ("Nguyen Van A", 7.4, 6.5, 7.0)
tim_ten = input("Nhập tên sinh viên cần tìm: ")
for i in sinhvienA:
    if i == tim_ten:
        print(f"{sinhvienA[0]} có điểm trung bình {(sinhvienA[1] + sinhvienA[2] + sinhvienA[3])//3}")
# Câu 13
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
money = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)
for i in range(2,6):
    print(f"{fruits[i]} có giá là {money[i]}/kg")
# Câu 14
tuples1 = fruits[:3]
tuples2 = fruits[-3:]
print(tuples1 + tuples2)
# Câu 15
new_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "pineapple", "strawberry", "cucumber")
new_money = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0)
choice = int(input("Nhập lựa chọn (1: Tìm kiếm/0: Xuất): "))
if choice == 1:
    search_fruits = input("Nhập tên trái cây bạn muốn tìm: ")
    for i in range(len(new_fruits)):
        if new_fruits[i] == search_fruits:
            print(f"{new_fruits[i]} có giá tiền {new_money[i]}")
else:
    for i in range(len(new_fruits)):
        print(f"{new_fruits[i]} có giá là {new_money[i]}")
# Set
# Câu 16
set_fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "pineapple", "strawberry", "cucumber"}
print(set_fruits)
fruit = input("Nhập tên trái cây: ")
print(fruit in set_fruits)
# Câu 17
insert = {"avocado", "grape", "grapefruit", "starfruit", "lychee"}
new_set_fruits = set_fruits.union(insert)
print(new_set_fruits)
# Câu 18
set1 = {"avocado", 1.0, "grape", 2.0, "grapefruit", 3.0, "starfruit", 4.0, "lychee", 5.0}
set2 = {"apple", 6.0, "banana", 7.0, "cherry", 8.0, "orange", 9.0, "kiwi", 10.0}
sea_fr = input("Nhập tên trái cây muốn tìm: ")
if sea_fr in set1:
    print("Trong set thứ nhất")
    for i in range(len(set1)):
        if sea_fr == set1[i]:
            print(f"{set1[i]} có giá tiền {set1[i+1]}")
elif sea_fr in set2:
    print("Trong set thứ hai")
    for i in range(len(set2)):
        if sea_fr == set2[i]:
            print(f"{set2[i]} có giá tiền {set2[i+1]}")
else:
    print("Không tìm thấy")
union_set = set1.union(set2)
sea_fr1 = input("Nhập tên trái cây muốn tìm: ")
if sea_fr1 in union_set:
    for i in range(len(union_set)):
        if sea_fr1 == union_set[i]:
            print(f"{union_set[i]} có giá tiền {union_set[i+1]}/kg")
else:
    print("Không tìm thấy")
# Câu 19
set1 = {"avocado", 1.0, "grape", 2.0, "grapefruit", 3.0, "starfruit", 4.0, "lychee", 5.0}
set2 = {"apple", 6.0, "banana", 7.0, "cherry", 8.0, "orange", 9.0, "kiwi", 10.0}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.union(set2))
print(set1.difference_update(set2))
print(set2.difference_update(set1))