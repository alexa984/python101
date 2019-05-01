class Computer:
    _RAM = 0
    _HDD = 0
    _CPU_cores = 0

    def __str__(self):
        return "RAM: {}GB, HDD: {}GB, CPU: {} cores". format(self._RAM, self._HDD, self._CPU_cores)
    def get_RAM(self):
        return self._RAM

    def get_HDD(self):
        return self._HDD

    def get_CPU(self):
        return self._CPU_cores


class PC(Computer):
    _RAM = 4
    _HDD = 750
    _CPU = 2

class Laptop(Computer):
    _RAM = 8
    _HDD = 1000
    _CPU = 8
class Server(Computer):
    _RAM = 64
    _HDD = 500
    _CPU = 16

class ComputerFactory():
    def create_computer(self, type_computer):
        return globals()[type_computer]()

computer = ComputerFactory()
my_computers = ['Laptop', 'Laptop', 'PC', 'Server', 'Laptop']
for cp in my_computers:
    this_computer = computer.create_computer(cp)
    print(this_computer)