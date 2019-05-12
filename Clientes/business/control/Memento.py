from datetime import datetime


class Memento:
    def __init__(self, state: object) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def set_state(self, state: object) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> object:
        return self._state

    def get_date(self) -> object:
        return self._date
