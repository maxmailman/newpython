from printers import Printers

kab315 = Printers('keyocera', 2040, 4000)
kab625 = Printers('samsung', 4200, 54000)
kab626 = Printers('xerox', 1030, 10000)
kab627 = Printers('keyocera', 2540, 15000)

printers_all = [kab315, kab625, kab626, kab627]

for p in printers_all:
    print(p.brand, p.model)

print([(p.brand, p.model, p.number) for p in printers_all])

print([(rec.brand, rec.number) for rec in printers_all if rec.model == 2540])
