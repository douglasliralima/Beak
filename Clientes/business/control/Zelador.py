import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Fonte import Fonte
from business.control.Memento import Memento


class Zelador:
    def __init__(self, fonte: Fonte) -> None:
        self._mementos = []
        self._fonte = fonte

    def save_state(self, state: object) -> None:
        self._mementos.append(self._fonte.create_state_memento())
        self._fonte.restore_state(Memento(state))

    def undo_state(self) -> None:
        if not self._mementos:
            return None

        previous_memento = self._mementos.pop()

        try:
            self._fonte.restore_state(previous_memento)
        except Exception:
            self.undo_state()

    def getFonte(self) -> Fonte:
        return self.__fonte

