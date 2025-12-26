from .game_settings import *
from .module import Module
from .gui import GUI

class Server:

    def __init__(
        self,
        modules_access_amount: int = START_SERVER_MODULES,
        gui_windows_amount: int = START_GUI_WINDOWS_ON_SERVER,
    ) -> None:
        
        self.max_modules = modules_access_amount
        self.gui_windows_amount = gui_windows_amount
        self.modules: list[Module] = []
        self.guis: list[GUI] = []
        
    def add_module(self, module: Module) -> None:
        if len(self.modules) < self.max_modules:
            self.modules.append(module)
    
    def remove_module(self, module) -> None:
        if module in self.modules:
            self.modules.remove(module)

    def remove_module_by_index(self, index: int) -> Module:
        if 0 <= index < len(self.modules):
            module = self.modules[index]
            self.modules.remove(module)

        return module
    
    def key_event_down(self, key: str) -> None:
        for gui in self.guis:
            gui.key_event_down(key)
    
    def tick_update(self) -> None:
        pass

    def draw(self) -> None:
        pass