from dataclasses import dataclass

@dataclass
class Stock:
    price: float
    stockholder_equity: list
    net_income: list
    total_shares: float

    @property
    def pe(self):
        self.net_income_last = sum(self.net_income[:4])
        self.eps = self.net_income_last / self.total_shares
        print(self.eps)
        return self.price / self.eps

    @property
    def pb(self):
        self.book_value = self.stockholder_equity[0]
        self.bvps = self.book_value / self.total_shares
        return self.price / self.bvps
    
    def __str__(self):
        net_income_last = sum(self.net_income[:4])
        eps = net_income_last / self.total_shares
        book_value = self.stockholder_equity[0]
        bvps = book_value / self.total_shares
        pe_ratio = self.price / eps
        pb_ratio = self.price / bvps
        return (f"Stock(price={self.price}, total_shares={self.total_shares}, eps={eps:.2f}, "
                f"pe={pe_ratio:.2f}, book_value={book_value}, bvps={bvps:.2f}, pb={pb_ratio:.2f})")

if __name__ == '__main__':
    # Ticker VEA
    stock = Stock(
        price=36800,
        stockholder_equity=[27163711893525],
        net_income=[1420106147334, 1559684055781, 1525485712150, 1789587057259],
        total_shares=1328800000
    )

    print(stock)