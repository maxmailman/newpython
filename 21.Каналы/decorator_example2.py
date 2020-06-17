class Order:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError('Неверное значение')
        self._quantity = value


apple_order = Order('apple', 1, 10)
apple_order.quantity = -10
print(apple_order.quantity)
