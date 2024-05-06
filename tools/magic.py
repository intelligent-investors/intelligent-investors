from dataclasses import dataclass

@dataclass
class Stock:
    price: float
    earning: float
    book_value: float

    @property
    def pe(self):
        return self.price / self.earning

    @property
    def pb(self):
        return self.price / self.book_value

# Creating an instance of Stock with the provided data
stock = Stock(price=36.8, earning=4.737, book_value=20.442)

# Accessing and printing P/E and P/B ratios using the properties
print('P/E:', stock.pe)
print('P/B:', stock.pb)