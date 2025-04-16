import tkinter as tk
from tkinter import messagebox
import base64
import os
from playsound import playsound

# تشغيل صوت عند التشغيل (بصيغة mp3)
def تشغيل_الصوت():
    try:
        playsound("assets/intro.mp3")
    except:
        pass

# تنفيذ العمليات
def تنفيذ_عملية(اسم):
    messagebox.showinfo("StrikeNet", f"تم تنفيذ: {اسم}")
    try:
        playsound("assets/execute.mp3")
    except:
        pass

# الواجهة
def بناء_الواجهة():
    root = tk.Tk()
    root.title("StrikeNet – قيادة أبوسالم")
    root.geometry("500x400")
    root.configure(bg="black")

    شعار = tk.PhotoImage(file="assets/logo.png")
    tk.Label(root, image=شعار, bg="black").pack(pady=10)

    tk.Label(root, text="مرحباً بالقائد أبوسالم", fg="white", bg="black", font=("Helvetica", 14)).pack()

    tk.Button(root, text="تشغيل ضربة رقمية", command=lambda: تنفيذ_عملية("ضربة رقمية"), width=30).pack(pady=10)
    tk.Button(root, text="تشغيل أداة خارجية", command=lambda: تنفيذ_عملية("أداة خارجية"), width=30).pack(pady=10)
    tk.Button(root, text="عرض سجل العمليات", command=lambda: تنفيذ_عملية("عرض السجل"), width=30).pack(pady=10)
    tk.Button(root, text="خروج", command=root.destroy, width=30, bg="red").pack(pady=20)

    تشغيل_الصوت()
    root.mainloop()

بناء_الواجهة()
