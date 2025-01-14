import unittest
from unittest.mock import patch
from tkinter import Tk, Entry, StringVar, Scale, OptionMenu, messagebox
import tkinter as tk

# Simulacija funkcionalnosti aplikacije
def process_order(name_entry, coffee_var, sugar_scale, addons_vars, coffee_prices, addons_prices):
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Greška", "Molimo unesite ime za čašu.")
        return

    coffee = coffee_var.get()
    try:
        sugar = int(sugar_scale.get())
    except ValueError:
        messagebox.showerror("Greška", "Unesite validan broj za šećer.")
        return

    addons = [addon for addon, var in addons_vars.items() if var.get() == 1]
    addons_total = sum(addons_prices[addon] for addon in addons)

    coffee_price = coffee_prices[coffee]
    total_price = coffee_price + addons_total

    summary = f"""
Ime na čaši: {name}
Kafa: {coffee} ({coffee_price} RSD)
Dodaci: {", ".join(addons) if addons else "Bez dodataka"}
Ukupno: {total_price} RSD
"""
    messagebox.showinfo("Porudžbina", summary)

class TestAkademskaKafica(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.root.withdraw()  # Skrivanje Tkinter prozora tokom testiranja
        self.name_entry = Entry(self.root)
        self.name_entry.insert(0, "Test Kafa")
        self.coffee_var = StringVar(value="Espreso")
        self.sugar_scale = Scale(self.root, from_=0, to=5)
        self.sugar_scale.set(2)
        self.addons_vars = {
            "Mleko": tk.IntVar(value=1),
            "Šlag": tk.IntVar(value=0),
        }
        self.coffee_prices = {
            "Espreso": 150,
            "Kapućino": 180,
        }
        self.addons_prices = {
            "Mleko": 50,
            "Šlag": 60,
        }

    def test_null_customer_name(self):
        self.name_entry.delete(0, tk.END)  # Simulacija praznog imena
        with patch('tkinter.messagebox.showerror') as mock_error:
            process_order(self.name_entry, self.coffee_var, self.sugar_scale, self.addons_vars, self.coffee_prices, self.addons_prices)
            mock_error.assert_called_with("Greška", "Molimo unesite ime za čašu.")

    def test_empty_customer_name(self):
        self.name_entry.delete(0, tk.END)  # Prazno ime
        with patch('tkinter.messagebox.showerror') as mock_error:
            process_order(self.name_entry, self.coffee_var, self.sugar_scale, self.addons_vars, self.coffee_prices, self.addons_prices)
            mock_error.assert_called_with("Greška", "Molimo unesite ime za čašu.")

    def test_true_false_addons(self):
        self.addons_vars["Mleko"].set(1)  # Mleko je izabrano
        with patch('tkinter.messagebox.showinfo') as mock_info:
            process_order(self.name_entry, self.coffee_var, self.sugar_scale, self.addons_vars, self.coffee_prices, self.addons_prices)
            mock_info.assert_called_with("Porudžbina", unittest.mock.ANY)

    def test_valid_numeric_input(self):
        self.sugar_scale.set(3)  # Validan broj za šećer
        with patch('tkinter.messagebox.showinfo') as mock_info:
            process_order(self.name_entry, self.coffee_var, self.sugar_scale, self.addons_vars, self.coffee_prices, self.addons_prices)
            mock_info.assert_called_with("Porudžbina", unittest.mock.ANY)

    def test_invalid_numeric_input(self):
        self.sugar_scale.set("invalid")  # Neispravan unos za šećer
        with patch('tkinter.messagebox.showerror') as mock_error:
            process_order(self.name_entry, self.coffee_var, self.sugar_scale, self.addons_vars, self.coffee_prices, self.addons_prices)
            mock_error.assert_called_with("Greška", "Unesite validan broj za šećer.")

if __name__ == "__main__":
    unittest.main()
