import sys

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.control.Memento import Memento


class Fonte:
    def __init__(self, state: object) -> None:
        self._state = state

    def create_state_memento(self) -> Memento:
        return Memento(self._state)

    def restore_state(self, memento: Memento) -> None:
        self._state = memento.get_state()

    def get_state(self):
    	return self._state
