from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract class for command"""
    @abstractmethod
    def execute(self) -> None:
        ...


class PrintCommand(Command):
    """Simple print command"""
    def execute(self) -> None:
        print('Printing current file...')


class SetupLinuxServerCommand(Command):
    """Complex command that setup paid linux server"""
    def __init__(self, receiver, chosen_tier: int):
        self._receiver = receiver
        self._chosen_tier = chosen_tier

    def execute(self) -> None:
        self._receiver().setup(self._chosen_tier)


class Button:
    """GUI button mockup"""
    def __init__(self, on_click=None):
        self._on_click = on_click

    def click(self):
        self._on_click.execute()


class EditorInvoker:
    """Simple on event invoker"""
    _on_open = None
    _on_close = None

    def set_commands_on_open(self, command_list: list[Command]) -> None:
        self._on_open = command_list

    def set_commands_on_close(self, command_list: list[Command]) -> None:
        self._on_close = command_list

    def editor_opens(self) -> None:
        print('User opens editor.')
        for command in self._on_open:
            command.execute()

    def editor_closes(self) -> None:
        print('User closes editor.')
        for command in self._on_close:
            command.execute()


class LoadFontCommand(Command):
    def execute(self) -> None:
        print('Loading chosen fonts...')


class OpenRecentTabs(Command):
    def execute(self) -> None:
        print('Opening recent tabs...')


class SaveRecentTabs(Command):
    def execute(self) -> None:
        print('Saving recent tabs...')


class LinuxServerCommandReceiver:
    """Mockup of linux server creator"""
    def setup(self, tier: int):
        print('Creating environment...')
        print('Downloading updates...')
        print(f'Setting tier to {tier}..')
        print('Done')


if __name__ == '__main__':
    simple_print_btn = Button(on_click=PrintCommand())
    simple_print_btn.click()
    # Printing current file...

    create_linux_server_btn = Button(on_click=SetupLinuxServerCommand(receiver=LinuxServerCommandReceiver, chosen_tier=3))
    create_linux_server_btn.click()
    # Creating environment...
    # Downloading updates...
    # Setting tier to 3..
    # Done

    editor_invoker = EditorInvoker()
    editor_invoker.set_commands_on_open([LoadFontCommand(), OpenRecentTabs()])
    editor_invoker.set_commands_on_close([SaveRecentTabs()])
    editor_invoker.editor_opens()
    editor_invoker.editor_closes()
    # User opens editor.
    # Loading chosen fonts...
    # Opening recent tabs...
    # User closes editor.
    # Saving recent tabs...

