from printers import Printers
import pprint

class Second_printers(Printers):
    def add_nuber(self, ex, ex2):
        Printers.add_number(self, ex + ex2)


if __name__ == '__main__':
    kab626 = Second_printers('xerox', 1030, 10000)
    kab627 = Second_printers('keyocera', 2540, 15000)

    print(kab626.full_name())
    kab626.add_nuber(5, 20)
    print(kab626.full_name())
    print(kab627)

