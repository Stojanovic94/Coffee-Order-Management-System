class Order:
    def __init__(self, name, coffee, sugar, blend, addons):
        self.name = name
        self.coffee = coffee
        self.sugar = sugar
        self.blend = blend
        self.addons = addons
        self.coffee_prices = {
            "Espreso": 150,
            "Kapućino": 180,
            "Makijato": 170,
            "Latte": 190,
            "Mocha": 200,
        }
        self.addons_prices = {
            "Mleko": 50,
            "Šlag": 60,
            "Rum": 70,
            "Cimet": 50,
            "Espreso šot": 80,
        }

    def calculate_total_price(self):
        coffee_price = self.coffee_prices.get(self.coffee, 0)
        addons_total = sum(self.addons_prices[addon] for addon in self.addons)
        total_price = coffee_price + addons_total
        return total_price

    def generate_summary(self):
        addons_str = ", ".join(self.addons) if self.addons else "Bez dodataka"
        total_price = self.calculate_total_price()
        return f"""
Ime na čaši: {self.name}
Kafa: {self.coffee} ({self.coffee_prices[self.coffee]} RSD)
Blend: {self.blend}
Šećer: {self.sugar} kašičica/e
Dodaci: {addons_str}
Ukupno: {total_price} RSD
"""
