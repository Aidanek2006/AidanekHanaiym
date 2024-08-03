class Computer:
    def __init__(self, ram, cpu, storage):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def show(self):
        return f'{self.ram}, {self.cpu}, {self.storage}'

computer1 = Computer(16, 'Intel i7', 512)
print(computer1.show())


class Laptop(Computer):
    def __init__(self, ram, cpu, storage, model):
        super().__init__(ram, cpu, storage, )
        self.model = model
    def show(self):
        return f'{self.ram}, {self.cpu}, {self.storage}'
Laptop1 = Laptop(8, 'm2', 512, 'MackBook Pro')
print(Laptop1.show())


class Desktop(Laptop):
    def __init__(self,ram, cpu, storage, model, size):
        super().__init__(ram, cpu, storage, model)
        self.size = size
    def show(self):
        return f'{self.ram}, {self.cpu}, {self.storage}, {self.model}'
Desktop1 = Desktop(12, 'intel i5', 256, 'Acer', 17)
print(Desktop1.show())
