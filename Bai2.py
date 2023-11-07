import tkinter as tk
import sympy as sym

def daoham():
    ham = ham_input.get()
    x = sym.Symbol('x')
    fx = sym.sympify(ham)
    daoham = sym.diff(fx, x)
    kqua.configure(text=f"Đạo hàm: {daoham}")

def tichphan():
    ham = ham_input.get()
    x = sym.Symbol('x')
    fx = sym.sympify(ham)
    tichphan = sym.integrate(fx, x)
    kqua.configure(text=f"Tích phân: {tichphan}")

def ghan():
    ham = ham_input.get()
    x = sym.Symbol('x')
    fx = sym.sympify(ham)
    ghan = sym.limit(fx, x, 0)
    kqua.configure(text=f"Giới hạn: {ghan}")

def rutgon():
    ham = ham_input.get()
    x = sym.Symbol('x')
    fx = sym.sympify(ham)
    rutgon = sym.simplify(fx)
    kqua.configure(text=f"Biểu thức rút gọn: {rutgon}")
window = tk.Tk()
window.title("Ứng dụng hỗ trợ môn giải tích")
window.geometry('500x200')

ham_frame = tk.Frame(window)
ham_frame.place(x=10, y=10)

ham_label = tk.Label(ham_frame, text="Biểu thức hàm số:")
ham_label.pack(side=tk.LEFT)

ham_input = tk.Entry(ham_frame)
ham_input.pack(side=tk.LEFT)

tdaoham = tk.Button(window, text="Tính đạo hàm", command=daoham)
tdaoham.place(x=10, y=50)

ttichphan = tk.Button(window, text="Tính tích phân", command=tichphan)
ttichphan.place(x=120, y=50)

tghan = tk.Button(window, text="Tính giới hạn", command=ghan)
tghan.place(x=230, y=50)

trutgon = tk.Button(window, text="Rút gọn biểu thức", command=rutgon)
trutgon.place(x=350, y=50)

kqua = tk.Label(window, text="Kết quả:")
kqua.place(x=10, y=90)

window.mainloop()
