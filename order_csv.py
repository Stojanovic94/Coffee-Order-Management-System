import csv
import os
from tkinter import messagebox

class OrderCSV:
    def __init__(self, name, coffee, coffee_price, blend, sugar, addons, addons_total, total_price):
        self.name = name
        self.coffee = coffee
        self.coffee_price = coffee_price
        self.blend = blend
        self.sugar = sugar
        self.addons = addons
        self.addons_total = addons_total
        self.total_price = total_price

    def generate_csv(self):
        # Kreira CSV fajl sa imenom korisnika
        filename = f"{self.name}.csv"
        file_exists = os.path.isfile(filename)

        # Otvori fajl sa UTF-8 enkodiranjem
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Ako fajl ne postoji, napišemo zaglavlje
            if not file_exists:
                writer.writerow(["Ime na čaši", "Kafa", "Cena kafe", "Blend", "Šećer", "Dodaci", "Cena dodataka", "Ukupno"])

            # Upisujemo podatke o porudžbini
            writer.writerow([self.name, self.coffee, self.coffee_price, self.blend, self.sugar, ", ".join(self.addons) if self.addons else "Bez dodataka", self.addons_total, self.total_price])
        
        messagebox.showinfo("Porudžbina", f"CSV fajl sa porudžbinom je generisan: {filename}")
