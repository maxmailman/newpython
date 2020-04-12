class Printers:
    # Универсальное представление принтеров: данные+логика
    def __init__(self, brand, model, number, company=None):
        self.brand = brand
        self.model = model
        self.number = number
        self.company = company
        # Добавим методы

    def full_name(self):
        return self.brand + ' ' + str(self.model) + ' ' + str(self.number)

    def add_number(self, a):
        self.number += a

    def __str__(self):
        return '<%s => %s %s %s> %s' % (self.__class__.__name__, self.brand, self.model, self.number, self.company)


class Second_printers(Printers):
    def __init__(self, brand, model, number):
        Printers.__init__(self, brand, model, number, 'KrasEco')

    def add_number(self, a, b=2):
        Printers.add_number(self, a + b)


if __name__ == '__main__':
    kab315 = Printers('keyocera', 2040, 4000)
    kab625 = Second_printers('samsung', 4200, 54000)
    kab626 = Second_printers(brand='Xerox', model='4342', number=300)
    kab626.add_number(4)
    for obj in (kab315, kab625, kab626):
        print(obj)