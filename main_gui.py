import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import pymysql
from capture_images import capture_images, delete_images
from train_model import train_model
from recognize_faces import recognize_faces

class FaceRecognitionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Hệ thống nhận diện khuôn mặt")
        self.window.geometry('1200x800')
        self.window.configure(background='#f1f3f6')

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        self.create_widgets()

    def configure_styles(self):
        self.style.configure('TFrame', background='#f1f3f6')
        self.style.configure('Header.TLabel', font=('Arial', 30, 'bold'), background='#1e3d58', foreground='white', anchor='center')
        self.style.configure('Content.TLabel', font=('Arial', 16), background='#f1f3f6', foreground='#333')
        self.style.configure('TEntry', font=('Arial', 16), padding=5)
        self.style.configure('TButton', font=('Arial', 16, 'bold'), background='#1e3d58', foreground='white', padding=10)
        self.style.map('TButton', background=[('active', '#2a5572')])

    def create_widgets(self):
        # Header Section
        header_frame = ttk.Frame(self.window, style='TFrame', padding=20)
        header_frame.pack(fill=tk.X)
        header_label = ttk.Label(header_frame, text="                  HỆ THỐNG NHẬN DIỆN KHUÔN MẶT", style='Header.TLabel', padding=20)
        header_label.pack(fill=tk.X)

        # Main Content Area
        main_frame = ttk.Frame(self.window, style='TFrame', padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left side: User info inputs
        input_frame = ttk.LabelFrame(main_frame, text="Thông tin người dùng", style='TFrame', padding=20)
        input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=30, pady=20, expand=True)

        self.id_entry = self.create_labeled_entry(input_frame, "ID:", 0)
        self.name_entry = self.create_labeled_entry(input_frame, "Tên:", 1)

        # Right side: Action Buttons
        action_frame = ttk.LabelFrame(main_frame, text="Chức năng", style='TFrame', padding=20)
        action_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=30, pady=20, expand=True)

        self.create_button(action_frame, "Chụp ảnh", self.TakeImages)
        self.create_button(action_frame, "Train ảnh", self.TrainImages)
        self.create_button(action_frame, "Nhận diện", self.TrackImages)

        # Add "Xuất file Excel" button here (above "Xóa ảnh")
        self.create_button(action_frame, "Xuất file Excel", self.export_to_excel)

        self.create_button(action_frame, "Xóa ảnh", self.DeleteImages)

        # Notifications and attendance info frame below user info
        info_frame = ttk.Frame(input_frame, style='TFrame', padding=10)
        info_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

        # Notification section
        self.notification_var = tk.StringVar()
        notification_label = ttk.Label(info_frame, text="Thông báo:", style='Content.TLabel', anchor='w')
        notification_label.pack(fill=tk.X)
        notification_content = ttk.Label(info_frame, textvariable=self.notification_var, style='Content.TLabel', wraplength=800)
        notification_content.pack(fill=tk.X, pady=10)

        # Attendance info section
        self.attendance_var = tk.StringVar()
        attendance_label = ttk.Label(info_frame, text="Thông tin điểm danh:", style='Content.TLabel', anchor='w')
        attendance_label.pack(fill=tk.X)
        attendance_content = ttk.Label(info_frame, textvariable=self.attendance_var, style='Content.TLabel', wraplength=800)
        attendance_content.pack(fill=tk.X, pady=10)

        # Footer with Quit Button
        footer_frame = ttk.Frame(self.window, style='TFrame', padding=10)
        footer_frame.pack(fill=tk.X, pady=10)

        quit_button = ttk.Button(footer_frame, text="Thoát", command=self.window.quit, style='TButton')
        quit_button.pack(side=tk.RIGHT, padx=20)

    def create_labeled_entry(self, parent, label_text, row):
        frame = ttk.Frame(parent, style='TFrame', padding=10)
        frame.pack(pady=10, fill=tk.X)

        label = ttk.Label(frame, text=label_text, style='Content.TLabel', width=12)
        label.pack(side=tk.LEFT)

        entry = ttk.Entry(frame, font=('Arial', 16))
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        return entry

    def create_button(self, parent, text, command):
        button = ttk.Button(parent, text=text, command=command, style='TButton', width=20)
        button.pack(pady=15)

    def show_notification(self, message):
        self.notification_var.set(message)

    def TakeImages(self):
        Id = self.id_entry.get()
        name = self.name_entry.get()
        if Id and name:
            res = capture_images(Id, name)
            self.show_notification(res)
        else:
            self.show_notification("Vui lòng nhập đầy đủ ID và tên.")

    def TrainImages(self):
        res = train_model()
        self.show_notification(res)

    def TrackImages(self):
        try:
            res = recognize_faces()
            self.attendance_var.set(str(res))
        except Exception as e:
            self.attendance_var.set(f"Lỗi: {str(e)}")

    def DeleteImages(self):
        Id = self.id_entry.get()
        if Id:
            res = delete_images(Id)
            self.show_notification(res)
        else:
            self.show_notification("Vui lòng nhập ID để xóa ảnh.")

    def export_to_excel(self):
        try:
            # Kết nối MySQL
            connection = pymysql.connect(
                host='localhost',
                user='root',  
                password='',
                database='attendance_db'
            )
            query = "SELECT * FROM Attendance"
            df = pd.read_sql(query, connection)
            connection.close()

            # Xuất file Excel
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                title="Lưu file điểm danh"
            )
            if file_path:
                df.to_excel(file_path, index=False)
                self.show_notification(f"Xuất file thành công: {file_path}")
        except Exception as e:
            self.show_notification(f"Lỗi khi xuất file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
