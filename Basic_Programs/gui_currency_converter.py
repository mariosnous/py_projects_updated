import customtkinter
from tkinter import *
from forex_python.converter import CurrencyRates


app = customtkinter.CTk()
app.config(bg="#202630")
app.geometry("400x450")
app.title("Currency Converter")
img = PhotoImage(file="My project.png")
img_label = customtkinter.CTkLabel(app, fg_color="#202630", image=img)
img_label.place(x=0, y=0)
app.iconphoto(False, img)

from_label = customtkinter.CTkLabel(
    app, text="From", fg_color="#202630")
from_label.place(x=10, y=150)
to_label = customtkinter.CTkLabel(app, text="To", fg_color="#202630")
to_label.place(x=248, y=150)

currency_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "GBP"]

variable1 = StringVar()
variable2 = StringVar()
txt = StringVar()


def convert():
    from_currency = variable1.get()
    to_currency = variable2.get()
    c = CurrencyRates()
    amt = c.convert(from_currency, to_currency, float(amount_entry.get()))
    amount = float("{:.3f}".format(amt))
    result_label = customtkinter.CTkLabel(
        app, textvariable=txt, text_color="#ffffff")
    result_label.place(x=130, y=350)
    txt.set(amount)


def reset():
    amount_entry.delete(0, END)


from_menu = customtkinter.CTkComboBox(
    app, variable=variable1, values=currency_list)
from_menu.place(x=10, y=180)

to_menu = customtkinter.CTkComboBox(
    app, variable=variable2, values=currency_list)
to_menu.place(x=250, y=180)


amount_entry = customtkinter.CTkEntry(
    app, text_color="#000000", justify=CENTER, width=370, fg_color="#ffffff")
amount_entry.place(x=18, y=240)


convert_button = customtkinter.CTkButton(app, command=convert, text="Convert")
reset_button = customtkinter.CTkButton(app, command=reset, text="Reset")
convert_button.place(x=50, y=300)
reset_button.place(x=200, y=300)


app.mainloop()
