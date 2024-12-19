import cv2
import pandas as pd
import os
import time
import datetime
import numpy as np
import pymysql

def recognize_faces():
    print("Đang đọc file CSV...")

    # Đọc dữ liệu từ file CSV, nếu file không tồn tại, tạo file mới
    attendance_file = "Attendance/Attendance.csv"

    if not os.path.exists(attendance_file):
        attendance = pd.DataFrame(columns=['Id', 'Name', 'Date', 'Time'])
    else:
        attendance = pd.read_csv(attendance_file)

    print("Nội dung của DataFrame:")
    print(attendance)

    # Đọc file chi tiết sinh viên
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    print("Nội dung của DataFrame sinh viên:")
    print(df)

    if 'Id' not in df.columns or 'Name' not in df.columns:
        if '01' in df.columns and 'pta' in df.columns:
            df = df.rename(columns={'01': 'Id', 'pta': 'Name'})
        elif 'ID' in df.columns:
            df = df.rename(columns={'ID': 'Id'})
        else:
            raise KeyError("Không tìm thấy cột 'Id' hoặc 'Name' trong DataFrame")

    df['Id'] = df['Id'].astype(str)

    # Kết nối với MySQL
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='attendance_db'  # Tên cơ sở dữ liệu
    )
    cursor = connection.cursor()

    # Tạo bảng nếu chưa có
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Attendance (
        Id VARCHAR(50),
        Name VARCHAR(100),
        Date DATE,
        Time TIME
    );
    """)
    connection.commit()

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            print(f"Recognized ID: {Id}, Confidence: {conf}")

            if conf < 70:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                Id = str(Id)
                aa = df.loc[df['Id'] == Id]['Name'].values
                if len(aa) > 0:
                    tt = f"{Id}-{aa[0]}"
                    name = aa[0]
                else:
                    tt = f"{Id}-Unknown"
                    name = 'Unknown'
                print(f"Matched Name: {name}")

                if Id not in attendance['Id'].values:
                    attendance.loc[len(attendance)] = [Id, name, date, timeStamp]

                    # Lưu vào cơ sở dữ liệu
                    cursor.execute("""
                    INSERT INTO Attendance (Id, Name, Date, Time)
                    VALUES (%s, %s, %s, %s)
                    """, (Id, name, date, timeStamp))
                    connection.commit()
                    print(f"Thêm vào MySQL: {Id}, {name}, {date}, {timeStamp}")
                else:
                    print(f"Người này đã được điểm danh trước đó: {name}")

                attendance.to_csv(attendance_file, index=False)
                print(f"Dữ liệu đã được lưu vào {attendance_file}")

            else:
                Id = 'Unknown'
                tt = str(Id)

            if conf > 90:
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite(f"ImagesUnknown/Image{noOfFile}.jpg", im[y:y + h, x:x + w])

            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)

        cv2.imshow('im', im)
        if cv2.waitKey(1) == ord('q'):
            print("Lưu thông tin điểm danh...")
            break

    cam.release()
    cv2.destroyAllWindows()
    cursor.close()
    connection.close()
    return attendance


if __name__ == "__main__":
    result = recognize_faces()
    print(result)
