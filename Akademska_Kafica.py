import tkinter as tk
from tkinter import messagebox
from order_csv import OrderCSV  # Importujemo klasu OrderCSV

# Funkcija za resetovanje unosa
def reset():
    name_entry.delete(0, tk.END)
    coffee_var.set("Espreso")
    sugar_scale.set(0)
    blend_var.set("Arabica 100%")
    for addon in addons_vars:
        addons_vars[addon].set(0)
    messagebox.showinfo("Reset", "Unos je resetovan.")

# Funkcija za obradu trenutne porudžbine
def process_order():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Greška", "Molimo unesite ime za čašu.")
        return

    coffee = coffee_var.get()
    sugar = sugar_scale.get()
    blend = blend_var.get()
    addons = [addon for addon, var in addons_vars.items() if var.get() == 1]
    addons_total = sum(addons_prices[addon] for addon in addons)

    coffee_price = coffee_prices[coffee]
    total_price = coffee_price + addons_total

    summary = f"""
Ime na čaši: {name}
Kafa: {coffee} ({coffee_price} RSD)
Blend: {blend}
Šećer: {sugar} kašičica/e
Dodaci: {", ".join(addons) if addons else "Bez dodataka"}
Ukupno: {total_price} RSD
"""
    messagebox.showinfo("Porudžbina", summary)

    # Generisanje CSV fajla sa porudžbinom
    order_csv = OrderCSV(name, coffee, coffee_price, blend, sugar, addons, addons_total, total_price)
    order_csv.generate_csv()

# Osnovne cene kafa
coffee_prices = {
    "Espreso": 150,
    "Kapućino": 180,
    "Makijato": 170,
    "Latte": 190,
    "Mocha": 200,
}

# Cene dodataka
addons_prices = {
    "Mleko": 50,
    "Šlag": 60,
    "Rum": 70,
    "Cimet": 50,
    "Espreso šot": 80,
}

# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Akademska Kafica")

# Naslov i logo
logo_frame = tk.Frame(root)
logo_frame.pack(pady=10)
logo = tk.PhotoImage(file="img/logo.png")  # Zamenite sa stvarnom putanjom do logotipa
tk.Label(logo_frame, image=logo).pack()
tk.Label(logo_frame, text="Akademska Kafica", font=("Arial", 20, "bold")).pack()

# Polje za ime korisnika
name_frame = tk.Frame(root)
name_frame.pack(pady=5)
tk.Label(name_frame, text="Ime na čaši:").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(name_frame, width=30)
name_entry.grid(row=0, column=1)

# Padajuća lista za tip kafe
coffee_frame = tk.Frame(root)
coffee_frame.pack(pady=5)
tk.Label(coffee_frame, text="Izaberite kafu:").grid(row=0, column=0, padx=5)
coffee_var = tk.StringVar(value="Espreso")
coffee_menu = tk.OptionMenu(coffee_frame, coffee_var, *coffee_prices.keys())
coffee_menu.grid(row=0, column=1)

# Polje za šećer
sugar_frame = tk.Frame(root)
sugar_frame.pack(pady=5)
tk.Label(sugar_frame, text="Kašičice šećera (0-5):").grid(row=0, column=0, padx=5)
sugar_scale = tk.Scale(sugar_frame, from_=0, to=5, orient=tk.HORIZONTAL)
sugar_scale.grid(row=0, column=1)

# Dugmad za blend
blend_frame = tk.Frame(root)
blend_frame.pack(pady=5)
tk.Label(blend_frame, text="Odaberite blend:").grid(row=0, column=0, padx=5)
blend_var = tk.StringVar(value="Arabica 100%")
tk.Radiobutton(blend_frame, text="Arabica 100%", variable=blend_var, value="Arabica 100%").grid(row=0, column=1)
tk.Radiobutton(blend_frame, text="Balkan Blend", variable=blend_var, value="Balkan Blend").grid(row=0, column=2)

# Dugmad za dodatke
addons_frame = tk.Frame(root)
addons_frame.pack(pady=5)
tk.Label(addons_frame, text="Dodaci:").grid(row=0, column=0, padx=5, sticky="w")
addons_vars = {addon: tk.IntVar() for addon in addons_prices}
col = 1
for addon, var in addons_vars.items():
    tk.Checkbutton(addons_frame, text=f"{addon} ({addons_prices[addon]} RSD)", variable=var).grid(row=0, column=col, sticky="w")
    col += 1

# Dugmad za kontrolu
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)
tk.Button(buttons_frame, text="Nova porudžbina", command=reset, bg="lightblue").grid(row=0, column=0, padx=5)
tk.Button(buttons_frame, text="Obradi porudžbinu", command=process_order, bg="lightgreen").grid(row=0, column=1, padx=5)
tk.Button(buttons_frame, text="Reset unosa", command=reset, bg="lightcoral").grid(row=0, column=2, padx=5)

# Pokretanje aplikacije
root.mainloop()

def main():
    # Ovde stavite kod za pokretanje aplikacije (npr. GUI)
    print("Pokreće se aplikacija 'Akademska Kafica'...")

if __name__ == "__main__":
    main()
