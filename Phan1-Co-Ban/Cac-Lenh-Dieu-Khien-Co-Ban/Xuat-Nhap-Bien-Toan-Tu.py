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
