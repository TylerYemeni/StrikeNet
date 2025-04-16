import tkinter as tk
from tkinter import messagebox
import pygame
import os

# تشغيل الصوت
def تشغيل_الصوت(المسار):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(المسار)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"[!] فشل تشغيل الصوت: {e}")

# تنفيذ العمليات
def تنفيذ_أمر(اسم):
    messagebox.showinfo("StrikeNet", f"تم تنفيذ: {اسم}")
    تشغيل_الصوت("assets/execute.mp3")

# الواجهة
def تشغيل_الواجهة():
    pygame.init()
    root = tk.Tk()
    root.title("StrikeNet – وحدة القيادة")
    root.geometry("500x400")
    root.configure(bg="black")

    try:
        شعار = tk.PhotoImage(file="assets/logo.png")
        tk.Label(root, image=شعار, bg="black").pack(pady=10)
    except:
        tk.Label(root, text="(لا يوجد شعار)", bg="black", fg="gray").pack()

    tk.Label(root, text="مرحبًا بالقائد أبوسالم", fg="white", bg="black", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="ضربة رقمية", width=30, command=lambda: تنفيذ_أمر("ضربة رقمية")).pack(pady=5)
    tk.Button(root, text="تشغيل أداة", width=30, command=lambda: تنفيذ_أمر("تشغيل أداة")).pack(pady=5)
    tk.Button(root, text="عرض السجل", width=30, command=lambda: تنفيذ_أمر("عرض السجل")).pack(pady=5)
    tk.Button(root, text="خروج", width=30, bg="red", command=root.destroy).pack(pady=20)

    تشغيل_الصوت("assets/intro.mp3")
    root.mainloop()

if __name__ == "__main__":
    تشغيل_الواجهة()
