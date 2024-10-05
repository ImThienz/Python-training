# BIỂU THỨC BOOLEAN
a=True
b=False
print('a=',a,'b=',b)
#gán lại kết quả cho a
a=False
print('a=',a,'b=',b)

# BIỂU THỨC IF
dtb=float(input("Nhâp điểm trung bình:"))
if dtb >= 5:
    print("Bạn đã đậu!")
else: print("Xui!")

"Q8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:"
#Q8. Tính tiền điện theo các chỉ số sau:
# Unit                            Price

# First 100 units                 no charge
# Next 100 units                  Rs 5 per unit
# After 200 units                 Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

# Nhập số đơn vị từ người dùng
units = int(input("Nhập số đơn vị điện đã sử dụng: "))

# Tính hóa đơn
def calculate_electricity_bill(units):
    if units <= 100:
        return 0
    elif units <= 200:
        return (units - 100) * 5
    else:
        return (100 * 5) + (units - 200) * 10

# Tính và in hóa đơn tiền điện
bill = calculate_electricity_bill(units)
print(f"Hóa đơn tiền điện của bạn là: Rs {bill}")



"Q9. Write a program to display the last digit of a number."
#(hint: any number % 10 will return the last digit)
#Q9. Tính số dư chia hết cho 10

number = int(input("Nhập một số: "))

# Tính chữ số cuối cùng
last_digit = number % 10

print(f"Chữ số cuối cùng của số {number} là: {last_digit}")


"Q10. Write a program to check whether the last digit of a number entered by user) is divisible by 3 or not."
#Q10. Kiểm tra xem chữ số cuối cùng của một số có chia hết cho 3 hay không?

number = int(input("Nhập một số: "))

last_digit = number % 10

if last_digit % 3 == 0:
    print(f"Chữ số cuối cùng {last_digit} chia hết cho 3.")
else:
    print(f"Chữ số cuối cùng {last_digit} không chia hết cho 3.")


# VÒNG LẶP WHILE
#s=0, i=1, n=5
print("Nhập N:")
n=int(input())
s=0
i=1
while i<=n:
    s=s+1
    i=i+1
    print("Tổng =",s)


"Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using While Loop"
# Viết chương trình in dãy Fibonacci đến n số (với n được nhập từ người dùng) bằng vòng lặp while

# Nhập số lượng số Fibonacci từ người dùng
n = int(input("Nhập số lượng số Fibonacci cần in: "))

# Khởi tạo các biến
a, b = 0, 1
count = 0

# In các số Fibonacci cho đến khi đạt số lượng yêu cầu
print("Dãy Fibonacci:")
while count < n:
    print(a, end=' ')
    # Cập nhật các giá trị
    a, b = b, a + b
    count += 1



"Q16. Write a program to print the factorial of a number accepted from user"

"Cách 1: Sử dụng vòng lặp while"
n = int(input("Nhập một số nguyên không âm: "))

if n < 0:
    print("Giai thừa không được định nghĩa cho số âm.")
else:
    # Khởi tạo biến để tính giai thừa
    factorial = 1
    count = 1

    # Tính giai thừa bằng vòng lặp while
    while count <= n:
        factorial *= count
        count += 1
    print(f"Giai thừa của {n} là: {factorial}")

"Cách 2: Import thư viện match"
import math

n = int(input("Nhập một số nguyên không âm: "))

if n < 0:
    print("Giai thừa không được định nghĩa cho số âm.")
else:
    # Tính giai thừa bằng hàm factorial của thư viện math
    factorial = math.factorial(n)

    # In kết quả
    print(f"Giai thừa của {n} là: {factorial}")
