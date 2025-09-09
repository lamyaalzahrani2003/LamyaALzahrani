from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(0, 0)
root.configure(bg="black")

# صندوق الإدخال
e = Entry(root, bd=10, width=30, font="Arial 21", bg="lightGrey")
e.pack()

# دالة لإضافة النص في الصندوق
def click(number):
    e.insert(END, str(number))

# دالة لإضافة العمليات
def add_op(op):
    e.insert(END, op)

# دالة لمسح كل شيء
def clear():
    e.delete(0, END)

# دالة لإظهار النتيجة
def equal():
    try:
        result = eval(e.get())  # يحسب النص المكتوب
        e.delete(0, END)
        e.insert(END, str(result))
    except:
        e.delete(0, END)
        e.insert(END, "Error")

# الأزرار
btn1 = Button(root, text="7", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(7))
btn1.place(x=10, y=60)

btn2 = Button(root, text="8", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(8))
btn2.place(x=85, y=60)

btn3 = Button(root, text="9", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(9))
btn3.place(x=160, y=60)

btn4 = Button(root, text="4", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(4))
btn4.place(x=10, y=145)

btn5 = Button(root, text="5", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(5))
btn5.place(x=85, y=145)

btn6 = Button(root, text="6", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(6))
btn6.place(x=160, y=145)

btn7 = Button(root, text="1", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(1))
btn7.place(x=10, y=230)

btn8 = Button(root, text="2", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(2))
btn8.place(x=85, y=230)

btn9 = Button(root, text="3", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
              command=lambda: click(3))
btn9.place(x=160, y=230)

btn10 = Button(root, text="0", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5,
               command=lambda: click(0))
btn10.place(x=10, y=320)

# العمليات
btn11 = Button(root, text="+", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5,
               command=lambda: add_op("+"))
btn11.place(x=235, y=60)

btn14 = Button(root, text="-", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5,
               command=lambda: add_op("-"))
btn14.place(x=235, y=145)

btn15 = Button(root, text="*", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5,
               command=lambda: add_op("*"))
btn15.place(x=235, y=230)

btn16 = Button(root, text="/", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5,
               command=lambda: add_op("/"))
btn16.place(x=235, y=320)

# زر الحذف
btn12 = Button(root, text="C", font="Arial 19 bold", bg="crimson", bd=10, padx=10, pady=5,
               command=clear)
btn12.place(x=85, y=320)

# زر المساواة
btn13 = Button(root, text="=", font="Arial 19 bold", bg="khaki", bd=10, padx=10, pady=5,
               command=equal)
btn13.place(x=160, y=320)

root.mainloop()