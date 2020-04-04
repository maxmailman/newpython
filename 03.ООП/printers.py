class Printers:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

if __name__ == '__main__':
    kab315 = Printers('keyocera', 2040, 4000)
    kab625 = Printers('samsung', 4200, 54000)
    kab626 = Printers('xerox', 1030, 10000)
    kab627 = Printers('keyocera', 2540, 15000)

    print(kab315.brand, kab315.model)
    print(kab627.model)

