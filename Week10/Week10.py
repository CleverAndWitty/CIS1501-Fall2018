class TaxableItem():

    def __init__(self, name, price=0, tax_rate=0):
        self.name = name
        self.price = price
        if tax_rate > 1 or tax_rate < 0:
            raise ValueError("Tax rate must be between 0 and 1")
        self.tax_rate = tax_rate

    def get_total_cost(self):
        return self.price * self.tax_rate + self.price


name = "BBQ Chips"
price = 2.99
tax_rates = [ 6, 1.06, .06 ]


for tax_rate in tax_rates:
    try:
        chips = TaxableItem(name, price, tax_rate)
        print(chips.get_total_cost())
    except ValueError as e:
        print(e)
