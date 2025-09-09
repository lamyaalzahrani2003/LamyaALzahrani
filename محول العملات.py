import tkinter as tk
from tkinter import ttk, messagebox

# أسعار الصرف مقابل الدولار الأمريكي (مثال تقريبي)
exchange_rates = {
    "USD": 1,
    "SAR": 3.75,
    "EGP": 30.9,
    "KWD": 0.31,
    "AED": 3.67,
    "TRY": 27.5
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_cb.get()
        to_currency = to_currency_cb.get()
        
        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            messagebox.showerror("خطأ", "اختر عملة صحيحة")
            return
        
        # التحويل أولاً إلى الدولار ثم للعملة المطلوبة
        amount_in_usd = amount / exchange_rates[from_currency]
        converted_amount = amount_in_usd * exchange_rates[to_currency]
        
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("خطأ", "ادخل رقم صحيح")

# إنشاء نافذة البرنامج
root = tk.Tk()
root.title("تحويل العملات")
root.geometry("400x250")
root.resizable(False, False)

# العنوان
title_label = tk.Label(root, text="تحويل العملات", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# إدخال المبلغ
amount_label = tk.Label(root, text="المبلغ:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# اختيار العملة من
from_currency_cb = ttk.Combobox(root, values=list(exchange_rates.keys()))
from_currency_cb.set("USD")
from_currency_cb.pack(pady=5)

# اختيار العملة إلى
to_currency_cb = ttk.Combobox(root, values=list(exchange_rates.keys()))
to_currency_cb.set("SAR")
to_currency_cb.pack(pady=5)

# زر التحويل
convert_button = tk.Button(root, text="تحويل", command=convert_currency)
convert_button.pack(pady=10)

# نتيجة التحويل
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()


