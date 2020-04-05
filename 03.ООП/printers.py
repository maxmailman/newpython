class Printers:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number
        # Добавим методы
    def full_name(self):
        return self.brand + ' ' + str(self.model) + ' ' + str(self.number)
    def add_number(self, a):
        self.number += a

if __name__ == '__main__':
    kab315 = Printers('keyocera', 2040, 4000)
    kab625 = Printers('samsung', 4200, 54000)
    kab626 = Printers('xerox', 1030, 10000)
    kab627 = Printers('keyocera', 2540, 15000)

    print(kab315.brand, kab315.model)
    print('Теперь методы')
    print(kab627.full_name())
    kab627.add_number(1000)
    print(kab627.number)

