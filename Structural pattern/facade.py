class Subsystem1:
    """Complex subsystem"""
    def operation_1(self):
        print(f'Performing operation 1 by {self.__class__.__name__}')

    def operation_n(self):
        print(f'Performing operation n by {self.__class__.__name__}')


class Subsystem2:
    """Complex subsystem"""
    def operation_1(self):
        print(f'Performing operation 1 by {self.__class__.__name__}')

    def operation_n(self):
        print(f'Performing operation n by {self.__class__.__name__}')


class ConverterMP4ToMP3Facade:
    """Facade to complex subsystems that convert mp4 to mp3"""
    def __init__(self, filename):
        self.filename = filename

    def convert(self):
        subsystem1 = Subsystem1()
        subsystem2 = Subsystem2()

        subsystem2.operation_1()
        subsystem1.operation_1()
        subsystem1.operation_n()
        subsystem2.operation_n()

        print(f'Converted {self.filename} to mp3')


converter = ConverterMP4ToMP3Facade('vevo doda.mp4')
converter.convert()

# Performing operation 1 by Subsystem2
# Performing operation 1 by Subsystem1
# Performing operation n by Subsystem1
# Performing operation n by Subsystem2
# Converted vevo doda.mp4 to mp3
