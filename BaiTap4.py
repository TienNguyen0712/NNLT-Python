# BaiTapThucHanh
# BaiTap1
class Employee:
    def __init__(self, name, salary):
       self.name = name
       self.salary = salary
    def show_info(self):
        print(f"Nhân viên: {self.name}\nLương: {self.salary}")
    def increase_salary(self, new_salary):
        self.salary+=new_salary

# BaiTap2
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def show_info(self):
        print(f"Nhân viên {self.name} có quản lý {self.bonus}\nLương {self.salary}")
# BaiTapVeNha
# BaiTap1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Số tiền đã thanh toán {self.__balance}")
        else:
            print("Không đủ")
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Không tồn tại")
    def caculate_total(self):
        return sum(item.get_price() for item in self.items)
    def apply_discount(self, discount):
        total_price = self.caculate_total()
        discount_price = total_price * (discount / 100)
        return total_price - discount_price
# BaiTap2
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def update_quantity(self, new_quantiy):
        self.quantity = new_quantiy
class Warehouse:
    def __init__(self, location):
        self.location = location
        self.items = []
    def add_item(self, item):
        return self.items.append(item)
    def remove_item(self, item, re_quantity):
        for i in self.items:
            if i.name == item:
                if i.quantity >= re_quantity:
                    i.update_quantity(i.quantity - re_quantity)
                    return True
                else:
                    return False
        return False
class StockManager(Warehouse):
    def check_stock(self, check_item, check_quantity):
        for item in self.items:
            if item.name == check_item:
                if item.quantity < check_quantity:
                    return "Cảnh báo"
                else:
                    return f"{check_item} có số lượng {item.quantity}"
        return "Không tìm thấy"
# BaiTap3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_salary(self):
        return self.salary
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def get_total_pay(self):
        self.salary + self.bonus
class Payroll:
    def __init__(self):
        self.employees = []
    def adđ_employees(self, employee):
        self.employees.append(employee)
    def caculate_total_cost(self):
        return sum(employee.get_salary() for employee in self.employeeslist)
# BaiTap4
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Số tiền đã thanh toán {self.__balance}")
        else:
            print("Không đủ")
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Không tồn tại")
    def caculate_total(self):
        return sum(item.get_price() for item in self.items)
    def apply_discount(self, discount):
        total_price = self.caculate_total()
        discount_price = total_price * (discount / 100)
        return total_price - discount_price
# BaiTap5
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def update_quantity(self, new_quantiy):
        self.quantity = new_quantiy
class Warehouse:
    def __init__(self, location):
        self.location = location
        self.items = []
    def add_item(self, item):
        return self.items.append(item)
    def remove_item(self, item, re_quantity):
        for i in self.items:
            if i.name == item:
                if i.quantity >= re_quantity:
                    i.update_quantity(i.quantity - re_quantity)
                    return True
                else:
                    return False
        return False
class StockManager(Warehouse):
    def check_stock(self, check_item, check_quantity):
        for item in self.items:
            if item.name == check_item:
                if item.quantity < check_quantity:
                    return "Cảnh báo"
                else:
                    return f"{check_item} có số lượng {item.quantity}"
        return "Không tìm thấy"
# BaiTap6
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_salary(self):
        return self.salary
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def get_total_pay(self):
        self.salary + self.bonus
class Payroll:
    def __init__(self):
        self.employees = []
    def adđ_employees(self, employee):
        self.employees.append(employee)
    def caculate_total_cost(self):
        return sum(employee.get_salary() for employee in self.employeeslist)
# BaiTap7
class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses
class Course:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee
    def get_course(self):
        print(f"Khoá học {self.name} có giá {self.fee}")
class Enrollment:
    def __init__(self, name):
        self.name = name
        self.list_course = []
    def enroll_course(self, course):
        return self.list_course.append(course)
    def total_fee(self):
        return f"Học phí: {sum(course.fee for course in self.list_course)}"
# BaiTap8
class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status
    def get_book(self):
        print(f"Sách : {self.title}\nTác giả : {self.author}\nNội dung : {self.status}")
class Member:
    def __init__(self, name, borrwed_books):
        self.name = name
        self.borrwed_books = borrwed_books
        self.list_book = []
    def add_book_borrow(self, name):
        if name in self.list_book:
            self.list_book.append(self.borrwed_books)
        else:
            print("Không tồn tại sách này trong thư viện")
class Library:
    def __init__(self, books, members):
        self.books = books
        self.member = members
        self.list_book = []
    def add_book_to_lib(self):
        return self.list_book.append(self.books)
# BaiTap9
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def check_balance(self):
        return self.balance
class Transaction():
    def __init__(self, amount, type, owner):
        self.amount = amount
        self.type = type
        self.owner = owner
    def add_or_remove_amount(self):
        if self.type == 1:
            self.owner.balance += self.amount
        else:
            if self.amount > self.balance:
                print("Không thể rút")
            else:
                self.owner.balance -= self.amount 
class Bank:
    def __init__(self, accounts, transactions):
        self.accounts = accounts
        self.transaction = transactions
    def get_acc(self):
        print(f"Tài khoản {self.accounts}\nGiao dịch {self.transaction}")
