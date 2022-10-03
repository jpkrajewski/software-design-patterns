from typing import List
from abc import ABC, abstractmethod
from datetime import datetime as dt


class Memento(ABC):
    """Stores past state of originator"""
    @abstractmethod
    def restore(self):
        pass


class Originator(ABC):
    """Holds important data that can change over time"""
    @abstractmethod
    def save(self) -> Memento:
        pass


class NoteMemento(Memento):
    def __init__(self, notepad: Originator, state: str, date: dt):
        self.notepad = notepad
        self.state = state
        self.date = date

    def restore(self) -> None:
        self.notepad.set_state(self.state)

    def __str__(self):
        return f'{self.state} / {self.date}'


class NotePad(Originator):
    def __init__(self):
        self.state = ''

    def write(self, text: str) -> None:
        self.state += text
        print(f'State changed... Notepad state: |{self.state}|')

    def save(self) -> NoteMemento:
        print('Saving state...')
        return NoteMemento(self, self.state, dt.now())

    def set_state(self, state) -> None:
        self.state = state
        print(f'Rollback... Notepad state: |{self.state}| ')


class NotepadCaretaker:
    def __init__(self, notepad: NotePad):
        self.notepad = notepad
        self.history: List[Memento] = []

    def undo(self):
        if len(self.history) > 0:
            self.history.pop().restore()

    def save_state(self):
        self.history.append(self.notepad.save())

    def show_changes(self):
        print('Changes: ')
        for mem in self.history:
            print(f'    {mem}')


notepad_app = NotePad()
caretaker = NotepadCaretaker(notepad_app)

notepad_app.write('First paragraph.')
notepad_app.write(' Second paragraph.')
caretaker.save_state()
notepad_app.write(' Third paragraph.')
caretaker.save_state()
notepad_app.write(' Fourth paragraph. jfsdf')
caretaker.show_changes()
caretaker.undo()
caretaker.undo()

# State changed... Notepad state: |First paragraph.|
# State changed... Notepad state: |First paragraph. Second paragraph.|
# Saving state...
# State changed... Notepad state: |First paragraph. Second paragraph. Third paragraph.|
# Saving state...
# State changed... Notepad state: |First paragraph. Second paragraph. Third paragraph. Fourth paragraph. jfsdf|
# Changes:
#     First paragraph. Second paragraph. / 2022-09-25 09:38:58.998182
#     First paragraph. Second paragraph. Third paragraph. / 2022-09-25 09:38:58.998182
# Rollback... Notepad state: |First paragraph. Second paragraph. Third paragraph.|
# Rollback... Notepad state: |First paragraph. Second paragraph.|
