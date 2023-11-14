import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

def draw_line():
    x = np.linspace(-10, 10, 100)
    y = x  # Ví dụ vẽ đường thẳng y = x
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Đường thẳng')
    plt.grid(True)
    plt.show()

def calculate_distance():
    x1 = float(entry_x1.get())
    y1 = float(entry_y1.get())
    x2 = float(entry_x2.get())
    y2 = float(entry_y2.get())
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    messagebox.showinfo("Kết quả", "Khoảng cách giữa hai điểm A và B: {}".format(distance))

def calculate_area():
    shape = entry_shape.get().lower()
    if shape == "hình chữ nhật":
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        messagebox.showinfo("Kết quả", "Diện tích hình chữ nhật: {}".format(area))
    elif shape == "hình tam giác":
        base = float(entry_base.get())
        height = float(entry_height.get())
        area = 0.5 * base * height
        messagebox.showinfo("Kết quả", "Diện tích hình tam giác: {}".format(area))
    elif shape == "hình tròn":
        radius = float(entry_radius.get())
        area = np.pi * radius**2
        messagebox.showinfo("Kết quả", "Diện tích hình tròn: {}".format(area))
    # Thêm các loại hình khác

def calculate_perimeter():
    shape = entry_shape.get().lower()
    if shape == "hình chữ nhật":
        length = float(entry_length.get())
        width = float(entry_width.get())
        perimeter = 2 * (length + width)
        messagebox.showinfo("Kết quả", "Chu vi hình chữ nhật: {}".format(perimeter))
    elif shape == "hình tam giác":
        side1 = float(entry_side1.get())
        side2 = float(entry_side2.get())
        side3 = float(entry_side3.get())
        perimeter = side1 + side2 + side3
        messagebox.showinfo("Kết quả", "Chu vi hình tam giác: {}".format(perimeter))
    elif shape == "hình tròn":
        radius = float(entry_radius.get())
        perimeter = 2 * np.pi * radius
        messagebox.showinfo("Kết quả", "Chu vi hình tròn: {}".format(perimeter))
    # Thêm các loại hình khác

def calculate_volume():
    shape = entry_shape.get().lower()
    if shape == "hình hộp chữ nhật":
        length = float(entry_length.get())
        width = float(entry_width.get())
        height = float(entry_height.get())
        volume = length * width * height
        messagebox.showinfo("Kết quả", "Thể tích hình hộp chữ nhật: {}".format(volume))
    elif shape == "hình hình cầu":
        radius = float(entry_radius.get())
        volume = (4 / 3) * np.pi * radius**3
        messagebox.showinfo("Kết quả", "Thể tích hình hình cầu: {}".format(volume))
    # Thêm các loại hình khác

def main():
    root = Tk()
    root.title("Chương trình ứng dụng hình học")
    
    label_shape = Label(root, text="Nhập tên hình:")
    label_shape.grid(row=0, column=0, sticky="w")
    entry_shape = Entry(root)
    entry_shape.grid(row=0, column=1)

    label_length = Label(root, text="Chiều dài:")
    label_length.grid(row=1, column=0, sticky="w")
    entry_length = Entry(root)
    entry_length.grid(row=1, column=1)

    label_width = Label(root, text="Chiều rộng:")
    label_width.grid(row=2, column=0, sticky="w")
    entry_width = Entry(root)
    entry_width.grid(row=2, column=1)

    label_base = Label(root, text="Cạnh đáy:")
    label_base.grid(row=3, column=0, sticky="w")
    entry_base = Entry(root)
    entry_base.grid(row=3, column=1)

    label_height = Label(root, text="Chiều cao:")
    label_height.grid(row=4, column=0, sticky="w")
    entry_height = Entry(root)
    entry_height.grid(row=4, column=1)

    label_radius = Label(root, text="Bán kính:")
    label_radius.grid(row=5, column=0, sticky="w")
    entry_radius = Entry(root)
    entry_radius.grid(row=5, column=1)

    label_x1 = Label(root, text="Tọa độ x1:")
    label_x1.grid(row=6, column=0, sticky="w")
    entry_x1 = Entry(root)
    entry_x1.grid(row=6, column=1)

    label_y1 = Label(root, text="Tọa độ y1:")
    label_y1.grid(row=7, column=0, sticky="w")
    entry_y1 = Entry(root)
    entry_y1.grid(row=7, column=1)

    label_x2 = Label(root, text="Tọa độ x2:")
    label_x2.grid(row=8, column=0, sticky="w")
    entry_x2 = Entry(root)
    entry_x2.grid(row=8, column=1)

    label_y2 = Label(root, text="Tọa độ y2:")
    label_y2.grid(row=9, column=0, sticky="w")
    entry_y2 = Entry(root)
    entry_y2.grid(row=9, column=1)

    Button(root, text="Vẽ đường thẳng", command=draw_line).grid(row=10, column=0)
    Button(root, text="Tính khoảng cách", command=calculate_distance).grid(row=10, column=1)
    Button(root, text="Tính diện tích", command=calculate_area).grid(row=11, column=0)
    Button(root, text="Tính chu vi", command=calculate_perimeter).grid(row=11, column=1)
    Button(root, text="Tính thể tích", command=calculate_volume).grid(row=12, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()