from pygame.math import Vector2

class GUI:

    def __init__(
            self,
            raw_text: str = '',
            is_visible: bool = False,
            is_active: bool = False,
            top_left_position: Vector2 = Vector2(0, 0),
        ) -> None:
        
        self.raw_text = raw_text
        self.is_visible = is_visible
        self.is_active = is_active
        self.top_left_position = top_left_position

    def key_event_down(self, key: str) -> None:
        if self.is_active:
            self.raw_text += key