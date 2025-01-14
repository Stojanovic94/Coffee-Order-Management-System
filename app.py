import tkinter as tk
from tkinter import messagebox
from order import Order

class CoffeeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Akademska Kafica")

        self.name_entry = None
        self.coffee_var = None
        self.sugar_scale = None
        self.blend_var = None
        self.addons_vars = {}

        self.create_ui()

    def create_ui(self):
        # Naslov i logo
        logo_frame = tk.Frame(self.root)
        logo_frame.pack(pady=10)
        logo = tk.PhotoImage(file="img/logo.png")  # Zamenite sa stvarnom putanjom do logotipa
        tk.Label(logo_frame, image=logo).pack()
        tk.Label(logo_frame, text="Akademska Kafica", font=("Arial", 20, "bold")).pack()

        # Polje za ime korisnika
        name_frame = tk.Frame(self.root)
        name_frame.pack(pady=5)
        tk.Label(name_frame, text="Ime na čaši:").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(name_frame, width=30)
        self.name_entry.grid(row=0, column=1)

        # Padajuća lista za tip kafe
        coffee_frame = tk.Frame(self.root)
        coffee_frame.pack(pady=5)
        tk.Label(coffee_frame, text="Izaberite kafu:").grid(row=0, column=0, padx=5)
        self.coffee_var = tk.StringVar(value="Espreso")
        coffee_menu = tk.OptionMenu(coffee_frame, self.coffee_var, *Order(None, None, None, None, None).coffee_prices.keys())
        coffee_menu.grid(row=0, column=1)

        # Polje za šećer
        sugar_frame = tk.Frame(self.root)
        sugar_frame.pack(pady=5)
        tk.Label(sugar_frame, text="Kašičice šećera (0-5):").grid(row=0, column=0, padx=5)
        self.sugar_scale = tk.Scale(sugar_frame, from_=0, to=5, orient=tk.HORIZONTAL)
        self.sugar_scale.grid(row=0, column=1)

        # Dugmad za blend
        blend_frame = tk.Frame(self.root)
        blend_frame.pack(pady=5)
        tk.Label(blend_frame, text="Odaberite blend:").grid(row=0, column=0, padx=5)
        self.blend_var = tk.StringVar(value="Arabica 100%")
        tk.Radiobutton(blend_frame, text="Arabica 100%", variable=self.blend_var, value="Arabica 100%").grid(row=0, column=1)
        tk.Radiobutton(blend_frame, text="Balkan Blend", variable=self.blend_var, value="Balkan Blend").grid(row=0, column=2)

        # Dugmad za dodatke
        addons_frame = tk.Frame(self.root)
        addons_frame.pack(pady=5)
        tk.Label(addons_frame, text="Dodaci:").grid(row=0, column=0, padx=5, sticky="w")
        addons_prices = Order(None, None, None, None, None).addons_prices
        self.addons_vars = {addon: tk.IntVar() for addon in addons_prices}
        col = 1
        for addon, var in self.addons_vars.items():
            tk.Checkbutton(addons_frame, text=f"{addon} ({addons_prices[addon]} RSD)", variable=var).grid(row=0, column=col, sticky="w")
            col += 1

        # Dugmad za kontrolu
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)
        tk.Button(buttons_frame, text="Nova porudžbina", command=self.reset, bg="lightblue").grid(row=0, column=0, padx=5)
        tk.Button(buttons_frame, text="Obradi porudžbinu", command=self.process_order, bg="lightgreen").grid(row=0, column=1, padx=5)
        tk.Button(buttons_frame, text="Reset unosa", command=self.reset, bg="lightcoral").grid(row=0, column=2, padx=5)

    def reset(self):
        self.name_entry.delete(0, tk.END)
        self.coffee_var.set("Espreso")
        self.sugar_scale.set(0)
        self.blend_var.set("Arabica 100%")
        for addon in self.addons_vars.values():
            addon.set(0)
        messagebox.showinfo("Reset", "Unos je resetovan.")

    def process_order(name_entry, coffee_var, sugar_scale, addons_vars, coffee_prices, addons_prices):
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Greška", "Molimo unesite ime za čašu.")
        return

    # Proveriti da li je šećer validan broj
    try:
        sugar = float(sugar_scale.get())
    except ValueError:
        messagebox.showerror("Greška", "Unesite validan broj za šećer.")
        return

    coffee = coffee_var.get()
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

