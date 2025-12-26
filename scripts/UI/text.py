import pygame


# Class Text - represents text in the model (this class optimizes the use of fonts and a text surface
# because pygame.font.Font is very slow)
class Text:
    fonts = {}  # Dictionary of fonts

    def __init__(self, text: str, color: list[int, int, int], size_font: int, type_font: str = None) -> None:
        self.color = color
        self.text_content = text
        font_key = (type_font, size_font)

        if font_key in Text.fonts:
            self.font = Text.fonts[font_key]
        else:
            if type_font:
                self.font = pygame.font.Font(f"fonts/{type_font}.ttf", size_font)
            else:
                self.font = pygame.font.Font(None, size_font)
            
            Text.fonts[font_key] = self.font

        # Render the surface once during init
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()

    def print(self, screen: pygame.Surface, pos: list[float, float], center: bool = False) -> None:
        if center:
            self.rect.center = pos
            screen.blit(self.image, self.rect)
        else:
            self.rect.topleft = pos
            screen.blit(self.image, self.rect)
