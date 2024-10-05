"Viết hàm tính giải phương trình bậc 1"
def PTB1(a,b):
    if a==0 and b==0:
        return "Vô số nghiệm"
    elif a==0 and b!=0:
        return "Vô nghiệm"
    else:
        return "x={0}".format(round(-b/a,2))

"Viết hàm xuất dữ liệu ra màn hình"
def XuatDuLieu(data):
    print(data)

"Phân tích giai thừa theo cách đệ qui?"
#n! = n.(n-1).(n-2).(n-3) ... 3.2.1
"Viết lại dạng PT Đệ qui có điều kiện"
#n! = 1, if n=0
#   = n.(n-1)!,
" Điểm dừng là khi n=0, quy luật là nếu biết (n-1)! thì tính được N! , vì N!=N*(N-1)! "

"1. Write a Python function to find the maximum of three numbers"