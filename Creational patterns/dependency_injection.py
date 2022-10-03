from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def on_connect(self):
        ...


class XboxController(Controller):
    def on_connect(self):
        print('Xbox controller connected.')


class PSController(Controller):
    def on_connect(self):
        print('PS controller connected.')


class AliExpressController(Controller):
    def on_connect(self):
        print('Cheap controller connected.')


class GamePad:
    def __init__(self, controller: Controller):
        self.controller = controller

    def show_info(self):
        self.controller.on_connect()


gp = GamePad(AliExpressController())
gp.show_info()
# Cheap controller connected.

gp = GamePad(PSController())
gp.show_info()
# PS controller connected.


gp = GamePad(XboxController())
gp.show_info()
# Xbox controller connected.
