class Printers:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def __str__(self):
        return '<%s => %s %s>' % (self.__class__.__name__, self.brand, self.model)


kab315 = Printers('keyocera', 2040, 4000)
print(kab315)
