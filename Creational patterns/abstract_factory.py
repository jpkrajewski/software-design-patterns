from abc import ABC, abstractmethod


class Button(ABC):
    ...


class WinButton(Button):
    ...


class MacButton(Button):
    ...


class SearchBar(ABC):
    ...


class WinSearchBar(SearchBar):
    ...


class MacSearchBar(SearchBar):
    ...


class GuiFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        ...

    @abstractmethod
    def create_searchbar(self) -> SearchBar:
        ...


class WinFactory(GuiFactory):
    """Create gui specific to Windows os"""
    def create_button(self) -> Button:
        return WinButton()

    def create_searchbar(self) -> SearchBar:
        return WinSearchBar()


class MacFactory(GuiFactory):
    """Create gui specific to Mac os"""
    def create_button(self) -> Button:
        return MacButton()

    def create_searchbar(self) -> SearchBar:
        return MacSearchBar()


class Application:
    factory: GuiFactory = None
    button: Button = None
    search_bar: SearchBar = None

    def __init__(self, user_os):
        self._user_os = user_os

    def create_gui(self):
        if self._user_os == 'windows':
            self.factory = WinFactory()

        if self._user_os == 'mac':
            self.factory = MacFactory()

        self.button = self.factory.create_button()
        self.search_bar = self.factory.create_searchbar()


def client_interacts(os: str):
    app = Application(os)
    app.create_gui()
    print(app.button.__class__.__name__)
    print(app.search_bar.__class__.__name__)


if __name__ == '__main__':
    client_interacts('windows')
    # WinButton
    # WinSearchBar

    client_interacts('mac')
    # MacButton
    # MacSearchBar
