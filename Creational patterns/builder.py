
class ComputerBuilder:
    """Base class builder for computer"""
    model = None
    settings = {}

    def reset(self):
        self.settings = {}

    def set_cpu(self, name):
        self.settings['cpu'] = name

    def set_gpu(self, name):
        self.settings['gpu'] = name

    def set_ram(self, name):
        self.settings['ram'] = name

    def set_storage(self, name):
        self.settings['storage'] = name

    def get_result(self):
        return self.model(**self.settings)


class Computer:
    """Base class"""
    def __init__(self, cpu=None, gpu=None, ram=None, storage=None):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f'{self.__class__.__name__}: {self.cpu} = cpu, {self.gpu} = gpu, {self.ram} = ram, {self.storage} = storage'


class Laptop(Computer):
    pass


class PC(Computer):
    pass


class LaptopBuilder(ComputerBuilder):
    model = Laptop


class PCBuilder(ComputerBuilder):
    model = PC


class Director:
    """Let's us build predefined objects"""
    def make_simple_pc(self, builder: ComputerBuilder) -> Computer:
        pcbuilder = builder()
        pcbuilder.reset()
        pcbuilder.set_cpu('Intel i7')
        pcbuilder.set_gpu('nVidia GTX 570')
        pcbuilder.set_ram('18GB ram')
        pcbuilder.set_storage('1TB samsung')
        return pcbuilder.get_result()

    def make_simple_pc_without_gpu(self, builder: ComputerBuilder) -> Computer:
        pcbuilder = builder()
        pcbuilder.reset()
        pcbuilder.set_cpu('Intel i8')
        pcbuilder.set_ram('8GB ram')
        pcbuilder.set_storage('1TB samsung')
        return pcbuilder.get_result()


director = Director()
simple_pc = director.make_simple_pc(PCBuilder)
print(simple_pc)

simple_pc = director.make_simple_pc_without_gpu(PCBuilder)
print(simple_pc)

custom_laptop_builder = LaptopBuilder()
custom_laptop_builder.set_cpu('AMD XPRO 1400')
custom_laptop_builder.set_ram('8GB')
custom_laptop = custom_laptop_builder.get_result()
print(custom_laptop)

# PC: Intel i7 = cpu, nVidia GTX 570 = gpu, 18GB ram = ram, 1TB samsung = storage
# PC: Intel i8 = cpu, None = gpu, 8GB ram = ram, 1TB samsung = storage
# Laptop: AMD XPRO 1400 = cpu, None = gpu, 8GB = ram, None = storage
