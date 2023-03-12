class Mebel:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
        self.count = 0

    def __setattr__(self, key, value):
        if not isinstance(value, str) and key == 'name':
            raise ValueError('Надо строку')
        if not isinstance(value, int) and key == 'cost':
            raise ValueError('Надо число')
        object.__setattr__(self, key, value)


class Card:
    def __init__(self):
        self.a = []

    def add(self, x):
        if x not in self.a:
            self.a.append(x)
            x.count += 1
        else:
            x.count += 1

    def show(self):
        print([f'Название: {i.name}, цена: {i.cost} рублей, количество: {i.count}' for i in self.a])

    def delete(self, x):
        if x.count > 1:
            x.count -= 1
        else:
            self.a.remove(x)


mb = Mebel(20, 'Диван')
mb1 = Mebel(30, 'Стул')
c = Card()
c.add(mb)
c.add(mb)
c.add(mb1)
c.add(mb1)
c.delete(mb1)
c.delete(mb1)
c.show()

