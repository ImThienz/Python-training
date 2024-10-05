"HÀM UPPER; lower"
# name="vũ thành đạt"
# print(name.upper())
#
# name1="NGUYỄN VĂN SƠN"
# print=(name1.lower())


"9. Write a Python program to remove the nih index character from a nonempty string."
# Viết chương trình Python để xóa ký tự tại vị trí n (vị trí do người dùng nhập vào) từ một chuỗi không rỗng.

user_string = input("Nhập một chuỗi không rỗng: ")
n = int(input("Nhập chỉ số của ký tự cần xóa (bắt đầu từ 0): "))

# Kiểm tra nếu n nằm trong phạm vi hợp lệ
if n < 0 or n >= len(user_string):
    print("Chỉ số không hợp lệ.")
else:
    # Xóa ký tự tại vị trí n
    new_string = user_string[:n] + user_string[n+1:]

    print("Chuỗi sau khi xóa ký tự tại vị trí", n, "là:", new_string)


"10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged."
# Viết chương trình Python thay đổi chuỗi sao cho ký tự đầu tiên và ký tự cuối cùng được hoán đổi vị trí?

user_string = input("Nhập một chuỗi: ")

# Kiểm tra nếu chuỗi có ít nhất 2 ký tự
if len(user_string) < 2:
    print("Chuỗi quá ngắn để hoán đổi ký tự đầu và cuối.")
else:
    # Tạo chuỗi mới bằng cách hoán đổi ký tự đầu và cuối
    new_string = user_string[-1] + user_string[1:-1] + user_string[0]
    print("Chuỗi sau khi hoán đổi ký tự đầu và cuối là:", new_string)


"11. Write a Python program to remove characters that have odd index values in a given string."
# Viết chương trình Python xóa các ký tự có chỉ số lẻ trong một chuỗi

user_string = input("Nhập một chuỗi: ")

# Tạo chuỗi mới bằng cách giữ lại các ký tự có chỉ số chẵn
new_string = user_string[::2]
print("Chuỗi sau khi xóa các ký tự có chỉ số lẻ là:", new_string)


"12. Write a Python program to count the occurrences of each word in a given sentence."
# Đếm số lần xuất hiện của mỗi từ trong một câu cho trước

sentence = input("Nhập một câu: ")
words = sentence.split()

# Khởi tạo từ điển để lưu số lần xuất hiện của từng từ
word_count = {}

# Lặp qua các từ và đếm số lần xuất hiện
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Số lần xuất hiện của mỗi từ trong câu là:")
for word, count in word_count.items():
    print(f"'{word}': {count}")


"13. Write a Python script that takes input from the user and displays that input back in upper and lower cases."
# Lấy đầu vào từ người dùng và hiển thị lại đầu vào đó dưới dạng chữ in hoa và chữ thường

user_input = input("Nhập một chuỗi: ")
print("Chuỗi in hoa:", user_input.upper())
print("Chuỗi in thường:", user_input.lower())


"14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically)."
"Sample Words: red, white, black, red, green, black Expected Result: black, green, red, white,red"
# 1. Nhập một chuỗi các từ, ngăn cách nhau bằng dấu phẩy.
# 2. Chuyển chuỗi thành danh sách các từ.
# 3. Loại bỏ các từ trùng lặp.
# 4. Sắp xếp các từ theo thứ tự bảng chữ cái (alphanumerically).
# 5. In kết quả là danh sách các từ đã được sắp xếp.

input_words = input("Nhập các từ, ngăn cách nhau bằng dấu phẩy: ")

# Chuyển chuỗi thành danh sách các từ, loại bỏ khoảng trắng đầu và cuối từ
word_list = [word.strip() for word in input_words.split(",")]

# Loại bỏ các từ trùng lặp bằng cách chuyển thành set, sau đó sắp xếp lại
distinct_words = sorted(set(word_list))

print("Các từ không trùng lặp, sắp xếp theo thứ tự là:", ", ".join(distinct_words))
