def ten():
    name = input("Nhập tên của bạn: ")
    print(f"Tên của bạn là {name}")

def mssv():
    ma_so_sinh_vien = input("Nhập mã số sinh viên của bạn: ")
    print(f"Mã số sinh viên của bạn là: {ma_so_sinh_vien}")

def thongtincanhan():
    stt = int(input("Nhập số thứ tự: "))
    user_name = input("Nhập tên của bạn: ")
    ms = input("Nhập mã số sinh viên của bạn: ")
    ngay_thang_nam = input("Nhập ngày tháng năm: ")
    que = input("Nhập quê quán: ")
    class_name = input("Nhập tên lớp: ")
    my_dic = {"STT" : stt, "Họ và tên" : user_name, "MSSV" : ms, "Ngày tháng năm sinh" : ngay_thang_nam, "Quê quán" : que, "Lớp" : class_name}
    print(my_dic)