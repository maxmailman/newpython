from printers import Printers
# Специализация конструктора


class Second_printers(Printers):

    def __init__(self, brand, model):
        Printers.__init__(self, brand, model, 'KrasEco')

    def __str__(self):
        return '<%s => %s %s>' % (self.__class__.__name__, self.brand, self.model)


if __name__ == '__main__':
    kab626 = Second_printers('xerox', 1030)
    kab627 = Second_printers('keyocera', 2540)

    print(kab626.number)
    print(kab626)