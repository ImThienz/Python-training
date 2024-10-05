# x=5
# print(type(x))
# x='teo'
# print(type(x))
# x=True
# print(type(x))
# del x
# x=5.5
# print(type(x))
# x=complex(113,114)
# print(type(x))
# print(x.real, x.imag)

f=open("data.txt","a",encoding="utf-8")
while True:
    maSV= input("nhập mã SV: ")
    if maSV =="":  # nếu o nhập gì
        break      # thoát while true ,kết thúc nhập
    tenSV =input("Tên Sinh viên: ")
    Lop= input("lớp : ")
    Que = input("Quê quán: ")

    f.write("\t".join([maSV,tenSV,Lop,Que]) + "\n") # ghi dữ liệu vào file
f.close() # đóng file

print("cách 1 ")

f=open("data.txt","r",encoding="utf-8")
print("\t".join([" Mã SV"," Tên SV","Lớp "," Quê"]))
for sv in f.readlines():
    print(sv.replace("\n",""))
f.close()
